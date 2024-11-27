# Copyright 2018-2019 Windy Darian. MIT License.
'''
Toggle all bone constraints in the armature named "armature"
Blender 2.79b
'''

import bpy

_ignored_bones = ['forearm_twist.R', 'forearm_twist.L']
_armature_name = 'armature'
'''
def disable_bone_constraints():
    obj = bpy.data.objects.get(_armature_name)
    for bone in obj.pose.bones:
        for con in bone.constraints:
            con.mute = True

def enable_bone_constraints():
    obj = bpy.data.objects.get(_armature_name)
    for bone in obj.pose.bones:
        for con in bone.constraints:
            con.mute = False
'''
def toggle_bone_constraints():
    obj = bpy.data.objects.get(_armature_name)
    for bone in obj.pose.bones:
        if bone.name in _ignored_bones:
            continue
        for con in bone.constraints:
            con.mute = not con.mute

if __name__ == '__main__':
    toggle_bone_constraints()
    print('Job done!')
