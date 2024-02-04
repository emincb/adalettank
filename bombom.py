import pyautogui
import pygetwindow as gw
import threading
import time
import os
def calculate_angle(point1, point2):
    # Calculate the slope of the line between point1 and point2
    slope = (point2[1] - point1[1]) / (point2[0] - point1[0])

    # Calculate the angle in radians between the line and the x-axis
    angle_radians = math.atan(slope)

    # Convert the angle to degrees
    angle_degrees = math.degrees(angle_radians)

    return abs(angle_degrees)

def click_until_found(image):
    # Join the directory path with the image file name
    image_path = os.path.join('C:\\Users\\eminb\\Desktop\\adalettank', image)

    while True:
        try:
            # Locate the image on the screen with high precision
            location = pyautogui.locateCenterOnScreen(image_path, confidence=0.7)
            if location:
                break
            else:
                print(f"Could not find {image} on the screen, clicking 'kaydir.png'...")
                locate_and_click('kaydir.png')
                time.sleep(1)  # Wait for a second before retrying to avoid excessive CPU usage
        except pyautogui.ImageNotFoundException:
            print(f"Could not find {image} on the screen, clicking 'kaydir.png'...")
            locate_and_click('kaydir.png')
            time.sleep(1)  # Wait for a second before retrying to avoid excessive CPU usage

def locate_and_move(image):
    # Join the directory path with the image file name
    image_path = os.path.join('C:\\Users\\eminb\\Desktop\\adalettank', image)

    while True:
        try:
            # Locate the image on the screen with 70% confidence
            location = pyautogui.locateCenterOnScreen(image_path, confidence=0.7)
            if location:
                # Move the mouse cursor to the image
                pyautogui.moveTo(location)
                break
            else:
                print(f"Could not find {image} on the screen, retrying...")
                time.sleep(1)  # Wait for a second before retrying to avoid excessive CPU usage
        except pyautogui.ImageNotFoundException:
            print(f"Could not find {image} on the screen, retrying...")
            time.sleep(1)  # Wait for a second before retrying to avoid excessive CPU usage
def locate_and_click(image):
    # Join the directory path with the image file name
    image_path = os.path.join('C:\\Users\\eminb\\Desktop\\adalettank', image)

    while True:
        try:
            # Locate the image on the screen with 70% confidence
            location = pyautogui.locateCenterOnScreen(image_path, confidence=0.7)
            if location:
                # Move the mouse cursor to the image and click
                pyautogui.moveTo(location)
                pyautogui.click()
                break
            else:
                print(f"Could not find {image} on the screen, retrying...")
                time.sleep(1)  # Wait for a second before retrying to avoid excessive CPU usage
        except pyautogui.ImageNotFoundException:
            print(f"Could not find {image} on the screen, retrying...")
            time.sleep(1)  # Wait for a second before retrying to avoid excessive CPU usage
def locate_image(image):
    # Join the directory path with the image file name
    image_path = os.path.join('C:\\Users\\eminb\\Desktop\\adalettank', image)

    while True:
        try:
            # Locate the image on the screen with 70% confidence
            location = pyautogui.locateCenterOnScreen(image_path, confidence=0.7)
            if location:
                print(f"Found {image} on the screen.")
                return location
            else:
                print(f"Could not find {image} on the screen, retrying...")
                time.sleep(1)  # Wait for a second before retrying to avoid excessive CPU usage
        except pyautogui.ImageNotFoundException:
            print(f"Could not find {image} on the screen, retrying...")
            time.sleep(1)  # Wait for a second before retrying to avoid excessive CPU usage       
def locate_image_region(image):
    # Join the directory path with the image file name
    image_path = os.path.join('C:\\Users\\eminb\\Desktop\\adalettank', image)

    while True:
        try:
            # Locate the image on the screen with 70% confidence
            location = pyautogui.locateOnScreen(image_path, confidence=0.7)
            if location:
                print(f"Found {image} on the screen.")
                return location
            else:
                print(f"Could not find {image} on the screen, retrying...")
                time.sleep(1)  # Wait for a second before retrying to avoid excessive CPU usage
        except pyautogui.ImageNotFoundException:
            print(f"Could not find {image} on the screen, retrying...")
            time.sleep(1)  # Wait for a second before retrying to avoid excessive CPU usage

