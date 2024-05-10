nombre = 'Julian'
apellido = 'Velez G'

# nombre_completo = nombre + apellido

# nombre_completo = 'Mr. %s %s.' %(nombre, apellido)

nombre_completo = 'Mr. {nombre} {primer_apellido} {segundo_apellido}.'.format(
nombre=nombre,
primer_apellido=apellido,
segundo_apellido='Gaitan'
)

print(nombre_completo)

