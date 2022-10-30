import glfw
from OpenGL.GL import *

#Флаг Ямайки

if glfw.init():
    pass
else:
    raise Exception("Ошибка библиотеки")

#Создание окна
window = glfw.create_window(1100, 700, "Jamaica", None, None)
if not window:
    glfw.terminate()
    raise Exception("Ошибка окна")

#Установка характеристик окна
glfw.set_window_pos(window, 400, 200)
glfw.make_context_current(window)#установить контекст
glClearColor(255, 25, 255, 0)#цвет фона

#цикл работы окна
while not glfw.window_should_close(window):
    glfw.poll_events()
    glClear(GL_COLOR_BUFFER_BIT)#очистка буфера кадра и буфера глубины

    #первый черный треугольник слева
    glColor3f(0, 0, 0)
    glBegin(GL_TRIANGLES)  # 0.5 в высоту и 0.5 в ширину
    glVertex2f(-1, 1)
    glVertex2f(0, 0)
    glVertex2f(-1, -1)
    glEnd()

    #второй черный треугольник справа
    glColor3f(0, 0, 0)
    glBegin(GL_TRIANGLES)
    glVertex2f(1, 1)
    glVertex2f(0, 0)
    glVertex2f(1, -1)
    glEnd()

    #первый зелёный треугольник сверху
    glColor3f(0, 100, 0)
    glBegin(GL_TRIANGLES)
    glVertex2f(-1, 1)
    glVertex2f(0, 0)
    glVertex2f(1, 1)
    glEnd()

    #второй зелёный треугольник снизу
    glColor3f(0, 100, 0)
    glBegin(GL_TRIANGLES)
    glVertex2f(-1, -1)
    glVertex2f(0, 0)
    glVertex2f(1, -1)
    glEnd()

    #рисую две линии крест-накрест
    glLineWidth(55)#установка ширины линии
    glColor3f(255, 255, 0)#желтый цвет для линий
    glBegin(GL_LINES)
    glVertex2f(-1, 1)
    glVertex2f(1, -1)
    glVertex2f(-1, -1)
    glVertex2f(1, 1)
    glEnd()

    glfw.swap_buffers(window)#вывести содержимое на экран

#Уничтожение окна
glfw.terminate()

