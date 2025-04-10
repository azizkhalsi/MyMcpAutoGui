import pyautogui
import time

def wait_for_permission():
    """Give user time to approve and return to proper window"""
    print("You have 5 seconds to approve and return to the main screen...")
    for i in range(5, 0, -1):
        print(f"{i}...")
        time.sleep(1)

def search_with_recovery():
    # Initial setup
    pyautogui.PAUSE = 1.5
    pyautogui.FAILSAFE = True
    
    # Print initial position for debugging
    print("Initial mouse position:", pyautogui.position())
    
    # Wait for user to approve and return
    wait_for_permission()
    
    try:
        # Ensure we're on the desktop (Command+F1 or similar)
        pyautogui.keyDown('command')
        pyautogui.press('f1')  # Or another key that brings you to desktop
        pyautogui.keyUp('command')
        time.sleep(1)
        
        # Now proceed with the search sequence
        # Open Spotlight
        pyautogui.keyDown('command')
        pyautogui.press('space')
        pyautogui.keyUp('command')
        time.sleep(2)
        
        # Type 'safari' and open it
        pyautogui.write('safari', interval=0.25)
        pyautogui.press('return')
        time.sleep(3)
        
        # Focus address bar
        pyautogui.keyDown('command')
        pyautogui.press('l')
        pyautogui.keyUp('command')
        time.sleep(1)
        
        # Go to Google
        pyautogui.write('www.google.com', interval=0.25)
        pyautogui.press('return')
        time.sleep(3)
        
        # Search for DXO Labs
        pyautogui.write('dxo labs', interval=0.25)
        pyautogui.press('return')
        
        print("Search completed successfully!")
        
    except Exception as e:
        print(f"Error occurred: {str(e)}")
        print(f"Mouse position when error occurred: {pyautogui.position()}")

if __name__ == "__main__":
    search_with_recovery() 