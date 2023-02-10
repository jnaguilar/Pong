import pygame, sys
import colores
from clases import Pelota, Paleta

pygame.init()

# ######################################################################################
def control_Colisiones(r1x, r1y, r1w, r1h, r2x, r2y, r2w, r2h):
    """
        Detecta si dos rectangulos entran en colision
        Recibe Rectangulo1/Rectangulo2 (x,y) (w,h) - posiicion x e y - ancho y alto (w,h)
        Devuelve True o False segun haya o no colision
    """
    if (r1x < r2x + r2w and \
        r1x + r1w > r2x and \
        r1y < r2y + r2h and \
        r1h + r1y > r2y):
        # Colision detectada
        return True
    else:
        # No colision
        return False

def marquesina(jugA, jugB):
    """
        Escribe el score de los jugadores arriba de la pantalla
        Parametros: variables enteras que repesentan el score de los jugadores
        Devuelve:   un objet que es la marquesina a imprimir
    """
    # Marquesina jugadores
    letra = pygame.font.SysFont("Monotype",40,bold=True)
    imagenTextoPresent = letra.render(f"{jugA} {' '*30}  {jugB}", True, colores.GHOST_WHITE, None )
    rectanguloTextoPresent = imagenTextoPresent.get_rect()
    rectanguloTextoPresent.centerx = screen.get_rect().centerx
    rectanguloTextoPresent.centery = 20
    return [imagenTextoPresent, rectanguloTextoPresent]


# Etapa de definiciones
size   = (1000,600)                         #Tupla (x,y) tamaño de la ventana
psBall = (int(size[0]/2),int(size[1]/2))    #Tupla inicio de la pelota
screen = pygame.display.set_mode(size)      #Pantalla de juego
fps    = 30                                 #Cuadros por segundo
clock  = pygame.time.Clock()                #Temporizador del juego
pygame.mouse.set_visible(False)             #Desaparece el puntero del mouse
contJugA = contJugB = 0


# Definimos los actores
ball = Pelota(screen, psBall,(20,20), colores.WHITE, (True,True,True,True) )
jugador_A = Paleta(screen, colores.WHITE_SMOKE, 'izq')
jugador_B = Paleta(screen, colores.WHITE_SMOKE, 'der')

while True:
    # Control de eventos
    for evnt in pygame.event.get():
        if evnt.type == pygame.QUIT:
            sys.exit()

        if evnt.type == pygame.KEYDOWN:
            if evnt.key == pygame.K_q:
                jugador_A.speed = -10
            if evnt.key == pygame.K_a:
                jugador_A.speed = 10

            if evnt.key == pygame.K_o:
                jugador_B.speed = -10
            if evnt.key == pygame.K_l:
                jugador_B.speed = 10

        if evnt.type == pygame.KEYUP:
            if evnt.key == pygame.K_q:
                jugador_A.speed = 0
            if evnt.key == pygame.K_a:
                jugador_A.speed = 0
            if evnt.key == pygame.K_o:
                jugador_B.speed = 0
            if evnt.key == pygame.K_l:
                jugador_B.speed = 0

    # Se dibuja la pantalla
    screen.fill(colores.ST_PATRICK_BLUE )
    pygame.draw.rect(screen, colores.WHITE,((size[0]/2,0),(1,size[1])))

    # Se mueven los actores
    ball.mover()
    jugador_A.mover()
    jugador_B.mover()

    # Control de colisiones
    p  = (int(ball.cordenadas[0]), int(ball.cordenadas[1]), ball.size[0], ball.size[0])
    j1 = (int(jugador_A.posicion[0]), int(jugador_A.posicion[1]), int(jugador_A.ancho),int(jugador_A.alto))
    j2 = (int(jugador_B.posicion[0]), int(jugador_B.posicion[1]), int(jugador_B.ancho),int(jugador_B.alto))
   
    # Colision pelota - J1
    colision = control_Colisiones(p[0], p[1], p[2], p[3], j1[0], j1[1], j1[2], j1[3])
    if colision:
        ball.speed[0] *= -1
    
    # Colision pelota - J2
    colision = control_Colisiones(p[0], p[1], p[2], p[3], j2[0], j2[1], j2[2], j2[3])
    if colision:
        ball.speed[0] *= -1
    
    # Control limites izquierdo y derecho
    if ball.cordenadas[0] <= 0:
        # Jugador B anota
        contJugB += 1
        ball.reset()
    
    if ball.cordenadas[0] + ball.size[0] >= size[0]:
        # Jugador A anota
        contJugA += 1
        ball.reset()

    # Actualizar la pantalla
    cartel = marquesina(contJugA, contJugB)
    screen.blit(cartel[0], cartel[1])
    pygame.display.flip()
    clock.tick(fps)

