#----------------PARTE 1-------------------------#
# CREAR UNA ESFERA

import bpy

#creamos la funcion de crear una esfera
def create_uv_sphere():
    # Seleccionamos todos los objetos presente en la escena y los eliminamos.
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete(use_global=False)
    
   # Creamos la nueva esfera y la serelcionamos
    bpy.ops.mesh.primitive_uv_sphere_add(location=(0,0,0))
    sphere = bpy.context.object
    sphere.name = "Sphere"
    sphere.scale = (2, 2, 2)
    sphere.select_set(True)

# Ejecutamos la funcion de crear una esfera
create_uv_sphere()
