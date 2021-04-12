from picture import *
import cv2
import numpy as np
#model을 가져와서 로딩하고, 해당 모델 돌려서 결과 predict 
class bill(picture):

    def predict(self,model):
        print("bill prediction")
        return "bill_prediction"

    #프로세스 작업. 이미지를 전처리. bilateralFilter사용해서 
    def preprocess(self):
        picture = self.file_name
        image = cv2.imread(picture)
        dst = cv2.bilateralFilter(image, 0, 100, 15)
        return dst

    def find_rectangle(self,image):


    def detect_edge(self,image):
        kernel = np.ones((5, ), np.uint8)
        image = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
        img_canny = cv2.Canny(image, 50, 100, edges=None, apertureSize=None, L2gradient=None)
        return img_canny
    
    def image_process(self):
        preprocessed = self.preprocess()
        edge_detected = self.detect_edge(preprocessed)
        cv2.imwrite("edge.jpg",edge_detected)

    def get_ocr(this):
        model = ""
        return model