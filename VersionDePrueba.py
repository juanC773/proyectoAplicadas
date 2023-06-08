#Laberinto //Matrices

#Importaciones
import turtle #Turtle permite crear una ventana de dibujo y controlar una tortuga virtual que puede moverse y dibujar líneas en la pantalla. La tortuga puede cambiar de dirección, cambiar de color, moverse hacia adelante y hacia atrás y mucho más. El módulo turtle también incluye funciones para configurar la apariencia de la tortuga y de las líneas que dibuja.
import math
import sys 

#Style
turtle.register_shape('marioRight.gif')
turtle.register_shape('marioLeft.gif')
turtle.register_shape('muroJuego.gif')
turtle.register_shape('starr.gif')
turtle.register_shape('ghost.gif')


#Visualización // ventana
window= turtle.Screen()

#Fondo
window.bgcolor(0,0,0) # RGB color negro

#Nombre de la ventana
window.title("Bienvenido al juego!")

#Tamaño de la ventana
window.setup(800,800)

import os
print(os.getcwd())


#Dibuja el tablero
class Pen(turtle.Turtle):
    def __init__(self):
        
        turtle.Turtle.__init__(self)
        self.shape('square')
        self.color('white')
        self.penup()
        self.speed(0)

 


#Niveles
levels = ['']       


# primer nivel
# Definimos el nivel del laberinto
LEVEL1 = [
    '#########################',
    '#s                    E #',
    '################ ########',
    '#                       #',
    '# # ##########  # ## ## #',
    '# #             # #     #',
    '# ############# # # # # #',
    '# #           # # # # # #',
    '# # ######### # # # # # #',
    '# # #       # # # # # # #',
    '# # # ##### # # # # # # #',
    '# # # #  T# # # # # # # #',
    '# # # # ### # # # # # # #',
    '# # # #     # # # # # # #',
    '# # # ##### # # # # # # #',
    '# # #       # # # # # # #',
    '# # # ####### # # # # # #',
    '#             # # # # # #',
    '# ############# # # # # #',
    '# #           # # # # # #',
    '# # ######### # # # # # #',
    '# # #       # # # # # # #',
    '# # # ##### # # # # # # #',
    '# # # #   # # # # # # # #',
    '#########################'
    
]

LEVEL2 = [
    '#########################',
    '##       ##########   T##',
    '## #####        ### #####',
    '## ##### ########## #####',
    '## ##### ########## #####',
    '##   ###            #####',
    '####    #################',
    '###  # ###        #######',
    '### ## ##### ####      ##',
    '### ## #####    ###### ##',
    '### ########### ###### ##',
    '###          #  ###### ##',
    '############ ## ###### ##',
    '###           # ###### ##',
    '### ####### ### ###### ##',
    '#   ####### ### ###### ##',
    '### ####### ### ###### ##',
    '###     ### ###        ##',
    '### ####### ##  #### ####',
    '#   ####### ##  #### ####',
    '# ##      # ## ##    ####',
    '# #  ###### ## ##### ####',
    '# # ##### # ## ##### ####',
    '#s                   ####',
    '#########################'
]
#en las filas o columnas donde hay # son los muros  

import numpy as np

# Replace characters with numerical values
mapping = {'#': 1, ' ': 0, 's': 2, 'T': 3, 'E':4}
LEVEL1 = [[mapping[ch] for ch in row] for row in LEVEL1]



mappingLevel2 = {'#': 1, ' ': 0, 's': 2, 'T': 3, 'E':4}
LEVEL2 = [[mappingLevel2[ch] for ch in row] for row in LEVEL2]


#Agregar el laberinto a los niveles

levels.append(LEVEL1) #Agrega el nivel 1

levels.append(LEVEL2)


