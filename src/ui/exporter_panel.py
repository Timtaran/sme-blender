import base64
import json
import os
import zlib

from bpy.types import Panel, Context, Operator
from abc import abstractmethod

from ..exporter import SceneExporter
from ..utils import EnhancedJSONEncoder


class SceneExporterPanel(Panel):
    bl_label = "Scene Exporter"
    bl_idname = "SME_ANIMATIONEXPORTER_PT_panel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "SME"
    bl_order = 1

    def draw(self, context: Context):
        layout = self.layout

        box = layout.box()
        row = box.row()
        row.operator(
            operator="sme.copy_scene_to_clipboard",
            text="Export Scene",
            icon="RENDER_ANIMATION",
        )


class BaseSceneExporterOperator(Operator):
    @staticmethod
    def _export_scene(context: Context) -> str:
        return json.dumps(
            SceneExporter.export(
                f"{os.path.splitext(os.path.basename(context.blend_data.filepath))[0]}_{context.scene.name}", context
            ),
            cls=EnhancedJSONEncoder,
        )

    @abstractmethod
    def execute(self, context):
        return self._export_scene(context)


class CopySceneToClipboardOperator(BaseSceneExporterOperator):
    bl_idname = "sme.copy_scene_to_clipboard"
    bl_label = "Copy to clipboard"

    def execute(self, context):
        context.window_manager.clipboard = self._export_scene(context)
        self.report({"INFO"}, "Successfully copied scene data to clipboard")
        return {"FINISHED"}
