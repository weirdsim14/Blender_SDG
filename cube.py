import bpy
import mathutils

# Function to make the camera look at a target
def look_at(obj, target):
    direction = target - obj.location
    rot_quat = direction.to_track_quat('-Z', 'Y')
    obj.rotation_euler = rot_quat.to_euler()

# Clear existing objects
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete()

# Create a cube
bpy.ops.mesh.primitive_cube_add(size=2, enter_editmode=False, align='WORLD', location=(0, 0, 0))
cube = bpy.context.object
cube.location.x += 1.0
cube.rotation_euler.y += 1.57
# Add a basic material (optional)
material = bpy.data.materials.new(name="CubeMaterial")
material.diffuse_color = (1, 0, 0, 1)  # Red color
cube.data.materials.append(material)

# Setup camera
cam = bpy.data.cameras.new("Camera")
cam_obj = bpy.data.objects.new("Camera", cam)
bpy.context.scene.collection.objects.link(cam_obj)
bpy.context.scene.camera = cam_obj
cam_obj.location = (5, 5, 5)

# Point camera to cube
look_at(cam_obj, cube.location)

# Add a light source
light_data = bpy.data.lights.new(name="Light", type='POINT')
light_data.energy = 1000
light_obj = bpy.data.objects.new(name="Light", object_data=light_data)
bpy.context.scene.collection.objects.link(light_obj)
light_obj.location = (3, 3, 5)

# Render settings
bpy.context.scene.render.image_settings.file_format = 'PNG'
bpy.context.scene.render.filepath = './image.png'
bpy.context.scene.render.resolution_x = 1920
bpy.context.scene.render.resolution_y = 1080

# Render the scene
bpy.ops.render.render(write_still=True)
