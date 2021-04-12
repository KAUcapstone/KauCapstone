#food class
#preprocessing, edge detection, find contours, find retangle
import cv2
from picture import *

class food(picture):
    def predict(self):
        print("food prediction")
        return "food_prediction"

    def get_prediction(self):
        model = "ha"
        print(self.file_name)
        return model

    def preprocess(self):
        picture = cv2.imread(self.file_name)
        