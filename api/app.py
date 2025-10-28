from flask import Flask,render_template,request,url_for,redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from database import Base,Tasks,db
import os,dotenv
dotenv.load_dotenv()

app = Flask(__name__,template_folder='../templates')

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
db.init_app(app)


@app.route('/',methods=['POST','GET'])
def home():
    today=datetime.today()
    if request.method=='POST':
        task=Tasks(
            task=request.form['task'],
            status=0,
            starred=0,
            due_date=datetime.strptime(request.form['date'], "%Y-%m-%d").date()
        )
        db.session.add(task)
        db.session.commit()
    pending_tasks=db.session.query(Tasks).filter(Tasks.status==0).order_by(Tasks.starred.desc()).all()
    done_tasks=db.session.query(Tasks).filter(Tasks.status==1).all()

    db.session.commit()

    return render_template('index.html',pending_tasks=pending_tasks,done_tasks=done_tasks,date=today)

@app.route('/update/<id>',methods=['POST'])
def update_data(id):
    task_update=db.get_or_404(Tasks,id)
    task_update.status=1
    task_update.completed_date=datetime.today()
    db.session.commit()
    return redirect(url_for('home'))

@app.route('/delete/<id>',methods=['POST'])
def delete_data(id):
    task_delete=db.get_or_404(Tasks,id)
    db.session.delete(task_delete)
    db.session.commit()
    return redirect(url_for('home'))

@app.route('/star/<id>',methods=['POST'])
def star_data(id):
    task_star=db.get_or_404(Tasks,id)
    task_star.starred=1 if task_star.starred==0 else 0
    db.session.commit()
    return redirect(url_for('home'))

# Vercel serverless function handler
if __name__ == '__main__':
    app.run()
else:
    # For Vercel
    handler = app
