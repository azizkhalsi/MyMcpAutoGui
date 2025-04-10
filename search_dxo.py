import pyautogui
import time

# Safety settings
pyautogui.PAUSE = 1.5  # Slightly longer pause for reliability
pyautogui.FAILSAFE = True

def search_dxo():
    print("Starting search automation in 3 seconds...")
    time.sleep(3)
    
    # Open Spotlight
    print("Opening Spotlight...")
    pyautogui.hotkey('command', 'space')
    time.sleep(1)
    
    # Type 'safari' and open it
    print("Opening Safari...")
    pyautogui.write('safari', interval=0.1)
    time.sleep(1)
    pyautogui.press('return')
    time.sleep(3)  # Wait for Safari to open
    
    # Focus address bar
    print("Focusing address bar...")
    pyautogui.hotkey('command', 'l')
    time.sleep(1)
    
    # Go to Google
    print("Navigating to Google...")
    pyautogui.write('www.google.com', interval=0.1)
    pyautogui.press('return')
    time.sleep(3)  # Wait for Google to load
    
    # Search for DXO Labs
    print("Searching for DXO Labs...")
    pyautogui.write('dxo labs', interval=0.1)
    pyautogui.press('return')
    
    print("Search completed!")

if __name__ == "__main__":
    search_dxo() 