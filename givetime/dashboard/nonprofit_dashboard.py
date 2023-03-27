#!/usr/bin/python3
"""Blueprint for Nonprofit dashboard"""
from flask import Blueprint, render_template, flash, redirect, request, url_for
from flask_login import login_required

dashboard_bp = Blueprint('dashboard',
                         __name__, url_prefix='/nonprofit/dashboard')


@dashboard_bp.route('/create')
def create():
    from givetime.modified_model import Category
    categories = Category.query.all()
    return render_template("dashboard/create_opportunity.html", categories=categories)


@dashboard_bp.route('/applications')
def applications():
    from givetime.modified_model import Application

    return render_template("dashboard/applications.html")


@dashboard_bp.route('/')
@login_required
def index():
    return render_template("dashboard/dashboard.html")
