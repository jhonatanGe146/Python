cadena=str (input("Ingrese el texto: "))

#!6- Determinar en que tiempo esta conjugado un verbo.
def verb_tiempo(verbo):
    seg_verb=(verbo[-1:])
    seg_verb2=(verbo[-2:-1])
    if seg_verb2 == chr(82) or seg_verb2 == chr (114):
        return ("Verbo en futuro")
    elif seg_verb == chr(225) or seg_verb == chr(193) or seg_verb == chr(233) or seg_verb == chr(201) or seg_verb == chr(237) or seg_verb == chr(205) or seg_verb == chr(243) or seg_verb == chr(211) or seg_verb == chr (250) or seg_verb == chr (218):
        return ("Verbo en Pasado")
    elif seg_verb == chr(97) or seg_verb == chr(65) or seg_verb == chr(101) or seg_verb == chr(69) or seg_verb == chr(105) or seg_verb == chr(73) or seg_verb == chr(111) or seg_verb == chr(79) or seg_verb == chr (117) or seg_verb == chr (85):
        return ("Verbo en presente")

#print (verb_tiempo(cadena))