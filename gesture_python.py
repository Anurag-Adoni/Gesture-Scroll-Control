import serial
import pyautogui 
import time

ser = serial.Serial('COM6', baudrate = 9600, timeout=1)


while True: 
    arduino_data = ser.readline()
    #print("gesture detected : ", arduino_data)
    buffer_d = []
    buffer_u = []
    gesture_raw = arduino_data.decode()
    gesture = gesture_raw.rstrip()
    gesture = str(gesture)
    
    if (gesture == "d"):
        print('it worked d')
        pyautogui.keyDown('pagedown')
        

    elif (gesture == "u"):
        print('it worked u')
        pyautogui.keyDown('pageup')
        
        
        

    elif (gesture == "r"):
        print('it worked r')

    elif (gesture == "l"):
        print('it worked l')


    

 

        

    
    
    

    

    

    

    
