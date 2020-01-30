from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'oracle://kwilnick:kwilnick@ora3.elka.pw.edu.pl:1521/ora3inf'
db = SQLAlchemy(app)

from app_filharmonia import routes
