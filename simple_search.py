import pyautogui
import time

# Safety settings
pyautogui.PAUSE = 1.5  # Longer pause between actions
pyautogui.FAILSAFE = True

def search_dxo():
    try:
        print("Starting automation in 3 seconds...")
        print("Current mouse position:", pyautogui.position())
        time.sleep(3)
        
        # Open Spotlight
        print("Opening Spotlight...")
        pyautogui.keyDown('command')
        time.sleep(0.5)
        pyautogui.press('space')
        time.sleep(0.5)
        pyautogui.keyUp('command')
        time.sleep(2)
        
        # Type 'safari' and open it
        print("Opening Safari...")
        pyautogui.write('safari', interval=0.25)
        time.sleep(1)
        pyautogui.press('return')
        time.sleep(3)
        
        # Focus address bar
        print("Focusing address bar...")
        pyautogui.keyDown('command')
        time.sleep(0.5)
        pyautogui.press('l')
        time.sleep(0.5)
        pyautogui.keyUp('command')
        time.sleep(1)
        
        # Go to Google
        print("Navigating to Google...")
        pyautogui.write('www.google.com', interval=0.25)
        time.sleep(1)
        pyautogui.press('return')
        time.sleep(3)
        
        # Search for DXO Labs
        print("Searching for DXO Labs...")
        pyautogui.write('dxo labs', interval=0.25)
        time.sleep(1)
        pyautogui.press('return')
        
        print("Search completed!")
        
    except Exception as e:
        print(f"Error occurred: {str(e)}")
        print(f"Mouse position when error occurred: {pyautogui.position()}")

if __name__ == "__main__":
    search_dxo() 