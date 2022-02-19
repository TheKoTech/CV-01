# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import numpy as np
import tkinter as tk
from PIL import ImageTk, Image
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from threading import Thread


# Обработка изображения
pil_image = Image.open("image2.png")
np_image = np.array(pil_image)
np_image = np_image[:, :, :3]
pil_image = Image.fromarray(np_image)

# Пункт 2 гистограммы яркости и цветов
br_list = []
red_list = []
green_list = []
blue_list = []

for i in range(len(np_image)):
    for j in range(len(np_image[i])):
        red_list.append((int(np_image[i][j][0])))
        green_list.append((int(np_image[i][j][1])))
        blue_list.append((int(np_image[i][j][2])))
        br_list.append((int(np_image[i][j][1]) + int(np_image[i][j][0]) + int(np_image[i][j][2])) / 3)

f, axs = plt.subplots(4)
axs[0].hist(br_list, 256, color=mcolors.CSS4_COLORS['grey'])
axs[1].hist(red_list, 256, color=mcolors.BASE_COLORS['r'])
axs[2].hist(green_list, 256, color=mcolors.BASE_COLORS['g'])
axs[3].hist(blue_list, 256, color=mcolors.BASE_COLORS['b'])
plt.show()
# Пункт 2 end

# Первое окно
root = tk.Tk()
win2 = root
canvas = tk.Canvas(root, width=np_image.shape[1], height=np_image.shape[0])
canvas.pack()
img = ImageTk.PhotoImage(image=pil_image)
canvas.create_image(0, 0, image=img, anchor=tk.NW)
rect = canvas.create_rectangle(0, 0, 10, 10)
canvas.move(rect, -6, -6)

# Второе окно
win1 = tk.Toplevel(root)
lbl_coord = tk.Label(win1, text="Coords: ?, ?")
lbl_rgb = tk.Label(win1, text="R: ?, G: ?, B: ?")

prev_x, prev_y = -1, -1


# 3. a) Внешняя рамка
def drawrect(x, y):
    global canvas
    canvas.move(rect, x - prev_x, y - prev_y)


#
def motion(event):
    global prev_x, prev_y
    x, y = event.x, event.y
    if (prev_x, prev_y) == (x, y):
        return
    if x > np_image.shape[0] or y > np_image.shape[1]:
        return
    lbl_coord.configure(text="Coords: {}, {}".format(x, y))
    lbl_rgb.configure(text="R: {}, G: {}, B: {}".format(np_image[y, x, 0], np_image[y, x, 1], np_image[y, x, 2]))
    drawrect(x, y)
    prev_x, prev_y = x, y


lbl_coord.pack()
lbl_rgb.pack()

canvas.bind('<Motion>', motion)

root.mainloop()
