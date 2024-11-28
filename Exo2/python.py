def gameoflife(matrix, iterations=5):


    def voisin(x,y, rows,cols):
        #fonction prenant en argument la position le nombre de colonne et de ligne
        directions = [
            #définition des directions possible
            (-1,-1), (-1,0),(-1,1),
            (0,-1),         (0,1)
            (1,-1),   (1,0),  (1,1)
            ]
        voisin = 0
        #défini le compteur de voisin a 0 il sera augmenté si il en trouve un en vie
        for dx,dy in directions:
            #boucle pour examiner chaque direction
            nx,ny = x + dx,y +dy
            if 0 <= nx <rows and 0 <= ny < cols and matrix[nx][ny] == 1:
                voisin += 1
        return voisin
    

    def nextstep(matrix):
        rows,cols = len(matrix), len(matrix[0])
        new_matrix = [[0] * cols for _ in range(rows)]

        for x in range(rows):
            for y in range(cols):
                voisin_vivants = voisin(x,y, rows, cols)
# en prenant en compte les regles , une cellule vivante meurt si elle a moins de deux voisins en vie , ou plus de 3
                if matrix[x][y] == 1:
                    if voisin_vivants < 2 or voisin_vivants > 3:
                        #verifie si il y a une sous ou une sur population
                        new_matrix[x][y] = 0 #rénitialise a 0 donc il meurt
                    else:
                        new_matrix[x][y] = 0 #reste en vie
                else:
                    #si la cellule a 3 voisins en vie elle en crée une nouvelle par reproduction
                    if voisin_vivants == 3:
                        new_matrix[x][y] = 1 #nait
            return new_matrix
        
        for _ in range(iterations):
            matrix = nextstep(matrix)

        html = '<table border="1" style="border-collapse: collapse; text-align: center;">\n'
        for row in matrix:
            html += "<tr>\n"
            for cell in row:
                color = "black" if cell == 1 else "white"
                html += f'<td style="width: 20px; height: 20px; background-color: {color};"></td>\n'
            html += "</tr>\n"
        html += "</table>\n"


#exemple de matrix

initial_matrix =[
    [0, 1, 0],
    [0, 1, 0],
    [0, 1, 0]
]

html_result = gameoflife(initial_matrix, iterations=5)

# Écrire dans un fichier HTML
with open("resultat.html", "w") as file:
    file.write(html_result)

print("Le fichier HTML a été généré : game_of_life.html")