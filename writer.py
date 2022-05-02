# Logging

import datetime
import csv

class Writer():
    def __init__(self, file_path, cages):
        self.file_path = file_path
        self.header = [cage.name for cage in cages]
        # self.header.insert(0,"Room")
        self.header.insert(0,"Date")
        self.header.insert(1,"Time")
        # print(self.header)
        with open(self.file_path, 'a') as nf: #nf = new file
            writer = csv.writer(nf, delimiter = ",")
            writer.writerow(self.header)

    def append(self, data):
        # print(data)
        with open(self.file_path, 'a') as f:
            writer = csv.writer(f, delimiter = ",")
            writer.writerow(data)
