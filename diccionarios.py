#diccionarios

dict={}
#print(type(dict))

telefonos={
    "pablo":43234243,
    "marta":34345667,
    "laura":56464646,
    "pedro":55645546
}
print(telefonos['pablo'])#print(telefonos)
print(telefonos.get('marta'))

#para borrar una key
del telefonos['pedro']
print(telefonos)

borrado=telefonos.pop('marta')
print(telefonos)
print(borrado)

# unir diccionarios
personas={
    'usuario1':'pablo',
    'usuario2':'laura',
    'usuario3':'pedro'
}

paises={
    'pais1':'Bolivia',
    'pais2':'Argentina',
    'pais3':'Peru'
}
personas.update(paises)
print(personas)