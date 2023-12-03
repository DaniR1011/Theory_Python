nombres = ["A", "B", "C", 5]
position = 1
for nombre in nombres:
 print(position)
 position+=1
 print(nombre)

 s = "Hola a todos"
 for letra in s:
  print(letra + "-")

  i = 1
  while i <= 10:
   print(i)
   i += 1

patatas = 5
tomates = 3
naranjas = 7

productos = [patatas, tomates, naranjas]
print(productos)

total = 0
for producto in productos:
 total += producto
 print(total)
print(total)

tareas = ["T1", "T2", "T3", "T4"]

while len(tareas) > 0:
 tarea_actual = tareas.pop(0)
 print(f"Estoy completando la tarea {tarea_actual}")
print('Puedes ver Netflix')

estudiante = {
 'nombre': 'Daniel',
 'apellido': 'Recio'
}
for clave, valor in estudiante.items():
 print(clave, ":", valor)

numeros = [5, 8, 10, -3, 2, 1]
for numero in numeros:
 print(numero)
 if numero < 0:
  print("El primer número negativo es:", numero)
  break # Una vez encuentra un número negativo, el bucle se termina.