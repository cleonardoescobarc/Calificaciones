print ("Vamos a calificar su rendimiento")
print ("Se clasificara en A, B, C Y R")
nota = float(input("Ingrese su calificacion: "))

if nota>9.0:
    print("Su calificacion es: ", nota, "Usted tiene A")

elif nota>8.0:
    print("Su calificacion es: ", nota, "Usted tiene B")
elif nota >= 7.5:
    print("Su calificacion es: ", nota, "Usted tiene C")

else:
    print("Su calcification es: ", nota, "Por ende desaprobo, usted tiene F")
