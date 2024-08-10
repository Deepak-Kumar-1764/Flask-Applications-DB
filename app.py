from flask import Flask,render_template,redirect,request
from flask_scss import Scss
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

#My App of Setup
app = Flask(__name__)
Scss(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///./database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATION"] = False
db = SQLAlchemy(app)


#Data class ~ Row of data
class MyTask(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    content = db.Column(db.String(100), nullable = False)
    complete = db.Column(db.Integer)
    created = db.Column(db.DateTime,default = datetime.utcnow)


    def __repr__(self) ->str:
        return f"Task{self.id}"

with app.app_context():
    db.create_all()

#Routes of webpages
#Homepage
@app.route("/",methods = ["POST","GET"])
def index():
    #add a task
    if request.method == "POST":
        current_task = request.form['content']
        new_task = MyTask(content = current_task)
        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect("/") 
        except Exception as e:
            print(f"ERROR :{e}")
            return f"ERROR:{e}"
        
    #see all current task
    else:
        tasks = MyTask.query.order_by(MyTask.created).all()
        return render_template("index.html", tasks = tasks)


#https://www.google.com/

#delete an Item
@app.route("/delete/<int:id>")
def delete(id:int):
    delete_task = MyTask.query.get_or_404(id)
    try:
        db.session.delete(delete_task)
        db.session.commit()
        return redirect("/")
    except Exception as e:
        return f"ERROR:{e}"


@app.route("/edit/<int:id>", methods= ["GET","POST"])
def edit(id:int):
    task = MyTask.query.get_or_404(id)
    if request.method == "POST":
     task.content = request.form['content']
     try:
         db.session.commit()
         return redirect("/")
     except Exception as e:
         return f"ERROR:{e}"
    else:
        return render_template('edit.html', task = task)
    
#runner and debugger
if __name__ in "__main__":
   app.run(host = '0.0.0.0',port = 200,debug = True)