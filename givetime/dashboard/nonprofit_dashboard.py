#!/usr/bin/python3
"""Blueprint for Nonprofit dashboard"""
from flask import Blueprint, render_template, flash, redirect, request, url_for
from flask_login import login_required, current_user
from flask_mail import Message

dashboard_bp = Blueprint('dashboard',
                         __name__, url_prefix='/nonprofit/dashboard')


@dashboard_bp.route('/create', methods=['POST', "GET"])
@login_required
def create():
    from givetime.modified_model import Category, Opportunity, OpportunityCategory
    from givetime.dashboard.create_form import OpportunitiesForm
    
    
    form = OpportunitiesForm()
    form.categories.choices = [(c.category_id, c.name) for c in Category.query.order_by('name')]

    if request.method == 'POST':
        title = request.form.get('title')
        status = request.form.get('status')
        description = request.form.get('description')
        category_id = request.form.get('categories')
        location = request.form.get('location')
        
        category = Category.query.get(category_id)
        
        nonprofit_id = current_user.nonprofit_id
        
        Opportunity.create(title=title, description=description,
                                  location=location, nonprofit_id=nonprofit_id,
                                  category_id=category.category_id, status=status)
        
        flash("New Opportunity Created!")

    return render_template("dashboard/create_opportunity.html", form=form)


@dashboard_bp.route('/applications', methods=['POST', 'GET'])
@login_required
def applications():
    from givetime.modified_model import Application, Opportunity, Volunteer

    nonprofit_id = current_user.nonprofit_id

    opps = Opportunity.query.filter(Opportunity.nonprofit_id==nonprofit_id).all()
    opp_ids = [opp.opp_id for opp in opps]

    applications = Application.query.filter(Application.opportunity_id.in_(opp_ids)).all()

    volunteer_ids = [app.volunteer_id for app in applications]

    volunteers =  Volunteer.query.filter(Volunteer.volunteer_id.in_(volunteer_ids)).all()
    
    return render_template("dashboard/applications.html", volunteers=volunteers)


@dashboard_bp.route('/')
@login_required
def index():
    return render_template("dashboard/dashboard.html")


@dashboard_bp.route('/accept/<string:user_email>/<string:name>', methods=['GET'])
def accept(user_email, name):

    if request.method == 'GET':
        msg = Message("Testing",
                    sender="givetimeng@gmail.com",
                    recipients=[user_email])

        msg.html = f"<b>Congrats {name} ...It Works!</b>"
        
        from givetime import mail
        mail.send(msg)

        return "Invite Sent!"

