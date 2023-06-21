from functions import *
import math
import subprocess
import json
import ast
import os


port = 9559
ip = "192.168.0.101"
session = connect(ip,port)


def move_init(session):
        posture_service = session.service("ALRobotPosture")

        posture_service.goToPosture("StandInit", .5)
        time.sleep(1)
    
        motion = session.service("ALMotion")
        initial_stand = [
            -1.562,
            -0.439,
            -0.048,
            0.154,
            ]
        Left_kinematic_chain = [
            "LShoulderRoll",
            "LShoulderPitch",
            "LElbowRoll",
            "LElbowYaw",
            ]

        motion.setAngles(  
            Left_kinematic_chain,
            initial_stand,
            0.5)
        # self.pepper.setAngles(["LShoulderRoll"],[0.009],1)
        motion.setAngles(["LShoulderRoll","HeadPitch","HeadYaw"],[1.562, 0.3,0.198],0.5)
        motion.setAngles(["LHand"],[0.98],0.5)
        motion.setAngles(["LWristYaw"],[-0.015],0.5)
        time.sleep(2)
    
    
    


def predict(session):

    observation = get_observations(session)

    # Define the command to execute the Python file with parameters
    python_file = r"C:\Users\Rania\Desktop\Graduation Project (ALL)\GP2\qi_sdk\predict_real.py"
      # Replace with the code to fetch observations from your real robot
    with open("obs.json", "w") as file:
        json.dump(observation, file)
    command = ["C:/Program Files (x86)/Microsoft Visual Studio/Shared/Python39_64/python.exe", python_file]

    # Execute the command and capture the output if needed
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    


    # Decode and print the output
    output = str(stdout.decode("utf-8"))

    values = output.strip("[]").split()

# Convert each value to float and create a Python list
    actions = [float(values[0]),float(values[1][:-1])]

    # Print the converted list
    return actions




    
move_init(session)

actions = predict(session)

os.system('cmd /c "netsh wlan connect name=pepper2"' )
time.sleep(4)
port = 9559
ip = "192.168.0.101"
session = connect(ip,port)
time.sleep(1)
motion =  session.service("ALMotion")


Left_kinematic_chain = [
            "LShoulderRoll",
            "LElbowRoll"]
motion.setAngles(Left_kinematic_chain,actions,0.5)






# Create an environment that matches the observations from the real robot


# Load the pre-trained model
# model = PPO.load(r'C:\Users\Rania\Desktop\Graduation Project (ALL)\GP2\qi_sdk\models\PPO_inverse_threshold_newlist_lr_0.001')

# Main loop for inference
while 0:
    # Get observation from the real robot

    # Preprocess the observation if needed

    # Use the pre-trained model to generate an action
    action, _ = model.predict(preprocessed_observation)

    # Send the action to the real robot for execution
    your_robot.execute_action(action)  # Replace with the code to send actions to your real robot













# model = SAC.load(os.path.join(env.models_dir,"SAC_lr_new_0.001"),env=env)
#     # obs,_ = env.reset()
#     # while True:
#     #     action, _states = model.predict(obs)
#     #     t0 = time.time()
#     #     obs, rewards, dones, info,_= env.step(action)
#     #     print(time.time()-t0)
#     #     # obs, reward, self.episode_over, 0,{}/
        
#     #     # break
#     #     # env.render()