#Crea al jugador
class PlayerSkin(turtle.Turtle):
     
     def __init__(self):
        
        turtle.Turtle.__init__(self)
        self.shape('marioRight.gif')
        self.color('red')
        self.penup()
        self.speed(0)
        self.win= 0
        

     
        #Atributos del jugador
     def up(self):
        nextStepRow= skin.xcor()
        nextStepColumn= skin.ycor() + 24

        if(nextStepRow, nextStepColumn) not in walls:
            self.goto(self.xcor(), self.ycor() + 24)

     def down(self):
        nextStepRow= skin.xcor()
        nextStepColumn= skin.ycor() - 24
     
        if(nextStepRow, nextStepColumn) not in walls:
            self.goto(self.xcor(), self.ycor() - 24)


     def left(self):
       
        nextStepRow= skin.xcor() -24
        nextStepColumn= skin.ycor()
        self.shape('marioLeft.gif')

        if(nextStepRow, nextStepColumn) not in walls:
            self.goto(self.xcor() -24 , self.ycor())


     def right(self):
         
        nextStepRow= skin.xcor() +24
        nextStepColumn= skin.ycor()
        self.shape('marioRight.gif')

        if(nextStepRow, nextStepColumn) not in walls:
            self.goto(self.xcor()+24, self.ycor())


     def check_collision(self, enemy):
        a = self.xcor() - enemy.xcor()
        b = self.ycor() - enemy.ycor()

        distance = math.sqrt((a**2) + (b**2))

        if distance < 5:  
            return True  # Mario ha muerto
        else:
            return False


     def endGame(self, findTreasure):
         a = self.xcor() - findTreasure.xcor()
         b = self.ycor() - findTreasure.ycor()

         distance = math.sqrt((a**2)+(b**2))

         if distance<5:
             return True
         else:
             return False
        
    




# Clase enemigo


class EnemySkin(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape('ghost.gif')
        self.color('red')
        self.penup()
        self.speed(0)
        self.win = 0

    def follow_player(self, player):
        a = player.xcor() - self.xcor()
        b = player.ycor() - self.ycor()
        distance = math.sqrt((a ** 2) + (b ** 2))

        if distance < 250:  # Ajusta este valor para determinar cuándo Bowser debe comenzar a seguir a Mario
            angle = math.atan2(b, a)
            self.setheading(math.degrees(angle))
            self.forward(0.8)  # velocidad (recomendada en 2)



     
    


draw= Pen() #Crear instancias de clase
skin= PlayerSkin()

enemy= EnemySkin()

#Lista de cordenadas 
walls = []

tesoros= []


#Generar laberinto
def configMaze(anyLevel):     #el nivel es un arreglo bidimensional, es decir una matriz
  
    for column in range(len(anyLevel)):
        for row in range(len(anyLevel[column])):  #Solo tomamos la columna válida
            
            character = anyLevel[column][row] #obtener los caracteres en cada cordenada (x,y)

            screenRow = -288 + (row * 24) #Saber en que posicion estamos parados 
            screenColumn = 288 - (column * 24)


            # si el caracter es '#' imprimimos ese muro
            if character == 1:
                draw.goto(screenRow, screenColumn)
                draw.shape('muroJuego.gif')
                draw.stamp()

                #agrega las cordenadas
                walls.append((screenRow,screenColumn))
            
            if character == 2:
                skin.goto(screenRow, screenColumn)

            if character == 3:
                tesoros.append(TesoroToWin(screenRow,screenColumn))

            if character == 4:
                enemy.goto(screenRow, screenColumn)






#Tesoro final 
class TesoroToWin(turtle.Turtle):
     
     def __init__(self, row, column):
        
        turtle.Turtle.__init__(self)
        self.shape('starr.gif')
        self.color('red')
        self.penup()
        self.speed(0)
        self.win= 1000
        self.goto(row,column)

     def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()
   


#alteraciones

#matriz transpuesta 
LEVEL1 = np.array(LEVEL1)
matriz_transpuesta = np.transpose(LEVEL1)


#matriz espejo
# Invertir el orden de las filas o columnas 
matriz_rotada = np.flip(LEVEL1, axis=0)  

#axis =1 horizontal, es decir filas
#axis = 0 vertical, es decir columnas







# Configurar el nivel
configMaze(LEVEL1)

# movimiento
turtle.listen()

# presiona flechas de movimiento
turtle.onkey(skin.up, 'Up')
turtle.onkey(skin.down, 'Down')
turtle.onkey(skin.left, 'Left')
turtle.onkey(skin.right, 'Right')

window.tracer(0)  # Reduce la cantidad de veces que se actualiza la pantalla para optimizar

# Ciclo del juego
while True:
    for tesoro in tesoros:
        if skin.endGame(tesoro):
            skin.win += tesoro.win
            print('Level passed, score: {}'.format(skin.win))

            tesoro.destroy()
            tesoros.remove(tesoro)

    if len(tesoros) == 0:  # Si no quedan tesoros en el nivel actual
          print("you've won")
          sys.exit()
       

       

    if skin.check_collision(enemy):
        # Realizar acciones cuando Mario muere
        skin.hideturtle()
        print("End Game")
        sys.exit()

    # Hacer que Bowser siga a Mario
    enemy.follow_player(skin)

    # Actualizar la pantalla cada vez que presionamos una flecha
    window.update()
