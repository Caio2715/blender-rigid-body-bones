bl_info = {
    "name": "Rigid Body Bones",
    "author": "Pauan",
    "version": (1, 0),
    "blender": (2, 80, 0),
    "location": "View3D > Sidebar > Rigid Body Bones",
    "description": "Adds rigid body physics to bones",
    "warning": "",
    "doc_url": "",
    "category": "Physics",
}

from . import properties
from . import armature
from . import bone
from . import utils

from importlib import reload
reload(properties)
reload(armature)
reload(bone)
reload(utils)

# This allows you to right click on a button and link to documentation
def add_object_manual_map():
    url_manual_prefix = "https://docs.blender.org/manual/en/latest/"
    url_manual_mapping = (
        ("bpy.ops.pose.create_rigid_bodies", "scene_layout/object/types.html"),
    )
    return url_manual_prefix, url_manual_mapping

classes = (
    properties.Scene,
    properties.Armature,
    properties.EditBone,
    armature.ResetDimensionsXOperator,
    armature.ResetDimensionsYOperator,
    armature.ResetDimensionsZOperator,
    armature.Panel,
    armature.RigidBodyPanel,
    armature.ConstraintPanel,
    #BONE_PT_rigid_body_bones_bone,
    #BONE_PT_rigid_body_bones_constraint,
)

def register():
    print("REGISTERING")
    from bpy.utils import register_class
    for cls in classes:
        register_class(cls)

    #bpy.utils.register_manual_map(add_object_manual_map)
    #bpy.types.VIEW3D_MT_pose.append(add_menu)

def unregister():
    print("UNREGISTERING")
    #bpy.types.VIEW3D_MT_pose.remove(add_menu)
    #bpy.utils.unregister_manual_map(add_object_manual_map)

    from bpy.utils import unregister_class
    for cls in reversed(classes):
        unregister_class(cls)

if __name__ == "__main__":
    register()