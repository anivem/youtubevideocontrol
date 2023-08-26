import serial
import keyboard
import pyautogui

# Replace 'COM3' with your actual COM port
ser = serial.Serial('COM3', 9600)

while True:
    try:
        data = ser.readline().decode().strip()
        
        if data == "forward":
            keyboard.press_and_release('right')  # Simulate a key press and release
        elif data == "backward":
            keyboard.press_and_release('left')   # Simulate a key press and release
        elif data == "vol+":
            keyboard.press_and_release('up')     # Simulate a key press and release
        elif data == "vol-":
            keyboard.press_and_release('down')   # Simulate a key press and release
        elif data == "vidcont":
            pyautogui.press('k')
        else:
            print("Unknown command:", data)
            
    except KeyboardInterrupt:
        break

ser.close()