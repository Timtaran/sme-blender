import bpy


class CustomObjectProperties(bpy.types.PropertyGroup):
    object_name: bpy.props.StringProperty(name="object_name")
