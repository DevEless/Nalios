def gameoflife(matrix, iteration=5):


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
    

    