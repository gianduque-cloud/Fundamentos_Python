nombre = "Camila"
ciudad = "Santiago"
print(nombre)
print(ciudad)
print(type(nombre))


'''
Crear  tres variables con el nombre de una pelicula,
un videojuego y una asignatura. Muestralas
con print() y aplica  type() a una de ellas.
'''

pelicula = input('ingrese nombre de pelicula ')

videojuego = input('ingresar Nombre videojuego ')
asignatura = input('ingresar asignatura ') 
print(f'''
Pelicula: {pelicula}
videojuego: {videojuego}
asignatura: {asignatura} 

''')
print(type(pelicula))


edad = 16
cantidad = 25
print(edad)
print(cantidad)
print(type(edad))

edad = input('Ingresar edad ')
can_hrnos = input('Ingresar la cantidad de hermanos ')
año_actual = int(input('Ingresar año actual ')) 
print(f'''
Edad:  {edad}
Cantidad de hermanos: {can_hrnos}
año actual: {año_actual}
''')
print(type(año_actual))


precio = 1599.90
altura = 1.65
print(precio)
print(altura)
print(type(altura))


p_producto = float(input('ingresar producto '))
temp = float(input('ingresar temperatura '))
promedio = float(input('ingresar promedio '))
print(f'''
precio del producto: {p_producto}
temperatura: {temp}
promedio: {promedio}
''')
print(type(promedio))

tiene_computador = True
esta_lloviendo = False
print(tiene_computador)
print(esta_lloviendo)
print(type(tiene_computador))

wifi = True
tarea = True
clases = False
print(f'''
hay internet? {wifi}
termine la tarea? {tarea}
mañan hay clases? {clases}
''')

name = input('ingresar nombre ')
cantidad = int(input('ingresar cantidad '))
precio = float(input('imngresar precio '))
dispo = False
print(f'''
Nombre: {name}
Cantidad: {cantidad}
Precio: {precio}
Disponibilidad {dispo}
''')