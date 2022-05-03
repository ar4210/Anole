This is a collection of scripts used for the temperature humidity sensor in the room where our lizards are housed. To use, run Temp_Hum_Sensor.py. Make sure to set a proper csv path to write to within the script.

By Aditya Rao (ar4210@columbia.edu)

## Temp_Hum_Sensor.py
This is the main code for the temperature and humidity graphical user interface. It displays temperatures and humidities for each cage, as well as the room as a whole.

## AdafruitDHT.py
This is a script taken from Adafruit's official Github repo. For use with Adafruit Temperature and Humidity Sensors.

## DigitalWatch.py
This is sample code taken from online that demonstrates how to make a simple digital clock using TKinter. I used it to learn how to update a label continuously using TKinter's after() method recursively. In Temp_Hum_Sensor.py, I use this information to update the temperatures and humidities continuously.

## cages.py
Helper code for Temp_Hum_Sensor.py. Class Cages() made to represent each cage in the lizard room, with attributes temperature and humidity that we can pull from in main GUI. In Temp_Hum_Sensor.py, a "Room" cage is also created, which represents the conditions of the room as a whole. Currently uses the random module to set random temperatures/humidities to each Cage object, but when the Raspberry Pi stuff is set up real values will be plugged in through here.

## example.csv
This is the default file that Temp_Hum_Sensor.py records to every 30 minutes, and it mainly used for testing. You can set up a different file name in Temp_Hum_Sensor.py and write to that file instead.

## fonts.py
Code found on Stack Overflow that depicts the different fonts you can use in TKinter.

## tkinter_practice.py
Script that I played around with to practice with the tk package.

## writer.py
Contains a Writer class that is used for logging temperature and humidity data to a specified csv directory.

