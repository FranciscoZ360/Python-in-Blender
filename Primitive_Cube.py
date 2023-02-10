import bpy

#creamos la funcion de crear un cubo
def create_cube():
    # Seleccionamos todos los objetos presente en la escena y los eliminamos.
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete(use_global=False)
    
    # Creamos un nuevo cubo
    bpy.ops.mesh.primitive_cube_add(size=2, location=(0,0,0), rotation=(0,0,0))
    cube = bpy.context.object
    cube.select_set(True)

# Ejecutamos la funcion de crear un cubo
create_cube()
