lista_cursos = ['Python', 'Django', 'Flask', 'Ruby', 'Java', 'Rust']
lista_cursos_2 = ['c', 'c++', 'Docker']

lista_cursos.append('MongoDB')
lista_cursos.append('C#')
lista_cursos.append('Javascript')

lista_cursos.insert(1, 'Rails')
lista_cursos.insert(0, 'pygame')


lista_cursos.extend(lista_cursos_2)


print(lista_cursos)
print(lista_cursos_2)

lista_cursos.remove('MongoDB')
del lista_cursos[0]

lista_cursos.clear()

print(lista_cursos)










# sub_lista = lista_cursos[::-1]
# print(sub_lista)




# primer_curso = lista_cursos[0]
# print(primer_curso)

# segundo_curso = lista_cursos[1]
# print(segundo_curso)

# ultimo_curso = lista_cursos[4]
# print(ultimo_curso)

# lista_cursos[4] = 'Rust'
# print(lista_cursos)




