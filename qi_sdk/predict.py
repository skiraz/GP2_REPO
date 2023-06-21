from roboflow import Roboflow
rf = Roboflow(api_key="vdIHXBMIuOaqFRuiaO8V")
project = rf.workspace().project("beverage-containers-3atxb")
model = project.version(3).model
print(342432)
# infer on a local image
image_path = r"C:\Users\Rania\Desktop\Graduation Project (ALL)\GP2\qi_sdk\classify1.jpg"
# model.plot(image_path, confidence=40, overlap=30, save_path="predicted_image.jpg")
model.predict(image_path=image_path, confidence=40, overlap=30).save(r"C:\Users\Rania\Desktop\Graduation Project (ALL)\GP2\qi_sdk\prediction1.jpg")
x = model.predict(image_path, confidence=40, overlap=30).json()
print(x["predictions"][0]["x"],x["predictions"][0]["y"])













