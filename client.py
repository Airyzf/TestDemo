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