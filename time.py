import schedule 
import time 

def func(): 
	print("Geeksforgeeks") 

schedule.every(0.2).minutes.do(func) 

while True: 
	schedule.run_pending() 
	time.sleep(1) 




#####Working code 

# pip install pyserial
import serial.tools.list_ports 
import schedule 
import time 


ports = serial.tools.list_ports.comports()
serialInst = serial.Serial()
portsList = []

for one in ports: 
    portsList.append(str(one))
    print(str(one))

com = input("Select Com Port for Arduino #: ")

for i in range(len(portsList)):
    if portsList[i].startswith("COM" + str(com)):
        use = "COM" + str(com)
        print(use)

serialInst.baudrate = 9600
serialInst.port = use 
print (serialInst.port)
serialInst.open()

while True:
    command = input("Arduino Command (ON/OFF/exit): ")
    ##opens coms and sends signals to arudino code. Make it so only opens coms at certain times of the daay??? 
    serialInst.write(command.encode('utf-8'))

    #cc=str(serialInst.readline())
    #print (cc)
    if command == 'exit':
        exit() 
 

 ######Working code_2 

 # pip install pyserial
import serial.tools.list_ports 
import schedule 
import time 
 

ports = serial.tools.list_ports.comports()
serialInst = serial.Serial()
portsList = []

for one in ports:
    portsList.append(str(one))
    print(str(one))

# Instead of asking the user for input, directly set the COM port
use = "COM5"  # Always use COM5

# Check if COM5 exists in the list of available ports
if use in portsList:
    print(f"Using port {use}")
else:
    print(f"Port {use} not found.") 

serialInst.baudrate = 9600
serialInst.port = use
print (serialInst.port)
serialInst.open()

while True: 
    #Make so signal sent at certain time of day or something idk 
    
    command = input("Arduino Command (ON/OFF/exit): ")
    
    serialInst.write(command.encode('utf-8'))

    #5
    # cc=str(serialInst.readline())
    #print (cc)
    if command == 'exit':
        exit() 