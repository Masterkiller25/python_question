import math
from tkinter import *

root = Tk()
root.geometry('500x500')
root.title("Simulateur")
root['bg'] = 'black'
root.resizable(height=False, width=False)


def detect_collision(line_coords, canvas):#si touche vrai
    x1, y1, x2, y2 = line_coords
    overlapping_items = canvas.find_overlapping(x1, y1, x2, y2)

    # Filtrer les objets bleus parmi les éléments superposés
    blue_objects = [item for item in overlapping_items if canvas.itemcget(item, "fill") == "blue"]

    return len(blue_objects) > 0


def start_line(event):
    global start_x, start_y
    start_x, start_y = event.x, event.y


def draw_line(event):
    global start_x, start_y
    line = canva.create_line(start_x, start_y, event.x, event.y, fill="blue", width=2)
    start_x, start_y = event.x, event.y


def create_box(canvas):
    canvas.create_rectangle(249, 249, 251, 251, fill='white')
    canvas.bind("<Button-1>", start_line)
    canvas.bind("<B1-Motion>", draw_line)


def this_line_isonbox(canvas, x, y, i):
    for idx in range(500):
        if detect_collision((x, y, idx * math.cos(math.radians(i))+x, idx * math.sin(math.radians(i))+y), canvas):
            return idx

    return 500


def create_proje(x, y, canvas):
    for i in range(360):
        coe = this_line_isonbox(canvas, x, y, i)
        print(coe)
        canvas.create_line(x, y, coe * math.cos(math.radians(i))+x, coe * math.sin(math.radians(i))+y, fill="white", width=1)


def keydown(e):
    global key
    key = e.keycode
    print(e)


start_x, start_y, key = None, None, None

canva = Canvas(root, width=500, height=500)
canva['bg'] = "black"
canva.place(x='0', y='0')
# canva.create_line(50, 50, 450, 450, fill="white", width=2)

create_box(canva)

frame = Frame(root, width=0, height=0)
frame.bind("<KeyPress>", keydown)
frame.pack()
frame.focus_set()

while True:
    while key == 32:
        print("espace")
        create_proje(250, 250, canva)
        key = 0

    if key == 13:
        break

    root.update()
