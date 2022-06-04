#South Bank Racing - Raspberry Pi

This repository is used for the development of reading OBDII data over a CANBUS data system.

Firstly, the OBDII codes are sent from the ECU directly to a PiCan3, using CANBUS.

The Raspberry Pi 4 connected to the PiCan3 then reads the data in its raw format and saves it into a .log file, line by line.

This .log file is then read and converted into a .csv file with the hex values converted as required. Conversions used are:
1. Hex temperature value to decimal fahrenheit and then to decimal centigrade.

Once the .csv file is created, an external python script to graph the data is used over time domain for each variable.
