'''Escriba una fecha en formato ISO'''

import datetime as d

fecha_actual = d.datetime.now().isoformat()
print(fecha_actual)