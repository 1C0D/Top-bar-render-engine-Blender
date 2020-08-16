bl_info = {
    "name": "TOPBAR render engine",
    "author": "1C0D",
    "version": (1, 3, 0),
    "blender": (2, 81, 0),
    "location": "View3D",
    "description": "TOPBAR render engine",
    "category": "Render",
}

import bpy
from bpy.props import BoolProperty

def drawrender(self, context):
    
    scene = context.scene
    rd = scene.render
    
    layout = self.layout
    row=layout.row(align=True)
    row.scale_x = 0.75     
    row.prop(rd, "engine", text="")
    
def update_render_bool(self,context):
    
    preferences = context.preferences
    addon_prefs = preferences.addons[__name__].preferences
        
    if addon_prefs.tools_object_options_bool:
        bpy.types.VIEW3D_PT_tools_object_options.append(drawrender)
    else:
        bpy.types.VIEW3D_PT_tools_object_options.remove(drawrender)    

def update_render_bool1(self,context):
    
    preferences = context.preferences
    addon_prefs = preferences.addons[__name__].preferences
    
    if addon_prefs.view3D_header_bool:
        bpy.types.VIEW3D_HT_header.append(drawrender)
    else:
        bpy.types.VIEW3D_HT_header.remove(drawrender)
        
    
class TOPBAR_render_engine_prefs(bpy.types.AddonPreferences):
    bl_idname = __name__
    
    view3D_header_bool: BoolProperty(
        name="render engines in view3D_header ",
        update=update_render_bool1,
        description="Quick access render engines in view3D_header "
        , default=True
    )   
    tools_object_options_bool: BoolProperty(
        name="render engines in tools_object_options",
        update=update_render_bool,
        description="Quick access render engines in tools_object_options"
        , default=False
    )   

    def draw(self, context):
        
        layout = self.layout
        layout.prop(self, "view3D_header_bool")
        layout.prop(self, "tools_object_options_bool")
        

        

def register():
    
    bpy.utils.register_class(TOPBAR_render_engine_prefs) 
    bpy.types.VIEW3D_HT_header.append(drawrender) 
    # bpy.types.VIEW3D_PT_tools_object_options.append(drawrender)     
#    bpy.types.VIEW3D_HT_header.prepend(drawrender)  #if you prefer if to the left


def unregister():
    
    bpy.utils.unregister_class(TOPBAR_render_engine_prefs)    
    bpy.types.VIEW3D_HT_header.remove(drawrender)
    bpy.types.VIEW3D_PT_tools_object_options.remove(drawrender)
    

if __name__ == "__main__":
    register()
