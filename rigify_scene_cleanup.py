# Copyright 2017 Windy Darian (Ruoyu Fan). MIT License.
# Created on August 20, 2017
'''
This script will parent all objects whose name start with "WGT-" to an empty
object.... just to clean up the view...

Tested with Blender 2.78c
'''
import bpy

WGT_parent_object_name = "rigify_WGT"

def rigify_scene_cleanup():
    root_object = bpy.data.objects.get(WGT_parent_object_name)
    if not root_object:
        root_object = bpy.data.objects.new(WGT_parent_object_name, None)
        bpy.context.scene.objects.link(root_object)
    for obj in bpy.data.objects:
        if obj.name.startswith("WGT-"):
            obj.parent = root_object

if __name__ == '__main__':
    rigify_scene_cleanup()
    print('Job done!')
