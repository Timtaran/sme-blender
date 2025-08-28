__all__ = ["operators", "panels"]

from .object_property_setter_panel import ObjectPropertySetterPanel
from .exporter_panel import SceneExporterPanel, CopySceneToClipboardOperator

operators = [CopySceneToClipboardOperator]
panels = [SceneExporterPanel, ObjectPropertySetterPanel]
