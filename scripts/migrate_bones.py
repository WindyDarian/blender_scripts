# Copyright 2017 Windy Darian. MIT License.
# Created on May 13, 2017
'''
Used to copy bone transforms from one armature to another
I use this script to move to a new rigify metarig after an version update
'''
import bpy

def copy_bone_matrices(old_armature_name, new_armature_name):
    obj_fromrig = bpy.data.objects.get(old_armature_name)
    if obj_fromrig is None or obj_fromrig.type != 'ARMATURE':
        print('obj_fromrig invalid')
        return
    obj_torig = bpy.data.objects.get(new_armature_name)
    if obj_torig is None or obj_torig.type != 'ARMATURE':
        print('obj_torig invalid')
        return
    # New rig must be in edit mode.
    for bone in obj_torig.data.edit_bones:
        old_bone = obj_fromrig.data.bones.get(bone.name)
        if not old_bone:
            print('unable to find old bone for ', bone.name)
            continue
        bone.matrix = old_bone.matrix_local # Difference between bpy.types.EditBone and bpy.types.Bone
        bone.length = old_bone.length

if __name__ == '__main__':
    copy_bone_matrices('armature', 'metarig')
    print('Job done!')