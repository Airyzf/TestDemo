import cv2
import json
import base64
import requests

with open('../Opencv-video/1.png', 'rb') as f:  # 以二进制读取图片
    data = f.read()
    encodestr = base64.b64encode(data) # 得到 byte 编码的数据
    img=str(encodestr,'utf-8')  # 重新编码数据
    res = {"image": img}
    print(res)
    # img = cv2.imread("../mnist-model/1.png")
# res = {"image": str(img.tolist()).encode('base64')}  # img是ndarray，无法直接用base64编码，否则会报错
# print(res)
    _ = requests.post("http://127.0.0.1:8081", data=json.dumps(res))



#打开摄像头
import numpy
import matplotlib.pyplot as plot
import cv2
import json
import base64
import requests

url = 'http://192.168.16.159:5001'
#摄像头对象
cap=cv2.VideoCapture(1)
#显示
while(1):
    ret,frame = cap.read()
    cv2.imshow("capture",frame)

    encodestr = base64.b64encode(frame) # 得到 byte 编码的数据
    img=str(encodestr,'utf-8')  # 重新编码数据
    res = {"image": img}
    ret = requests.post(url, data=json.dumps(res))
    print(ret.text)
    if(cv2.waitKey(1) & 0xFF==ord('q')):
        break
cap.release()
cv2.destroyAllWindows()
