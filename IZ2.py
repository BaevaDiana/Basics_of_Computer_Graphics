import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import math

def draw():
    glRotatef(0, 0, 0, 0)

#левый кузов
    glColor4f(0.0, 0.0, 1.0, 0.0)
    glBegin(GL_QUADS)
    glVertex3f(0.5, 0.5, 1)
    glVertex3f(0.5, -1.5, 1)
    glVertex3f(0.5, -1.5, 0)
    glVertex3f(0.5, 0.5, 0)
    glEnd()

#кузов передний маленький
    glColor4f(0.0, 0.0, 1.0, 0.0)
    glBegin(GL_QUADS)
    glVertex3f(0.5, 0.5, 1)
    glVertex3f(1, 0.5, 1)
    glVertex3f(1, 0.5, 0)
    glVertex3f(0.5, 0.5, 0)
    glEnd()

#правый кузов
    glColor4f(0.0, 0.0, 1.0, 0.0)
    glBegin(GL_QUADS)
    glVertex3f(1, 0.5, 1)
    glVertex3f(1, 0.5, 0)
    glVertex3f(1, -1.5, 0)
    glVertex3f(1, -1.5, 1)
    glEnd()

#кузов посередине сзади
    glColor4f(0.0, 0.0, 1.0, 0.0)
    glBegin(GL_QUADS)
    glVertex3f(1, -1.5, 1)
    glVertex3f(1, -1.5, 0)
    glVertex3f(0.5, -1.5, 0)
    glVertex3f(0.5, -1.5, 1)
    glEnd()

#кузов дно
    glColor4f(0.0, 0.0, 1.0, 0.0)
    glBegin(GL_QUADS)
    glVertex3f(0.5, 0.5, 0)
    glVertex3f(0.5, -1.5, 0)
    glVertex3f(1, 0.5, 0)
    glVertex3f(1, -1.5, 0)
    glEnd()

#кабина левая сторона
    glColor4f(0.0, 1.0, 1.0, 1.0)
    glBegin(GL_QUADS)
    glVertex3f(0.5, 0.5, 0)
    glVertex3f(0.5, 1.25, 0)
    glVertex3f(0.5, 1.25, 0.6)
    glVertex3f(0.5, 0.5, 0.6)
    glEnd()

#кабина правая сторона
    glColor4f(0.0, 1.0, 1.0, 1.0)
    glBegin(GL_QUADS)
    glVertex3f(1, 0.5, 0)
    glVertex3f(1, 1.25, 0)
    glVertex3f(1, 1.25, 0.6)
    glVertex3f(1, 0.5, 0.6)
    glEnd()

#кабина дно
    glColor4f(0.0, 1.0, 1.0, 1.0)
    glBegin(GL_QUADS)
    glVertex3f(0.5, 0.5, 0)
    glVertex3f(1, 0.5, 0)
    glVertex3f(0.5, 1.25, 0)
    glVertex3f(1, 1.25, 0)
    glEnd()

#кабина левая часть маленькая
    glColor4f(0.0, 1.0, 1.0, 1.0)
    glBegin(GL_QUADS)
    glVertex3f(0.5, 0.5, 0.6)
    glVertex3f(0.5, 0.5, 1)
    glVertex3f(0.5, 1, 1)
    glVertex3f(0.5, 1.25, 0.6)
    glEnd()

#кабина правая сторона маленькая
    glColor4f(0.0, 1.0, 1.0, 1.0)
    glBegin(GL_QUADS)
    glVertex3f(1, 0.5, 0.6)
    glVertex3f(1, 0.5, 1)
    glVertex3f(1, 1, 1)
    glVertex3f(1, 1.25, 0.6)
    glEnd()

#кабина середина 1
    glColor4f(0.0, 1.0, 1.0, 1.0)
    glBegin(GL_QUADS)
    glVertex3f(1, 1.25, 0)
    glVertex3f(0.5, 1.25, 0)
    glVertex3f(0.5, 1.25, 0.6)
    glVertex3f(1, 1.25, 0.6)
    glEnd()

#кабина середина 2
    glColor4f(0.0, 1.0, 1.0, 1.0)
    glBegin(GL_QUADS)
    glVertex3f(1, 1, 1)
    glVertex3f(0.5, 1, 1)
    glVertex3f(0.5, 1.25, 0.6)
    glVertex3f(1, 1.25, 0.6)
    glEnd()

#черная линия вдоль на левой стороне
    glLineWidth(40)
    glColor3f(0, 0, 0)
    glBegin(GL_LINES)
    glVertex3f(0.5, 0.5, 0.6)
    glVertex3f(0.5, 1.25, 0.6)
    glEnd()

#черная линия вдоль на правой стороне
    glLineWidth(40)
    glColor3f(0, 0, 0)
    glBegin(GL_LINES)
    glVertex3f(1, 0.5, 0.6)
    glVertex3f(1, 1.25, 0.6)
    glEnd()

#черная линия поперёк на левой стороне
    glLineWidth(40)
    glColor3f(0, 0, 0)
    glBegin(GL_LINES)
    glVertex3f(0.5, 1, 1)
    glVertex3f(0.5, 1, 0.6)
    glEnd()

#черная линия поперёк на правой стороне
    glLineWidth(40)
    glColor3f(0, 0, 0)
    glBegin(GL_LINES)
    glVertex3f(1, 1, 1)
    glVertex3f(1, 1, 0.6)
    glEnd()

