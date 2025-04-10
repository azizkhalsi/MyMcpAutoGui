import pyautogui
import time
import pygetwindow as gw

# Safety settings
pyautogui.PAUSE = 1.5
pyautogui.FAILSAFE = True

def get_screen_info():
    """Get information about the screen setup"""
    width, height = pyautogui.size()
    print(f"Screen size: {width}x{height}")
    print(f"Current mouse position: {pyautogui.position()}")
    return width, height

def focus_or_launch_safari():
    """Focus Safari if it's open, or launch it if it's not"""
    safari_windows = gw.getWindowsWithTitle('Safari')
    
    if safari_windows:
        safari = safari_windows[0]
        safari.activate()
        time.sleep(1)
        return True
    
    # If Safari isn't open, launch it via Spotlight
    print("Opening Safari via Spotlight...")
    pyautogui.hotkey('command', 'space')
    time.sleep(1)
    pyautogui.write('safari', interval=0.1)
    time.sleep(1)
    pyautogui.press('return')
    time.sleep(3)  # Wait for Safari to open
    return True

def search_dxo():
    """Perform the DXO Labs search"""
    try:
        # Get screen information
        width, height = get_screen_info()
        
        # Launch or focus Safari
        if not focus_or_launch_safari():
            print("Failed to launch Safari")
            return
        
        # Focus address bar
        print("Focusing address bar...")
        pyautogui.hotkey('command', 'l')
        time.sleep(1)
        
        # Navigate to Google
        print("Navigating to Google...")
        pyautogui.write('www.google.com', interval=0.1)
        pyautogui.press('return')
        time.sleep(3)
        
        # Search for DXO Labs
        print("Searching for DXO Labs...")
        pyautogui.write('dxo labs', interval=0.1)
        pyautogui.press('return')
        
        print("Search completed!")
        
    except Exception as e:
        print(f"Error occurred: {str(e)}")
        print(f"Mouse position when error occurred: {pyautogui.position()}")

if __name__ == "__main__":
    print("Starting automation in 3 seconds...")
    print("Move mouse to upper-left corner to abort!")
    time.sleep(3)
    search_dxo() 