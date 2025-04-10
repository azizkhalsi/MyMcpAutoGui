import pyautogui
import time
import sys

# Set a pause between actions to make them visible and prevent errors
pyautogui.PAUSE = 2.0  # 2 second pause between actions
pyautogui.FAILSAFE = True  # Move mouse to upper-left corner to abort

def open_safari_and_search():
    try:
        print("Current mouse position:", pyautogui.position())
        print("Screen size:", pyautogui.size())
        
        # First method: Try using Command + Tab to ensure we're on the desktop
        print("Pressing Command+Tab to ensure we're on desktop...")
        pyautogui.keyDown('command')
        time.sleep(0.5)
        pyautogui.press('tab')
        time.sleep(0.5)
        pyautogui.keyUp('command')
        time.sleep(1)
        
        # Now press Command + Space for Spotlight
        print("Opening Spotlight with Command+Space...")
        pyautogui.keyDown('command')
        time.sleep(0.5)
        pyautogui.press('space')
        time.sleep(0.5)
        pyautogui.keyUp('command')
        time.sleep(2)  # Wait for Spotlight
        
        # Type 'safari' slowly
        print("Typing 'safari'...")
        pyautogui.write('safari', interval=0.25)  # Type slower
        time.sleep(2)
        
        print("Pressing Enter to launch Safari...")
        pyautogui.press('enter')
        time.sleep(5)  # Give Safari time to open
        
        # Press Command + L to focus address bar
        print("Focusing address bar with Command+L...")
        pyautogui.keyDown('command')
        time.sleep(0.5)
        pyautogui.press('l')
        time.sleep(0.5)
        pyautogui.keyUp('command')
        time.sleep(1)
        
        # Type Google URL
        print("Typing Google URL...")
        pyautogui.write('www.google.com', interval=0.25)
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(5)  # Wait for Google to load
        
        # Get screen dimensions for center calculation
        screen_width, screen_height = pyautogui.size()
        center_x = screen_width // 2
        center_y = (screen_height // 3)  # Approximately where Google search box is
        
        # Move to the center (Google search box)
        print(f"Moving mouse to center ({center_x}, {center_y})...")
        pyautogui.moveTo(center_x, center_y, duration=1)
        time.sleep(1)
        
        print("Clicking search box...")
        pyautogui.click()
        time.sleep(1)
        
        # Type search query
        print("Typing search query...")
        pyautogui.write('dxo labs france', interval=0.25)
        time.sleep(1)
        
        print("Pressing Enter to search...")
        pyautogui.press('enter')
        
    except Exception as e:
        print(f"\nError occurred: {str(e)}")
        print(f"Mouse position when error occurred: {pyautogui.position()}")
        sys.exit(1)

if __name__ == "__main__":
    print("PyAutoGUI version:", pyautogui.__version__)
    print("\nStarting automation in 5 seconds...")
    print("Move mouse to upper-left corner to abort!")
    print("Please don't move your mouse or use keyboard during the automation...")
    
    # Countdown
    for i in range(5, 0, -1):
        print(f"{i}...")
        time.sleep(1)
    
    open_safari_and_search()
    print("\nSearch completed!") 