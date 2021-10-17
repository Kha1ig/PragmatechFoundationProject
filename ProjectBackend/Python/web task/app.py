from flask import Flask, render_template,request,redirect,url_for
from flask.helpers import url_for
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
from werkzeug.utils import secure_filename
UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'static/portfoilo_img/')

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///stories.db'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

db = SQLAlchemy(app)


class Portfoilo(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    image=db.Column(db.String(20))



@app.route('/')
def index():
    return render_template("index.html")

@app.route('/about')

def about():
    return render_template("about.html")

@app.route('/resume')

def resume():
    return render_template("resume.html")


@app.route('/portfoilo')

def portfoilo():
    port=Portfoilo.query.all()
    return render_template("portfoilo.html", ports=port)

@app.route('/contact')

def contact():
    return render_template("contact.html")


###  ADMIN  ###
@app.route('/admin/add-portfoilo', methods=['GET','POST'])
def add_portfoilo():
    if request.method =='POST':
        file = request.files['file']
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        port=Portfoilo(
            image = filename
        )
        db.session.add(port)
        db.session.commit()
        return redirect(url_for('portfoilo'))
    return render_template('admin/add-portfoilo.html')

if __name__ == '__main__':
    app.run(debug=True)
    