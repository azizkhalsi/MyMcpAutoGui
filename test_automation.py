import pyautogui
import time

# Safety settings
pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True

def test_automation():
    print("Starting test in 3 seconds...")
    time.sleep(3)
    
    # Get current position
    current_pos = pyautogui.position()
    print(f"Current mouse position: {current_pos}")
    
    # Move mouse in a small square
    print("Moving mouse in a square pattern...")
    pyautogui.moveTo(100, 100, duration=1)
    pyautogui.moveTo(200, 100, duration=1)
    pyautogui.moveTo(200, 200, duration=1)
    pyautogui.moveTo(100, 200, duration=1)
    pyautogui.moveTo(100, 100, duration=1)
    
    print("Test completed!")

if __name__ == "__main__":
    test_automation() 