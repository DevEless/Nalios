def sum(nombres):
    if not nombres:
        #si la liste est vide, return 0
        return 0
    return nombres[0] + sum(nombres[1:])
#nombres[0] indique l'index du premier element , nombres[1:] prends en compte tous les elements sauf le premier
#la fonction ajoute le premier element a la sommes des autres


#test

nombres = [2.5, 4.0, -2.0, 11.0]
result = sum(nombres)
print({result})