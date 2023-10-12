def crear_calculadora(a,b):
    def calcular(*args, **kwargs):
        rtas={}

        for op in args:
        
            if op == "+":
                op="Suma"
                rtas[op]= a+b
    
            elif op == "-":
                op="Resta"
                rtas[op]= a-b
            elif op == "*":
                op="Multiplicacion"
                rtas[op]= a*b
            elif op == "/":
                op="Division"
                if b != 0:
                     rtas[op]= a/b
                else:
                    return "Error: División por cero no permitida"
            else:
                return "Operador no válido"
        for clave , valor in rtas.items():
            print(f"{clave} = {valor}")

    return calcular

operacion = crear_calculadora(5,10)

(operacion('+','-','*','/'))