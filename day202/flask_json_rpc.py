#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2019/12/15 16:33
# @Author: max liu
# @File  : flask_json_rpc.py

from flask import Flask
from flask import request
from datetime import datetime
import os
import base64

app = Flask(__name__)


@app.route('/rest/time', methods=['POST'])
def date():
    print(request.values)
    print(request.headers)
    '''
    http://docs.jinkan.org/docs/flask/api.html#flask.request
    get_json(force=False, silent=False, cache=True)
    Parses the incoming JSON request data and returns it. If parsing fails the on_json_loading_failed() method on the request object will be invoked. 
    By default this function will only load the json data 
    if the mimetype is application/json but this can be overriden by the force parameter.

参数:	
force – if set to True the mimetype is ignored.
silent – if set to False this method will fail silently and return False.
cache – if set to True the parsed JSON data is remembered on the request.
    '''
    print(request.get_json(force=True))
    print(request.get_json().get('function'))
    if request.get_json(force=True).get('function') == 'date':
        date1 = datetime.now().strftime('%Y-%m-%d')
        return {'results': date1}
    elif request.get_json().get('function') == 'datetime':
        datetime1 = datetime.now().strftime('%Y-%m-%d %h:%m:%s')
        return {'results': datetime1}


@app.route('/rest/cmd', methods=['POST'])
def cmd():
    print(request.headers)
    print(request.get_json())
    if request.get_json().get('cmd'):
        result = os.popen(request.get_json().get('cmd')).read().encode('utf-8')  # byte类型，即二进制
        print(type(result))
        result = base64.b64encode(result).decode('utf-8')  # B64编码对象只能为byte类型，编码后也为byte类型，decode后为
        print(type(result))
        print(result)
        return {'result': result}  # 构造json字符串，值必须为字符串（byte为不可序列化的对象）


@app.route('/download/<filename>', methods=['GET'])
def down(filename):
    UPLOAD_FOLDER = '/day_by_day_python_001/test_units'
    if os.path.isfile(os.path.join(UPLOAD_FOLDER, filename)):  # 判断文件是否存在，非文件夹
        with open(os.path.join(UPLOAD_FOLDER, filename), 'rb') as f:
            date1 = base64.b64encode(f.read()).decode('utf-8')
        return {'result': date1}
    return {'result': 'file not exists'}


@app.route('/upload/<filename>', methods=['PUT'])
def up(filename):
    UPLOAD_FOLDER = '/day_by_day_python_001/test_units'
    date1 = base64.b64decode(request.get_json().get('file'))
    with open(os.path.join(UPLOAD_FOLDER, filename), 'wb') as f:
        f.write(date1)
    return {'result': True}


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=7777,
        debug=True)
