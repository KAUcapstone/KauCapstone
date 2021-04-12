from flask import Flask, jsonify, request, make_response, send_file
import pymysql
import os
from bill import *
from food import *
from werkzeug.utils import secure_filename
#
# db = pymysql.connect(user="root")
UPLOAD_FOLDER ='/workspace/KauCapstone/workspace/dataset'

app = Flask(__name__)
app.config["CORS_HEADERS"] = 'Content-Type'
app.config['JSON_AS_ASCII'] = False

#picture 업로딩(모델에 돌릴 사진 업로딩) 
def upload_pic(file):
    file_name =secure_filename(file.filename) 
    file.save(os.path.join(UPLOAD_FOLDER,file_name))
    # 여기서 모델을 돌릴모델 설정해줘야됨
    file_name = UPLOAD_FOLDER+"/"+file_name
    return file_name

def predict_bill(filename):
    #영수증 예측 모델을 여기서 돌림 
    return ""

def predict_food(filename):
    #음식 예측 모델을 여기서 돌림
    return ""
# 여기서 bill ocr 모델을 돌려야함
@app.route('/bill_pic_prediction',methods=['POST'])
def bill_prediction():
    if request.method == 'POST':
        file = request.files['file']
        file_name = upload_pic(file)
        bill = bill(file_name)
        bill.image_process()
            
        
@app.route('/food_pic_predicton',methods = ['POST'])
def food_prediction():
    if request.method == 'POST':        
        file = request.files['file']
        file_name = upload_pic(file)
        print(file_name)
        food(file_name)


if __name__ == '__main__':
    bill = bill("/Users/andy/Desktop/KauCapstone/workspace/paper.jpg")
    bill.image_process()
    
    app.run(host='0.0.0.0', port="5000", debug=True)
    
