import bpy

def create_uv_sphere():
    # Eliminar cualquier objeto existente en la escena
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete(use_global=False)
    
    # Crear un nuevo cubo y seleccionarlo
    bpy.ops.mesh.primitive_uv_sphere_add(location=(0,0,0))
    sphere = bpy.context.object
    sphere.name = "Sphere"
    sphere.scale = (2, 2, 2)
    sphere.select_set(True)

# Ejecutar la función para crear un cubo
create_uv_sphere()
