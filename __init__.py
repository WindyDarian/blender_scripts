bl_info = {
    "name": "Windy Blender Scripts",
    "version": (0, 0, 1),
    "author": "Windy Darian",
    "blender": (3, 0, 0),
    "description": "A collection of scripts for Windy Darian's game workflow.",
    "category": "Development",
}

from .scripts import rigify_constrain_meta_to_generated
import bpy


def register():
    rigify_constrain_meta_to_generated.register()

def unregister():
    rigify_constrain_meta_to_generated.unregister()