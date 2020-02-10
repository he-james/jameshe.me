"""Render MOD_AUTH templates."""

from flask import Blueprint, request, render_template, redirect, url_for
from app import db
from app.mod_main.models import Project


MOD_AUTH = Blueprint('auth', __name__, url_prefix='/')


@MOD_AUTH.route('/admin', methods=['GET', 'POST'])
def admin():
    """Render admin."""
    title = "Admin Login | James He"
    return render_template("auth/admin.html", title=title)

@MOD_AUTH.route('/admin/CRUD', methods=['GET', 'POST'])
def crud():
    """Renders projects."""
    title = "Admin Dashboard | James He"
    return render_template("auth/crud.html", title=title)

