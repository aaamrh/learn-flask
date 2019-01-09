from flask import Flask, make_response, redirect, url_for, session, request
import json
import os
    
app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY','tudou tudou,woshidigua')

@app.route('/')
def index():
    return '<h1>Hello Flask!!</h1>'


@app.route('/greet', defaults={"name":"marh"})
@app.route('/greet/<name>')
def greet(name):
    return'<h1>greet %s!</h1>' % name

@app.route('/set/<name>')
def set_cookie(name):
    
    # response = make_response('<h2>羞羞哒</h2>')
    response = make_response(redirect(url_for('greet',name='haha')))
    response.mimetype = 'text/plain'
    response.set_cookie('name', name, max_age=10)
    return response

@app.route('/login/')
def login():
    session['login_in'] = True
    return redirect(url_for('hello'))

@app.route('/')
@app.route('/hello/')
def hello():
    name = request.args.get('name')
    print(request)
    print(name)
    if name is None:
        name = request.cookies.get('name','Huan')
        response = '<h1>你好，%s</h1>' % name


        if 'login_in' in session:
            response += '登录了'
        else:
            response += '未登录'
            abort(403)
        return response