from flask import Flask, make_response, redirect, url_for, session, request, abort, render_template,flash
import json
import os
    
app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY','tudou tudou,woshidigua')


user = {
'username': 'Grey Li',
'bio': 'A boy who loves movies and music.',
} 
movies = [
    {'name': 'My Neighbor Totoro', 'year': '1988'},
    {'name': 'Three Colours trilogy', 'year': '1993'},
    {'name': 'Forrest Gump', 'year': '1994'},
    {'name': 'Perfect Blue', 'year': '1997'},
    {'name': 'The Matrix', 'year': '1999'},
    {'name': 'Memento', 'year': '2000'},
    {'name': 'The Bucket list', 'year': '2007'},
    {'name': 'Black Swan', 'year': '2010'},
    {'name': 'Gone Girl', 'year': '2014'},
    {'name': 'CoCo', 'year': '2017'},
]



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
    session.permanent = True
    return redirect(url_for('hello'))


@app.route('/logout/')
def logout():
    if 'login_in' in session:
        session.pop('login_in')


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

        return response

@app.route('/watchlist/')
def watchlist():
    return render_template('watchlist.html', user=user, movies = movies)

@app.context_processor
def inject_foo():
    foo = 'I am foo.'
    bar = 'I am bar.'
    return dict(foo=foo,bar=bar)    


@app.route('/base/')
def base():
    return render_template('usebase.html')


@app.route('/flash/')
def just_flash():
    flash(u'这是flask的闪现') 
    return redirect(url_for('base'))


@app.errorhandler(404)
def page_not_found(e):
    return render_template('errors/404.html'), 404 