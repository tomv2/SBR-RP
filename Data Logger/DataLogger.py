import csv

with open('dashboard.log', 'rb') as file_in:
    with open("dashboardout.txt", "wb") as file_out:
        file_out.writelines(filter(lambda line: b'32E#01' in line, file_in))
file_in.close()
        
with open('dashboardout.txt', 'r') as f:
    with open('Dashboard_raw_log.csv', mode='w') as csv_file:
        fieldnames = ['Timestamp', 'Coolant temp', 'Engine speed', 'Oil pressure', 'Battery voltage']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for line in f:
            writer.writerow({'Timestamp': line[1]+line[2]+line[3]+line[4]+line[5]+line[6]+line[7]+line[8]+line[9]+line[10]+line[11]+line[12]+line[13]+line[14]+line[15]+line[16]+line[17],'Coolant temp': line[31]+line[32], 'Engine speed': line[33]+line[34]+line[35]+line[36], 'Oil pressure': line[37]+line[38]+line[39]+line[40], 'Battery voltage': line[41]+line[42]+line[43]+line[44]})

with open('dashboardout.txt', 'r') as f:
    with open('Dashboard_conv_log.csv', mode='w') as csv_file:
        fieldnames = ['Timestamp', 'Coolant temp', 'Engine speed', 'Oil pressure', 'Battery voltage']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for line in f:
            n = line[31]+line[32]
            n2 = line[33]+line[34]+line[35]+line[36]
            n3 = line[37]+line[38]+line[39]+line[40]
            n4 = line[41]+line[42]+line[43]+line[44]
            tempconv = (int(n, 16)-32)/1.8
            oilpressure = (int(n3, 16)*0.001)
            batteryvoltage = (int(n4, 16)*0.00030518)
            enginespeed = (int(n2, 16)) 
            writer.writerow({'Timestamp': line[1]+line[2]+line[3]+line[4]+line[5]+line[6]+line[7]+line[8]+line[9]+line[10]+line[11]+line[12]+line[13]+line[14]+line[15]+line[16]+line[17],'Coolant temp': tempconv, 'Engine speed': n2, 'Oil pressure': oilpressure, 'Battery voltage': batteryvoltage})
