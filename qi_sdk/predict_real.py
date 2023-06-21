from stable_baselines3 import PPO
import ast
import sys
import numpy as np 
import json
# print("starrrtt0000000000000000000000000000")
# Retrieve the JSON string argument

# Parse the JSON string back into a dictionary
with open("obs.json", "r") as file:
        data = json.load(file)


# Use the dictionary as needed
data["image"] = np.array(data["image"]) 
model = PPO.load(r'C:\Users\Rania\Desktop\Graduation Project (ALL)\GP2\qi_sdk\models\PPO_inverse_threshold_newlist_lr_0.001')

action, _ = model.predict(data)

# Convert the string list to a real Python list
# python_list = ast.literal_eval(action)

# Print the converted list
print(action)
# print(type(action))
# print(action[0])



