import bpy

from .utils import CustomObjectProperties
from .ui import operators, panels

classes = [CustomObjectProperties]
classes.extend(operators)
classes.extend(panels)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)

    bpy.types.Object.my_props = bpy.props.PointerProperty(type=CustomObjectProperties)


def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)


if __name__ == "__main__":
    register()
