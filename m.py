import pyautogui
import random
import time

def move_mouse_and_press_key():
    print("Waiting for 5 seconds before starting random movement...")
    time.sleep(5)  # Wait 5 seconds

    # Get the initial mouse position after the delay
    initial_position = pyautogui.position()
    print("Starting random cursor movement. Move the mouse to stop.")

    while True:
        # Check if the mouse has been moved by the user
        current_position = pyautogui.position()
        if current_position != initial_position:
            print("User moved the mouse. Stopping the program.")
            break

        # Generate a random position on the screen
        screen_width, screen_height = pyautogui.size()
        random_x = random.randint(0, screen_width)
        random_y = random.randint(0, screen_height)

        # Move the mouse to the random position
        pyautogui.moveTo(random_x, random_y, duration=0.5)
        
        # Simulate a harmless keypress (e.g., Shift key)
        pyautogui.press("shift")

        # Update initial_position for the next loop iteration
        initial_position = pyautogui.position()

        # Pause briefly before the next random movement
        time.sleep(1)

# Run the function
move_mouse_and_press_key()
