# pip install pyserial
import serial.tools.list_ports
import schedule
import time

ports = serial.tools.list_ports.comports()
serialInst = serial.Serial()
portsList = []





def run_model(): 

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
    print(serialInst.port)
    serialInst.open()

    # Function to send "ON" command
    def send_on_command():
        command = "ON"
        serialInst.write(command.encode('utf-8'))
        print(f"Sent command: {command}")

    # Schedule the "ON" command every 5 seconds (or adjust the interval as needed)
    schedule.every(1).seconds.do(send_on_command) ###set as an input from another file lol 

    # Loop to keep the program running and send the command
    while True:
        schedule.run_pending()  # Runs any scheduled tasks
        time.sleep(1)  # Sleep for a short period to avoid maxing out the CPU
