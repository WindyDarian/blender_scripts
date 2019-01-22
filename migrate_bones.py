# Copyright 2017-2019 Windy Darian. MIT License.
# Created on May 13, 2017
'''
ummmmm....just used to copy bone transformations
'''
import bpy

def copy_bone_matrices():
    obj_metarig = bpy.data.objects.get('metarig')
    if obj_metarig is None or obj_metarig.type != 'ARMATURE':
        pass  #TODO: raise an exception
    obj_newrig = bpy.data.objects.get('metarig_2')
    if obj_newrig is None or obj_newrig.type != 'ARMATURE':
        pass  #TODO: raise an exception
    for bone in obj_newrig.data.edit_bones:
        old_bone = obj_metarig.data.bones.get(bone.name)
        if not old_bone:
            continue
        bone.matrix = old_bone.matrix_local # Difference between bpy.types.EditBone and bpy.types.Bone
        bone.length = old_bone.length

if __name__ == '__main__':
    copy_bone_matrices()
    print('Job done!')
