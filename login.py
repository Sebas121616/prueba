Usuario = "2"
datos = "1"
while Usuario != datos:
    datos = input("Ingrese su nombre de usuario: ")
    Usuario = "Sebas"
    if datos == Usuario:
        print ("Su usuario es correcto")
    else:
        Usuario = input("Ingrese su nuevo usuario: ")
        print("Su usuario es incorrecto")