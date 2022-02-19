# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# Press the green button in the gutter to run the script.
# Press Ctrl+F8 to toggle the breakpoint.

import numpy as np
import tkinter as tk
from PIL import ImageTk, Image


pil_image = Image.open("image.png")
np_image = np.array(pil_image)
#np_image = np_image[:, :, :3]
print(np_image.shape)
pil_image = Image.fromarray(np_image)

root = tk.Tk()
win2 = root
canvas = tk.Canvas(root, width=np_image.shape[0], height=np_image.shape[1])
canvas.pack()
img = ImageTk.PhotoImage(image=pil_image)
canvas.create_image(0, 0, image=img, anchor=tk.NW)

win1 = tk.Toplevel(root)
lbl_coord = tk.Label(win1, text="Coords: ?, ?")

def motion(event):
    x, y = event.x, event.y
    print(x, y)
    lbl_coord.configure(text="{}, {}".format(x, y))

lbl_coord.pack()

canvas.bind('<Motion>', motion)

root.mainloop()
