#coding:utf-8
from flask import request, Flask
import json
import numpy as np
import time
import cv2
import base64

app = Flask(__name__)

@app.route("/", methods=['POST'])
def get_frame():
    start_time = time.time()
    res = json.loads(str(request.data,encoding='utf-8'))
    img_data_str = res["image"]  # dtype为int32

    img_byte = base64.b64decode(img_data_str)
    img_np_arr = np.fromstring(img_byte, np.uint8)
    frame = cv2.imdecode(img_np_arr, cv2.IMREAD_COLOR)

    #frame = np.array(frame, dtype=np.uint8)
    cv2.imwrite('tmp.jpg',frame)
    duration = time.time() - start_time
    print('duration:[%.0fms]' % (duration*1000))
    return '0000'

if __name__ == "__main__":
    app.run("127.0.0.1", port=8081)  #端口为8081