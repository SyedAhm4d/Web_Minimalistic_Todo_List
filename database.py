from flask import Flask,render_template,request,url_for,redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import mapped_column,Mapped,DeclarativeBase
from sqlalchemy import Integer,String,Boolean,Date
from datetime import datetime
import os,dotenv
dotenv.load_dotenv()


class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)

class Tasks(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    task: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    status: Mapped[str] = mapped_column(Integer, nullable=False)
    starred: Mapped[str] = mapped_column(Integer, nullable=False)
    due_date: Mapped[str] = mapped_column(Date, nullable=False)
    completed_date: Mapped[str] = mapped_column(Date, nullable=True)
