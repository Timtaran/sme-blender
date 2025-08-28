from bpy.types import Context
from mathutils import Vector

from ..models import Scene, Keyframe, Action, ActionTypes


class SceneExporter:
    @staticmethod
    def export(name: str, context: Context) -> Scene:
        scene = Scene(name=name, keyframes=[], models={})
        start_frame = context.scene.frame_start
        end_frame = context.scene.frame_end

        for scene_object in context.scene.objects:
            if scene_object.type == "ARMATURE":
                scene.models[scene_object.name] = scene_object.my_props.object_name

        for f in range(start_frame, end_frame + 1):
            keyframe = Keyframe(frame=f, actions=[])

            for scene_object in context.scene.objects:
                if scene_object.type == "ARMATURE":
                    for bone in scene_object.pose.bones:
                        rotations = bone.matrix.to_quaternion().to_axis_angle()

                        keyframe.actions.append(
                            Action(
                                type=ActionTypes.MODEL,
                                umid=scene_object.name,
                                object_name=scene_object.my_props.object_name,
                                bone_name=bone.name,
                                coords=bone.matrix.to_translation(),
                                rotations=Vector((rotations[0].x, rotations[0].y, rotations[0].z, rotations[1])),
                            )
                        )

            scene.keyframes.append(keyframe)

        return scene
