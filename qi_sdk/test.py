from functions import * 
import math
# import numpy as np 
import subprocess
import json
# from stable_baselines3 import PPO



port = 9559
ip = "192.168.0.101"
session = connect(ip,port)
print(session)

motion =  session.service("ALMotion")






with open("obs.json", "r") as file:
        data = json.load(file)

# Use the dictionary as needed
data["image"] = np.array(data["image"]) 
print(data)
# model = PPO.load(r'C:\Users\Rania\Desktop\Graduation Project (ALL)\GP2\qi_sdk\models\PPO_inverse_threshold_newlist_lr_0.001')

# action, _ = model.predict(data)

# print(action)

port = 9559
ip = "192.168.0.101"
session = connect(ip,port)
obs = get_observations(session)# autonomous_life = session.service("ALAutonomousLife")
print(obs)
# # Disable autonomous mode
# autonomous_life.setState("disabled")

# # Disconnect from the robot
# session.close()
# audio_device = session.service("ALAudioDevice")

# # Get the current volume level
# current_volume = audio_device.getOutputVolume()

# # Raise the volume by a desired increment
# volume_increment = 40  # Adjust the increment as needed
# new_volume = current_volume - volume_increment

# # Get the ALRobotPosture service
# robot_posture = session.service("ALRobotPosture")

# # Wake up Pepper
# robot_posture.goToPosture("Stand", 1.0)  # "Stand" is the posture name, adjust the speed (1.0) as desired

# # Disconnect from the robot
# session.close()


get_image_info(session=session)



# Get the ALRobotPosture service

# Get the ALMotion service
print(get_pos_ore(session))
SystemExit()

motion = session.service("ALMotion")

# Specify the name of the link you want to retrieve the pose of
link_name = "LArm"

# Get the position and rotation of the specified link


# Get the position and rotation matrix of the specified link
link_pose = motion.getTransform(link_name, 2, True)


position = link_pose[:3]

# Extract rotation values (roll, pitch, yaw)
rotation_matrix = link_pose[3:12]
rotation = [math.degrees(math.atan2(rotation_matrix[7], rotation_matrix[8])),
            math.degrees(math.atan2(-rotation_matrix[6], math.sqrt(rotation_matrix[7]**2 + rotation_matrix[8]**2))),
            math.degrees(math.atan2(rotation_matrix[3], rotation_matrix[0]))]

position = [link_pose[3], link_pose[7], link_pose[11]]
rotation = [link_pose[0], link_pose[1], link_pose[2], link_pose[9]]
Left_kinematic_chain = [
            "LShoulderRoll",
            "LElbowRoll"]


# link_position = link_pose[:3]
# link_rotation_matrix = np.array(link_pose[3:])

# # # Convert the rotation matrix to Euler angles
# # link_rotation_euler = np.array([math.atan2(link_rotation_matrix[2, 1], link_rotation_matrix[2, 2]),
# #                                 math.atan2(-link_rotation_matrix[2, 0],
# #                                            math.sqrt(link_rotation_matrix[2, 1] ** 2 +
# #                                                      link_rotation_matrix[2, 2] ** 2)),
# #                                 math.atan2(link_rotation_matrix[1, 0], link_rotation_matrix[0, 0])])

# # # Print the position and rotation (Euler angles)
# # print("Position of", link_name, ":", link_position)
# # print("Rotation of", link_name, ":", link_rotation_euler)

# # Disconnect from the robot
