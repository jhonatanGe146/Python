"""2. Función generadora de direcciones IP versión4. Una dirección IP es un conjunto de 4 numeros (octetos binarios) que se convierten a decimal.
Ejemplo de una dirección IP 190.8.176.187, teniendo en cuenta que cada numero corresponde a un octeto siempre debe estar en el rango de 0 a 255 (00000000 a 11111111)

Escriba un decorador para funciones que usan como parámetro una o varias direcciones IP, la decoradora debe validar si los numeros de las direcciones estan en el rango adecuado,
es decir 0 a 255. En caso de no estarlo debe emitir un mensaje de error. Si esta bien, debe dejar ejecutar la función. 

Las funciones a decorar pueden ser:
1. Determinar la clase a la que pertenece una dirección IP que se pasa como parámetro
2. Decir cuantos host puede direccionar una dirección IP que se pasa como parámetro
3. Decir si una dirección IP pasada como parámetro es pública o privada
4. Decir la mascara de subred que tiene la dirección pasada como parámetro
5. Hacer subneting con la dirección pasada como parámetro."""




def trabajando_IP ():
    print('Inicia El Procesamiento De IP')
    def operando_IP(*args, **kwargs):
        try:
            for index, ips in enumerate(args):
                octetos = ips.split('.')  # Divide la dirección IP en octetos
                for octeto in octetos:
                    if len(octeto) < 0 or len(octeto) >255:
                        raise TypeError
            
            
        
       
            #fun(*args, **kwargs)
        except TypeError:
            print("IP fuera de rango")

    return operando_IP

x = trabajando_IP()
x("190.8.176.187", "191.9.136.10000")


