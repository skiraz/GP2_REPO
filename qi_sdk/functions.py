import qi 
from naoqi import ALProxy 
import vision_definitions
import numpy as np
import cv2
import time 
import subprocess

# Execute the file and capture the output



def standup(session):
    motion_service = session.service("ALMotion")
    posture_service = session.service("ALRobotPosture")
    posture_service.goToPosture("StandInit",0.5)
    # motion_service.rest()
    # motion_service.wakeUp()
    return 


def move_head(session):
    mot = session.service("ALMotion")
    mot.setStiffnesses("Head",1)
    names = "HeadPitch"
    angle = 0.7
    f = 0.1

    mot.setAngles(names,angle,f)



def get_depth_image(session):
    camera_service = session.service("ALVideoDevice")

    # Set the camera parameters
    resolution = 1 # 320x240
    color_space =0 # RGB
    fps = 10

    # Start the camera
    camera_id = camera_service.subscribeCamera("python_client", 2, resolution, color_space, fps)
    # Capture an image
    image = camera_service.getImageRemote(camera_id)
    # print(image)

    # Convert the image data to a Numpy array
    image_width = image[0]
    image_height = image[1]
    # print(image[6])
    image_array = np.frombuffer(image[6], dtype=np.uint8).reshape((image_height, image_width, 1))

    # Save the image to a file on your laptop
    filename = "pepper_image.jpg"
    cv2.imwrite(filename, image_array)

    # Stop the camera
    camera_service.unsubscribe(camera_id)


def connect(ip,port):
    session = qi.Session()
    
    connection_url = "tcp://" + ip + ":" + str(port)
    session.connect(connection_url)
    return session


def predict(image):
       
    rf = Roboflow(api_key="vdIHXBMIuOaqFRuiaO8V")
    project = rf.workspace().project("beverage-containers-3atxb")
    model = project.version(3).model

    # infer on a local image
    print(model.predict("your_image.jpg", confidence=40, overlap=30).json())



def get_pos_ore(session,link_name="LArm",Left_kinematic_chain=[
            "LShoulderRoll",
            "LElbowRoll"]):
    motion = session.service("ALMotion")


    link_pose = motion.getTransform(link_name, 2, True)




    position = [link_pose[3], link_pose[7], link_pose[11]]
    rotation = [link_pose[0], link_pose[1], link_pose[2], link_pose[9]]
    angles = motion.getAngles(Left_kinematic_chain,True)

    return angles+position+rotation






def get_image_info(session):

    import os 
    os.system('cmd /c "netsh wlan connect name=pepper2"' )


    time.sleep(4)

    move_head(session)




    # get_depth_image(session=session)
    # sys.exit()
    # Get the ALVideoDevice service
    video_service = session.service("ALVideoDevice")

    time.sleep(2)

    # Set the camera parameters
    camera_name = "CameraTop"  # Choose the camera name ("CameraTop" or "CameraBottom")
    resolution = 1  # Set the resolution (0: 160x120, 1: 320x240, 2: 640x480, 3: 1280x960)
    color_space = 11  # Set the color space (11: RGB)

    # Subscribe to the camera



    a = video_service.subscribeCamera("gfe23", 0, resolution, color_space, 30)

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
    time.sleep(4)
    process = subprocess.Popen([
        r"c:/Users/Rania/AppData/Local/Programs/Python/Python311/python.exe",
        r"c:/Users/Rania/Desktop/Graduation Project (ALL)/GP2/qi_sdk/predict.py"
    ], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # Read the output from stdout and stderr
    stdout, stderr = process.communicate()

    # Decode the output from bytes to string
    stdout = stdout.decode("utf-8")
    stderr = stderr.decode("utf-8")


    x,y = float(stdout[70:75]),float(stdout[75:])
    image = cv2.imread(r"C:\Users\Rania\Desktop\Graduation Project (ALL)\GP2\qi_sdk\prediction1.jpg")

    os.system('cmd /c "netsh wlan connect name=pepper2"' )
    time.sleep(5)
    
    return (x,y,image)






def get_observations(session):
        kinematics = get_pos_ore(session)

        x,y,image = get_image_info(session)

        obs = {"kinematics":kinematics,"soda_can":[x,y],"image":image.tolist()}
        return obs
    
def execute_action(session):
    pass