from roboflow import Roboflow

rf = Roboflow(api_key="gS9k17WHXz3q7MRSBjXm")

project = rf.workspace("suspicious-movement").project("suspicious-detection")

dataset = project.version(7).download("yolov8")