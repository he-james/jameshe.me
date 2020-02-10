"""Render MOD_MAIN templates."""

from flask import Blueprint, request, render_template, redirect, url_for
from app import db
from app.mod_main.models import Project 


MOD_MAIN = Blueprint('main', __name__, url_prefix='/')


@MOD_MAIN.route('/', methods=['GET', 'POST'])
def home():
    """Render home page."""
    title = "Home | James He"
    return render_template("main/home.html", title=title)

@MOD_MAIN.route('/projects', methods=['GET', 'POST'])
def projects():
    """Renders projects."""
    title = "Projects | James He"
    return render_template("main/projects.html", title=title)

@MOD_MAIN.route('/blog', methods=['GET', 'POST'])
def blog():
    """Renders blog directory"""
    title = "Blog | James He"
    return render_template("main/blog.html", title=title)
