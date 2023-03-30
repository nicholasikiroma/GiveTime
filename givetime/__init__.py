#!/usr/bin/python3
"""Base Flask Application for GiveTime"""
from flask import Flask, render_template, request
import os
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_required, current_user
from flask_migrate import Migrate
from sqlalchemy import MetaData
from flask_mail import Mail


convention = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}

metadata = MetaData(naming_convention=convention)


login_manager = LoginManager()
db = SQLAlchemy(metadata=metadata)
migrate = Migrate()
mail = Mail()


def create_app():

    app = Flask('__name__', template_folder='givetime/templates', static_folder='givetime/static')
    base_dir = os.path.dirname(os.path.realpath(__file__))

    app.config['MAIL_SERVER']='smtp.gmail.com'
    app.config['MAIL_PORT'] = 465
    app.config['MAIL_USERNAME'] = 'givetimeng@gmail.com'
    app.config['MAIL_PASSWORD'] = 'nnzfiuriduyiaslc'
    app.config['MAIL_USE_TLS'] = False
    app.config['MAIL_USE_SSL'] = True

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(
        base_dir, 'givetimeStorage.db')
    app.secret_key = '8745f7abde63c4ba78c4d60c863ded4eaf4bdf239dc3d2c866364629ab07f73b'

    db.init_app(app)


    @app.route('/')
    def index():
        """Renders template for home page"""
        from givetime.modified_model import Opportunity
        from sqlalchemy.orm import joinedload

        opportunities = Opportunity.query.options(
            joinedload(Opportunity.nonprofits), joinedload(Opportunity.categories)).all()


        return render_template('index.html', opportunities=opportunities)


    @app.route('/apply/<nonprofit_name>/<string:id>')
    @login_required
    def apply(nonprofit_name, id):
        """Renders template for home page"""
        from givetime.modified_model import Opportunity
        from sqlalchemy.orm import joinedload

        x = id
        opportunities = Opportunity.query.options(joinedload(Opportunity.nonprofits), joinedload(Opportunity.categories)).filter(Opportunity.opp_id==x).one()

        return render_template('apply.html', opportunities=opportunities)


    @app.route('/application/<string:opp_id>')
    def application(opp_id):
        user_id = current_user.volunteer_id
        from givetime.modified_model import Application
        Application.create(opportunity_id=opp_id, volunteer_id=user_id)
        return "Successful!"


    @app.route('/registration')
    def register():
        """Renders the html template for the explore page"""
        return render_template('registration.html')


    @app.route('/about')
    def about():
        return render_template('about.html')


    from givetime.auth.nonprofit_auth import nonprofit_bp
    from givetime.auth.volunteer_auth import volunteer_bp

    app.register_blueprint(nonprofit_bp)
    app.register_blueprint(volunteer_bp)

    from givetime.dashboard.nonprofit_dashboard import dashboard_bp
    app.register_blueprint(dashboard_bp)


    login_manager.blueprint_login_views = {
        "nonprofit_auth" : "nonprofit_auth.nonprofit_login",
    }
    login_manager.init_app(app)
    mail.init_app(app)


    @login_manager.user_loader
    def load_user(user_id):
        # Determine which model to load the user from based on the
        # blueprint name
        from givetime.modified_model import Nonprofit, Volunteer

        x = Nonprofit.query.get(str(user_id))
        if x == None:
            x = Volunteer.query.get(str(user_id))

        return x

    with app.app_context():
        from givetime.modified_model import Nonprofit, Category, Recommendation, Volunteer, VolunteerCategory, Application, Opportunity, OpportunityCategory
        db.create_all()


    migrate.init_app(app, db)

    return app
