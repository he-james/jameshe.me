"""Render mod_main templates."""

from flask import Blueprint, request, render_template, redirect, url_for
from app import db
from app.mod_main.models import Project


mod_main = Blueprint('main', __name__, url_prefix='/')


@mod_main.route('/', methods=['GET', 'POST'])
def home():
    """Render home page."""
    title = "Home | James He"
    return render_template("main/home.html", title=title)

@mod_main.route('/projects', methods=['GET', 'POST'])
def projects():
    title = "Projects | James He"
    return render_template("main/projects.html", title=title)
