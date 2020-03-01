#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2019/11/30 13:27
# @Author: max liu
# @File  : flask_003.py

from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/test01', methods=['GET'])
def test001():
    return render_template('test001.html')


@app.route('/test01', methods=['POST'])
def test002():
    page_list = request.form['page_num']
    if int(page_list) > 0: # 可以不用判断，模板已有判断
        return render_template('test001.html', page_num=page_list)
    else:
        return render_template('test001.html', page_num=page_list, message='请输入整数!')


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=7778,
        debug=True)
