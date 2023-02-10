import pygame, random

class Bloque:
    def __init__(self, screen, cordenada, tamano, color) -> None:
        self.screen = screen        #Pantalla donde se dibuja el bloque
        self.cordenada = cordenada  #Posicion (x,y)
        self.tamano = tamano        #Posicion (w,h)
        self.color = color          #Color del bloque
    
    def dibujar(self):
            pygame.draw.rect(self.screen,self.color, (self.cordenada, self.tamano))


class Pelota:
    def __init__(self, screen, pBall, tamano, color, limites):
        self.screen  = screen   #obj screen es la pantalla actual
        self.pBall   = pBall    #Posicion (x,y) de iniciio de la bola
        self.size    = tamano   #Tamaño (w,h)
        self.color   = color    #Tupla (r,g,b): Define el color de la pelota
        self.speed   = [10,10]  #Lista (x,y)    
        self.limites = limites  #Tupla (arriba, abajo, izq, der)
        self.cordenadas = [self.pBall[0], self.pBall[1]]
        self.reset()
    
    def dibujar(self):
        pygame.draw.rect(self.screen,self.color, (self.cordenadas , self.size))
    
    def cntrLimites(self):
        """
            Controla no sobrepasar los limites de la pantalla dada la
            tupla (arriba, abajo, izquierda, derecha) sean True o False
        """
        if self.limites[0] and self.cordenadas[1] < 0:
            # Limite superior de la pantalla
            self.speed[1] *= -1

        if self.limites[1] and self.cordenadas[1] > pygame.display.Info().current_h - self.size[0]:
            # Limite inferior de la pantalla
            self.speed[1] *= -1
        
        if self.limites[2] and self.cordenadas[0] < 0:
            # Limite izquierdo de la pantalla
            self.speed[0] *= -1

        if self.limites[3] and self.cordenadas[0] > pygame.display.Info().current_w - self.size[1]:
            # Limite derecho de la pantalla
            self.speed[0] *= -1

    def mover(self):
        self.cordenadas[0] += self.speed[0]
        self.cordenadas[1] += self.speed[1]
        
        self.cntrLimites()
        self.dibujar()
    
    def reset(self):
        self.speed[0] = random.choice((10,-10))
        self.speed[1] = random.choice((10,-10))

        self.cordenadas[0] = pygame.display.Info().current_w / 2
        self.cordenadas[1] = pygame.display.Info().current_h / 2


class Paleta:
    def __init__(self, scr, color, posicion):
        self.screen   = scr              #obj screen es la pantalla actual
        self.color    = color
        self.ancho    = 20
        self.alto     = 80
        self.speed    = 0

        if posicion == 'izq':
            cordX = 10
        else:
            cordX = pygame.display.Info().current_w - self.alto / 2 + 10
        cordY = pygame.display.Info().current_h / 2 - self.alto / 2
        self.posicion = [cordX, cordY]    # Lista (x,y) por parametro viene solo si es izq o der 


    def  dibujar(self):
        """
            Dibuja el rectangulo de la paleta
            Obj Rect = Rect((left, top), (width, height))
        """
        pos = (self.posicion,(self.ancho,self.alto))
        pygame.draw.rect(self.screen,self.color, pos)

    def cntrl_limites(self):
        if self.posicion[1] < 0:
            self.posicion[1] = 0
        
        if self.posicion[1] + self.alto > pygame.display.Info().current_h:
            self.posicion[1] = pygame.display.Info().current_h - self.alto
    
    def mover(self):
        self.posicion[1] += self.speed
        self.cntrl_limites()
        self.dibujar()










