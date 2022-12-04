bl_info = {
    "name": "Windy Blender Scripts",
    "version": (0, 0, 1),
    "author": "Windy Darian",
    "blender": (3, 0, 0),
    "description": "A collection of scripts for Windy Darian's game workflow.",
    "category": "Development",
}

from .scripts.rigify_constrain_meta_to_generated import AddMetarigConstraints
import bpy


def register():
    bpy.utils.register_class(AddMetarigConstraints)

def unregister():
    bpy.utils.unregister_class(AddMetarigConstraints)