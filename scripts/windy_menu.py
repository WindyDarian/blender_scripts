# Copyright 2022 Windy Darian. MIT License.
# Created on December 20, 2022
import bpy


class WindyView3dMenu(bpy.types.Menu):
    bl_idname = "VIEW3D_MT_windy"
    bl_label = "windy"
    def draw(self, context):
        pass

def draw_windy_menu(self, context):
    self.layout.menu(WindyView3dMenu.bl_idname)

def register():
    bpy.utils.register_class(WindyView3dMenu)
    bpy.types.VIEW3D_MT_editor_menus.append(draw_windy_menu)

def unregister():
    bpy.types.VIEW3D_MT_editor_menus.remove(draw_windy_menu)
    bpy.utils.unregister_class(WindyView3dMenu)

if __name__ == '__main__':
    register()