import bpy

start_frame = bpy.context.scene.frame_start
end_frame = bpy.context.scene.frame_end

for f in range(start_frame, end_frame + 1):
    for scene_object in bpy.context.scene.objects:
        if scene_object.type == "ARMATURE":
            for bone in scene_object.pose.bones:
                print(bone.name)
                print(bone.matrix.to_quaternion().to_axis_angle())
                print(scene_object.matrix_world @ bone.matrix)
                print(bone.location.x)
                print(bone.matrix.to_quaternion().to_axis_angle()[0].x)
