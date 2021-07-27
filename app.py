from bs4 import BeautifulSoup
import urllib
import urllib.request
import requests
import csv
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from main import *

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///justdial.db"
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)

# class Justdial(db.Model):
#     sno = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(200), nullable=False)
#     phone = db.Column(db.String(500), nullable=False)
#     rating = db.Column(db.String(15), nullable = False)
#     address = db.Column(db.String(100), nullable = False)
#     #date_created = db.Column(db.DateTime, default=datetime.utcnow)

#     def __repr__(self) -> str:
#         return f"{self.sno} - {self.name} - {self.phone} - {self.rating} - {self.address}"

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method=='POST':
        query = request.form['query']
        city = request.form['city']

        data = run_main(city, query)
        print(data)
        return render_template('index.html', data = data)
        #todo =(title=title, desc=desc)
        # db.session.add(todo)
        # db.session.commit()
        
    #allTodo = Justdial.query.all() 
    return render_template('index.html')


# @app.route('/update/<int:sno>', methods=['GET', 'POST'])
# def update(sno):
#     if request.method=='POST':
#         title = request.form['title']
#         desc = request.form['desc']
#         todo = Todo.query.filter_by(sno=sno).first()
#         todo.title = title
#         todo.desc = desc
#         db.session.add(todo)
#         db.session.commit()
#         return redirect("/")
        
#     todo = Todo.query.filter_by(sno=sno).first()
#     return render_template('update.html', todo=todo)

# @app.route('/delete/<int:sno>')
# def delete(sno):
#     todo = Todo.query.filter_by(sno=sno).first()
#     db.session.delete(todo)
#     db.session.commit()
#     return redirect("/")

if __name__ == "__main__":
    app.run(debug=True, port=8000)