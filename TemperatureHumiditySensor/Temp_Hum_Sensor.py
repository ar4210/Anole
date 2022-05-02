import tkinter as tk
from cages import Cage # Custom
from writer import Writer # Custom
import random
from datetime import datetime
import threading


class TempHumSensor(tk.Tk):
    def __init__(self):
        # initializes Tkinter parent class
        super().__init__()

        # For logging temperature/humidity data later
        self.file_path = "example.csv" # Engram file should go here
        # cages dict
        self.cages = {}

        # root window
        self.title("Temperature Humidity Sensor")
        self.configure(bg = 'white')

        for i in range(3):
            # These two lines make it so the labels will move with the window edges
            self.columnconfigure(i, weight=1, minsize=0)
            self.rowconfigure(i, weight=1, minsize=0)
            for j in range(4):
                label = tk.Label(master = self,
                    # Initialize labels. Text will change to actual values upon opening
                    text = f"Row {i}\nColumn {j}",
                    font = ("Lao MN", 30),
                    background="#ffffff",
                )
                label.grid(row = i, column = j, padx = 70, pady = 10)
                label.cage_name = f"CAGE_{len(self.cages) + 1}"
                self.cages[label] = Cage(label.cage_name)

        room = tk.Label(master = self,
            text = "Room",
            font = ("Lao MN", 30),
            background="#ffffff",
        )
        room.grid(row = 3, columnspan = 4, pady = 10)

        room.cage_name = "Room"
        self.cages[room] = Cage(room.cage_name)

        # Initialize logger AFTER cages so csv header can use the cages dict
        self.writer = Writer(self.file_path, self.cages.values())

        # Begin infinite update
        self.update()

    def update(self):
        '''
        Checks if time is on the hour or 30 min past the hour, and if True, log
            temperature and humidity to csv file designated by self.file_path

        Continuously updates GUI. Change frequency by changing parameter for
            self.after(milliseconds).
        '''
        self.log()
        self.update_labels()
        self.after(1000, self.update)

    def log(self):
        data = []
        # Every 30 minutes, i.e. 12:00:00 PM and 12:30:00 PM, etc.
        if datetime.now().minute == 0 or datetime.now().minute == 30:
            if datetime.now().second == 0:
                data.append(datetime.now().strftime('%m/%d/%Y'))
                data.append(datetime.now().strftime('%H:%M:%S'))
                for cage in self.cages.values():
                    data.append(f"{cage.temperature}*/{cage.humidity}")
                # Open up a new thread for logging so the TKinter GUI doesn't freeze
                threading.Thread(target = self.writer.append(data)).start()

    def update_labels(self):
        for k, v in self.cages.items(): # k = label, v = cage
            # TODO:Replace random nums with temperature and humidities from cage objects (values)
            k.config(text = f"{self.cages[k].name}\nTemp (F): {random.randint(10, 20)}\nHum (%): {random.randint(10, 20)}")

if __name__ == "__main__":
    ths = TempHumSensor()
    ths.mainloop()