def startup():
    try:
        # Locate 'ikon.png' on the screen
        locate_and_click('ikon.png')

        # Rest of your code...

        # Locate and click on the images
        images = ['kesif.png', 'oda.png', 'odabilgi.png']
        for image in images:
            locate_and_click(image)

        # Locate 'surukleme.png' and move the mouse cursor to that position
        locate_and_move('surukleme.png')

        click_until_found('sirk.png')

        # Locate and click on 'sirk.png' and 'tamam.png'
        locate_and_click('sirk.png')
        locate_and_click('tamam.png')

        # Locate and click on 'basla.png'
        locate_and_click('basla.png')
    except FileNotFoundError:
        print("Could not find one or more image files in the specified directory.")

def game():
    while True:
        # Detect the 'radar.png' image on the screen
        radar_location = locate_image_region('radar.png')
        
        if radar_location:
            # Convert the Box object to a tuple
            radar_location = (radar_location.left, radar_location.top, radar_location.width, radar_location.height)
            
            # Capture the region of the screen where the radar is located
            radar_image = pyautogui.screenshot(region=radar_location)

            # Convert the radar image to a format that can be used with OpenCV
            radar_image = cv2.cvtColor(np.array(radar_image), cv2.COLOR_RGB2BGR)

            # Detect the blue circle in the radar image
            blue_circle_location = cv2.matchTemplate(radar_image, cv2.imread('blue_circle.png', 0), cv2.TM_CCOEFF_NORMED)

            if blue_circle_location is not None:
                print("Blue circle found.")
            else:
                print("Blue circle not found.")

            # Convert the radar image to grayscale
            radar_image_gray = cv2.cvtColor(radar_image, cv2.COLOR_BGR2GRAY)

            # List of shapes to match
            shapes = ['circle.png', 'triangle.png', 'square.png']

            for shape in shapes:
                # Detect the shape in the radar image
                shape_location = cv2.matchTemplate(radar_image_gray, cv2.imread(shape, 0), cv2.TM_CCOEFF_NORMED)

                if shape_location is not None:
                    print(f"{shape} found.")

                    # Calculate the coordinates of the center of the blue circle and the shape
                    blue_circle_center = (blue_circle_location[0] + blue_circle_location[2] // 2, blue_circle_location[1] + blue_circle_location[3] // 2)
                    shape_center = (shape_location[0] + shape_location[2] // 2, shape_location[1] + shape_location[3] // 2)

                    # Calculate the angle between the line connecting the blue circle and the shape and the x-axis
                    angle = calculate_angle(blue_circle_center, shape_center)
                    print(f"The angle between the blue circle and {shape} is {angle} degrees")
                else:
                    print(f"{shape} not found.")
            # Check if 'battle_end.png' is found
            battle_end_location = locate_image('battle_end.png')
            if battle_end_location is not None:
                print("Battle ended.")
                break
def energy():
    # Locate and click on 'backpack.png' and 'accesory.png'
    images = ['backpack.png', 'accesory.png']
    for image in images:
        locate_and_click(image)

    # If 'fullenergy.png' is not found, click on 'energypacket.png' and 'useenergy.png'
    if not pyautogui.locateOnScreen('fullenergy.png', confidence=0.7):
        locate_and_click('energypacket.png')
        locate_and_click('useenergy.png')

def check_for_waiter():
    while True:
        try:
            locate_and_click('adalettankwaiter.png')
        except FileNotFoundError:
            print("Could not find adalettankwaiter.png in the specified directory.")
            break

        time.sleep(1)  # Wait for a second before checking again to avoid excessive CPU usage

if __name__ == "__main__":
    # Start the waiter checking thread
    waiter_thread = threading.Thread(target=check_for_waiter)
    waiter_thread.start()

    # Run the main program
    startup()
    game()
    energy()