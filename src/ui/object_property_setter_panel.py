from bpy.types import Panel, Context


class ObjectPropertySetterPanel(Panel):
    bl_label = "Property Setter"
    bl_idname = "SME_PROPERTYSETTER_PT_panel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "SME"
    bl_order = 0

    def draw(self, context: Context):
        layout = self.layout
        obj = context.object

        box = layout.box()
        row = box.row()
        row.label(text="Model Data", icon="OUTLINER_DATA_ARMATURE")
        if obj and obj.type == "ARMATURE":
            row = box.row()
            row.label(text=f"Selected object: {obj.name}")

            row = box.row()
            row.prop(
                obj.my_props,
                "object_name",
                text="Assigned model",
                icon="OUTLINER_DATA_MESH",
                expand=True,
            )
        else:
            row = box.row()
            row.label(text="Select an Armature to see details.")
