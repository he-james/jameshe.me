"""Create Flask object application."""

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configurations
app.config.from_object('config')
db = SQLAlchemy(app)

# Error Handling
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404


from app.mod_main.controllers import mod_main as main_module


app.register_blueprint(main_module)


db.create_all()
