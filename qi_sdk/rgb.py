import qi
import cv2
import numpy as np
from functions import * 
import sys
import time
import subprocess
# Connect to Pepper robot
import os 
os.system('cmd /c "netsh wlan connect name=pepper2"' )


time.sleep(4)

port = 9559
ip = "192.168.0.101"
session = connect(ip,port)
move_head(session)




# get_depth_image(session=session)
# sys.exit()
# Get the ALVideoDevice service
video_service = session.service("ALVideoDevice")

time.sleep(2)

# Set the camera parameters
camera_name = "CameraTop"  # Choose the camera name ("CameraTop" or "CameraBottom")
resolution = 2  # Set the resolution (0: 160x120, 1: 320x240, 2: 640x480, 3: 1280x960)
color_space = 11  # Set the color space (11: RGB)

# Subscribe to the camera



a = video_service.subscribeCamera("S121", 0, resolution, color_space, 30)

# Capture an image
print(a,352 )
image = video_service.getImageRemote(a)



if image is not None:
    print("image success")
    # Get the image data
    width, height = image[0], image[1]
    image_data = np.frombuffer(image[6], dtype=np.uint8).reshape((height, width, 3))
    cv2.imwrite( r"C:\Users\Rania\Desktop\Graduation Project (ALL)\GP2\qi_sdk\classify1.jpg",image_data)
   
    # Display the image
  

else:
    print("Failed to capture the image.")


# prediciton code 
import os
os.system('cmd /c "netsh wlan connect name=PSUT-Students"' )
# Run a terminal command
time.sleep(5)
os.system("C:/Users/Rania/AppData/Local/Programs/Python/Python311/python.exe \"C:\Users\Rania\Desktop\Graduation Project (ALL)\GP2\qi_sdk\predict.py\"")

# result = subprocess.run(command, shell=True, capture_output=True, text=True)


# # Check the result
# if result.returncode == 0:
#     output = result.stdout
#     print("Command output:")
#     print(output)
#     cv2.imshow("prediction.jpg", image_data)
#     cv2.waitKey(0)
# else:
#     error = result.stderr
#     print("Command execution failed:")
#     print(error)



# Unsubscribe from the camera
# video_service.unsubscribe("rgb_image")

# # Disconnect from Pepper
# session.close()
