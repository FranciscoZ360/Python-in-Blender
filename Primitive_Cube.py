#----------------PARTE 1-------------------------#
# CREAR UN CUBO
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

#----------------PARTE 2-------------------------#
# MODIFICAR LOS VECTORES

def change_cube_vectors():
    # Seleccionamos na vez mas el cubo
    bpy.ops.object.select_all(action='DESELECT')
    bpy.data.objects['Cube'].select_set(True)
    cube = bpy.context.object
    
    # Accedemos a la malla de nuestro cubo
    mesh = cube.data
    
    # Modificamos los vectores del cubo dandole un valor a sus cordenadas.
    for vertex in mesh.vertices:
        vertex.co.x *= 2
        vertex.co.y *= 1
        vertex.co.z *= 3
    
    # Actualizamos los cambios en la la malla
    mesh.update()

# Ejecutamos la funcion para cambiar los vectores del cubo
change_cube_vectors()

#----------------PARTE 3-------------------------#
# APLICAR MODIFICADORES

def add_subdivisions_to_cube():
    # Seleccionar el objeto cubo
    bpy.ops.object.select_all(action='DESELECT')
    bpy.data.objects['Cube'].select_set(True)
    cube = bpy.context.object
    
    # Acceder a la malla del objeto
    mesh = cube.data
    
    # Añadir subdivisiones a la malla
    bpy.ops.object.modifier_add(type='SUBSURF')
    subsurf_modifier = mesh.modifiers["Subsurf"]
    subsurf_modifier.levels = 2
    
    # Actualizar la malla
    mesh.update()

# Ejecutar la función para añadir subdivisiones al cubo
add_subdivisions_to_cube()
