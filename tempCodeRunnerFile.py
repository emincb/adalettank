def game():
    while True:
        # Capture the region of the screen where the radar is located
        radar_image = pyautogui.screenshot(region=(1492,172,183,134))
        radar_location = (1492,172,183,134)  # Assign the tuple to radar_location
        if radar_location:
            # Convert the PIL.Image object to a numpy array
            radar_image = np.array(radar_image)

            # Ensure radar_image is a grayscale image
            if len(radar_image.shape) == 3:  # If the image is a color image
                radar_image = cv2.cvtColor(radar_image, cv2.COLOR_BGR2GRAY)

            # Save the radar image for debugging
            cv2.imwrite('debug_radar_image.png', radar_image)

            # Load the template image in grayscale
            template = cv2.imread('blue_circle.png', 0)

            # Now you can use matchTemplate
            blue_circle_corr = cv2.matchTemplate(radar_image, template, cv2.TM_CCOEFF_NORMED)
            _, _, _, blue_circle_location = cv2.minMaxLoc(blue_circle_corr)

            if blue_circle_location is not None:
                print("Blue circle found.")
            else:
                print("Blue circle not found.")

            # List of shapes to match
            shapes = ['circle.png', 'triangle.png', 'square.png']

            for shape in shapes:
                # Detect the shape in the radar image
                shape_image = cv2.imread(shape, 0)
                shape_corr = cv2.matchTemplate(radar_image, shape_image, cv2.TM_CCOEFF_NORMED)
                _, _, _, shape_location = cv2.minMaxLoc(shape_corr)

                if shape_location is not None:
                    print(f"{shape} found.")

                    # Save the shape image for debugging
                    cv2.imwrite(f'debug_{shape}', shape_image)

                    # Calculate the coordinates of the center of the blue circle and the shape
                    blue_circle_center = (blue_circle_location[0] + template.shape[1] // 2, blue_circle_location[1] + template.shape[0] // 2)
                    shape_center = (shape_location[0] + shape_image.shape[1] // 2, shape_location[1] + shape_image.shape[0] // 2)

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