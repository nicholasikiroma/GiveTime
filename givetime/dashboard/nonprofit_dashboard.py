#!/usr/bin/python3
"""Blueprint for Nonprofit dashboard"""
from flask import Blueprint, render_template, flash, redirect, request, url_for

dashboard_bp = Blueprint('dashboard',
                         __name__, url_prefix='/nonprofit/dashboard')

@dashboard_bp.route('/create')
def create():
    return render_template("dashboard/create_opportunity.html")



@dashboard_bp.route('/applications')
def applications():
    return render_template("dashboard/applications.html")



@dashboard_bp.route('/')
def index():
    return render_template("dashboard/dashboard.html")