# черная линия вдоль посередине
    glLineWidth(40)
    glColor3f(0, 0, 0)
    glBegin(GL_LINES)
    glVertex3f(0.5, 1.25, 0.6)
    glVertex3f(1, 1.25, 0.6)
    glEnd()

    #колесо 1 кузов левая сторона
    glColor4f(1.0, 1.0, 1.0, 0.0)
    glBegin(GL_QUADS)
    glVertex3f(0.5, 0.1, 0)
    glVertex3f(0.5, 0.5, 0)
    glVertex3f(0.5, 0.5, -0.3)
    glVertex3f(0.5, 0.1, -0.3)
    glEnd()

#колесо 2 кузов левая сторона
    glColor4f(1.0, 1.0, 1.0, 0.0)
    glBegin(GL_QUADS)
    glVertex3f(0.5, -0.9, 0)
    glVertex3f(0.5, -1.3, 0)
    glVertex3f(0.5, -1.3, -0.3)
    glVertex3f(0.5, -0.9, -0.3)
    glEnd()

#колесо 1 кузов правая сторона
    glColor4f(1.0, 1.0, 1.0, 0.0)
    glBegin(GL_QUADS)
    glVertex3f(0.9, 0.1, 0)
    glVertex3f(0.9, 0.5, 0)
    glVertex3f(0.9, 0.5, -0.3)
    glVertex3f(0.9, 0.1, -0.3)
    glEnd()

# колесо 2 кузов правая сторона
    glColor4f(1.0, 1.0, 1.0, 0.0)
    glBegin(GL_QUADS)
    glVertex3f(0.9, -0.9, 0)
    glVertex3f(0.9, -1.3, 0)
    glVertex3f(0.9, -1.3, -0.3)
    glVertex3f(0.9, -0.9, -0.3)
    glEnd()

#ручка дверцы на левой стороне
    glLineWidth(30)
    glColor3f(0, 0, 0)
    glBegin(GL_LINES)
    glVertex3f(0.5, 0.8, 0.4)
    glVertex3f(0.5, 0.6, 0.4)
    glEnd()

#ручка дверцы на правой стороне
    glLineWidth(30)
    glColor3f(0, 0, 0)
    glBegin(GL_LINES)
    glVertex3f(1, 0.8, 0.4)
    glVertex3f(1, 0.6, 0.4)
    glEnd()

#фара на левой стороне
    glLineWidth(50)
    glColor3f(1, 0.5, 0)
    glBegin(GL_LINES)
    glVertex3f(0.492, 1.27, 0.3)
    glVertex3f(0.492, 1, 0.3)
    glEnd()

#фара на правой стороне
    glLineWidth(50)
    glColor3f(1, 0.5, 0)
    glBegin(GL_LINES)
    glVertex3f(1.08, 1.27, 0.3)
    glVertex3f(1.08, 1, 0.3)
    glEnd()


#отображение на экране
pygame.init()
display = (1200, 900)
scree = pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

glEnable(GL_DEPTH_TEST)
glEnable(GL_LIGHTING)
glShadeModel(GL_SMOOTH)
glEnable(GL_COLOR_MATERIAL)
glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)

glEnable(GL_LIGHT0)
glLightfv(GL_LIGHT0, GL_AMBIENT, [0.5, 0.5, 0.5, 1])
glLightfv(GL_LIGHT0, GL_DIFFUSE, [1.0, 1.0, 1.0, 1])

sphere = gluNewQuadric()

glMatrixMode(GL_PROJECTION)
gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)

glMatrixMode(GL_MODELVIEW)
gluLookAt(0, -8, 0, 0, 0, 0, 0, 0, 1)
viewMatrix = glGetFloatv(GL_MODELVIEW_MATRIX)
glLoadIdentity()

# init mouse movement and center mouse on screen
displayCenter = [scree.get_size()[i] // 2 for i in range(2)]
mouseMove = [0, 0]
pygame.mouse.set_pos(displayCenter)

pygame.mouse.set_visible(False)
up_down_angle = 0.0
paused = False
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE or event.key == pygame.K_RETURN:
                run = False
            if event.key == pygame.K_PAUSE or event.key == pygame.K_p:
                paused = not paused
                pygame.mouse.set_pos(displayCenter)
        if not paused:
            if event.type == pygame.MOUSEMOTION:
                mouseMove = [event.pos[i] - displayCenter[i] for i in range(2)]
            pygame.mouse.set_pos(displayCenter)

    if not paused:
        # get keys
        keypress = pygame.key.get_pressed()
        # mouseMove = pygame.mouse.get_rel()

        # init model view matrix
        glLoadIdentity()

        # apply the look up and down
        up_down_angle += mouseMove[1] * 0.1
        glRotatef(up_down_angle, 1.0, 0.0, 0.0)

        # init the view matrix
        glPushMatrix()
        glLoadIdentity()

        # apply the movment
        if keypress[pygame.K_w]:
            glTranslatef(0, 0, 0.1)
        if keypress[pygame.K_s]:
            glTranslatef(0, 0, -0.1)
        if keypress[pygame.K_d]:
            glTranslatef(-0.1, 0, 0)
        if keypress[pygame.K_a]:
            glTranslatef(0.1, 0, 0)

        # apply the left and right rotation
        glRotatef(mouseMove[0] * 0.1, 0.0, 1.0, 0.0)

        # multiply the current matrix by the get the new view matrix and store the final vie matrix
        glMultMatrixf(viewMatrix)
        viewMatrix = glGetFloatv(GL_MODELVIEW_MATRIX)

        # apply view matrix
        glPopMatrix()
        glMultMatrixf(viewMatrix)

        glLightfv(GL_LIGHT0, GL_POSITION, [1, -1, 1, 0])

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        glPushMatrix()

        draw()

        glPopMatrix()

        pygame.display.flip()
        pygame.time.wait(10)

pygame.quit()