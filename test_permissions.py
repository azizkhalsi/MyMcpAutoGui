import pyautogui
import time

print("PyAutoGUI version:", pyautogui.__version__)
print("Screen size:", pyautogui.size())

print("\nTesting mouse control in 5 seconds...")
print("Watch your mouse cursor - it should move in a square pattern")
time.sleep(5)

# Get the current mouse position
start_x, start_y = pyautogui.position()
print(f"Starting position: ({start_x}, {start_y})")

try:
    # Move in a square pattern
    pyautogui.moveTo(start_x + 100, start_y, duration=1)
    print("Moved right")
    time.sleep(1)
    
    pyautogui.moveTo(start_x + 100, start_y + 100, duration=1)
    print("Moved down")
    time.sleep(1)
    
    pyautogui.moveTo(start_x, start_y + 100, duration=1)
    print("Moved left")
    time.sleep(1)
    
    pyautogui.moveTo(start_x, start_y, duration=1)
    print("Moved back to start")
    
    print("\nIf you didn't see the mouse move in a square pattern,")
    print("you need to grant accessibility and input monitoring permissions")
    print("to your Terminal/IDE in System Settings → Privacy & Security")
    
except Exception as e:
    print(f"\nError: {e}")
    print("This likely means PyAutoGUI doesn't have the required permissions") 