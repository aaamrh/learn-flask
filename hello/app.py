
from flask import Flask, make_response, redirect, url_for, session, request, abort, \
render_template,flash, send_from_directory
from flask_ckeditor import CKEditor
from flask_sqlalchemy import SQLAlchemy

import click
import json
import os
import uuid
import datetime

from forms import LoginForm, UploadForm, RichTextForm, NewPostForm, NewNoteForm, DeleteNoteForm, EditNoteForm

    
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://user:123123@192.168.11.228:3306/learnflask"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

app.config.update(
    MAX_CONTENT_LENGTH=3*1024*1024,
    UPLOAD_PATH = os.path.join(app.root_path, 'uploads'),
    CKEDITOR_SERVE_LOCAL = True,
    CKEDITOR_LANGUAGE = 'zh-cn'
) 
app.secret_key = os.getenv('SECRET_KEY','tudou tudou,woshidigua')

ckeditor = CKEditor(app)


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.Text)

    def __repr__(self):
        return '<Note %r>' % self.body


@app.route('/')
def index():
    form = DeleteNoteForm()
    notes = Note.query.all()
    return render_template('index.html', form=form, notes=notes)


@app.cli.command()
def initdb():
    db.create_all()
    click.echo('初始化数据库')


@app.route('/new', methods=['GET','POST'])
def new_note():
    form = NewNoteForm()
    if form.validate_on_submit():
        body = form.body.data
        note = Note(body=body)
        db.session.add(note)
        db.session.commit()
        flash('Your note is saved')
        return redirect(url_for('index'))
    return render_template('new_note.html', form=form)


@app.route('/edit/<int:note_id>', methods=['GET', 'POST'])
def edit_note(note_id):
    form = EditNoteForm()
    note = Note.query.get(note_id)
    if form.validate_on_submit():
        note.body = form.body.data
        db.session.commit()
        flash('修改成功')
        return redirect(url_for('index'))
    form.body.data = note.body
    return render_template("edit_note.html", form=form)


@app.route('/del/<int:note_id>', methods=['GET','POST'])
def delete_note(note_id):
    form = DeleteNoteForm()
    note = Note.query.get(note_id)

    if form.validate_on_submit():
        db.session.delete(note)
        db.session.commit()
        flash('删除成功')
    else:
        abort(404)
    return redirect(url_for('index'))


@app.errorhandler(404)
def page_not_found(e):
    return render_template('errors/404.html'), 404