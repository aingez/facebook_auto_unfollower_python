import pyautogui
import time

# Constants for screen center coordinates
SCREEN_CENTER_X = 960
SCREEN_CENTER_Y = 540

def locate_image(image_path):
    return pyautogui.locateOnScreen(image_path)

def handle_sign(image_path):
    location = locate_image(image_path)
    if location:
        print(f"{image_path} found")
        banner_delay()
        pyautogui.click(location)
        return True
    return False

def banner_delay():
    # Sleep 100 ms to wait for the banner to disappear
    time.sleep(0.1)

def scroll():
    # Scroll up
    pyautogui.moveTo(SCREEN_CENTER_X, SCREEN_CENTER_Y)
    pyautogui.scroll(-1000)

# Main function
def main():
    status = True
    scroll_count = 0

    while status:
        follow_found = handle_sign("following_sign.png")
        like_found = handle_sign("liked_sign.png")

        if not follow_found and not like_found:
            if scroll_count > 10:
                status = False
                print("No sign found, stopping.")
                break
            print("No sign found")
            scroll_count += 1
            scroll()
            banner_delay()
            banner_delay()

if __name__ == "__main__":
    main()
