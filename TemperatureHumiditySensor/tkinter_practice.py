import tkinter as tk
from cages import Cage
import random

cages = {}

for i in range(4):
    for j in range(3):
        cages[f"CAGE_{i}{j}"] = Cage(f"CAGE_{i}{j}")

def main(window):
    for i in range(4):
        window.columnconfigure(i, weight=1, minsize=50)
        window.rowconfigure(i, weight=1, minsize=50)

        for j in range(3):
            frame = tk.Frame(
                master = window,
                relief = tk.FLAT,
                borderwidth = 1,
                background="#ffffff"
            )
            frame.grid(row = i, column = j, padx = 5, pady = 5)

            # Give each frame a name that matches the cage?
            frame.cage_name = f"CAGE_{i}{j}"

            label = tk.Label(master = frame,
                text = f"Row {i}\nColumn {j}",
                font = ("Futura", 15),
                background="#ffffff"
            )
            label.pack(padx=5, pady=5)
    # // Gets text from every label from each frame
    # for frame in window.children.values():
    #     for label in frame.children.values():
    #         print(label.cget("text"))


    # // Also gets text from every label from each frame, but also prints cage name
    # for frame in window.children.values():
    #     print(frame.cage_name)
    #     print(list(frame.children.values())[0].cget("text"))

    # // UPDATES LABEL TEXT WITH TEMPERATURE AND HUMIDITY FROM EACH CAGE (HOW TO UPDATE CONSTANTLY?)
    for frame in window.children.values():
        for label in frame.children.values():
            label.config(text = f"{cages[frame.cage_name].name}\nTemperature: {cages[frame.cage_name].temperature}\nHumidity: {cages[frame.cage_name].humidity}")
    # def refresh():
    #     for frame in window.children.values():
    #         for label in frame.children.values():
    #             label.config(text = f"{cages[frame.cage_name].name}\nTemperature: {random.randint(0, 10)}\nHumidity: {random.randint(10, 20)}")
    #     window.after(10000, refresh())

    # refresh()
    window.mainloop()

# def update(window):
#     for frame in window.children.values():
#         for label in frame.children.values():
#             label.config(text = f"{cages[frame.cage_name].name}\nTemperature: {random.randint(0, 10)}\nHumidity: {random.randint(10, 20)}")
#
# def refresh(window):
#     for frame in window.children.values():
#         for label in frame.children.values():
#             label.config(text = f"{cages[frame.cage_name].name}\nTemperature: {random.randint(0, 10)}\nHumidity: {random.randint(10, 20)}")
#     window.after(10000, refresh(window))

window = tk.Tk()
window.configure(bg = 'white')
window.title("Temperature/Humidity Sensor")
main(window)
