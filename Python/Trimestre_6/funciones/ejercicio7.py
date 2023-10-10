"""Ejercicio 7.
Crear una subrutina llamada “Login”, que recibe un nombre de usuario y una contraseña y te devuelve Verdadero si el nombre de usuario es “usuario1” y la contraseña es “asdasd”.
Además recibe el número de intentos que se ha intentado hacer login y si no se ha podido hacer login incremente este valor."""

def validar (usuario, contrasena):   
    user = "usuario1"
    password= "asdasd"
    if usuario == user and password == contrasena:
        return "Verdadero"
    elif usuario == user and password != contrasena:
        return "false_contra"
    elif usuario != user:
        return "false_todo"
  

def login ():
    intentos = 0
    while True:
        long_tex = len("Login")
        espacios = 40 - long_tex // 2
        print(" "*espacios+"Login")
        print("=" * 80)
        user = str(input("Digite su nombre de usuario: "))
        password = str(input("Digite su contraseña: "))
        x = validar(user,password)
        print()
        if "Verdadero" == x:
            print ("Bienvenido")
            break
        elif "false_contra" == x:
            print("Contraseña Incorrecta, intentalo nuevamente")
            intentos+=1
            print("")
        
        elif "false_todo" == x:
            print("Usuario inexistente, intentalo nuevamente")
            intentos+=1
            print("")

    print (f"intentos {intentos}")
login()