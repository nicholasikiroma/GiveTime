#!/usr/bin/python3
"""Base Instance of Flask Application.

   Returns:
   -Instance of flask app

   Requires-import flask, flask_sqlalchemy, flask_login, flaskmail, os
"""
from flask import Flask, render_template, request, url_for
import os
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_required, current_user
from flask_migrate import Migrate
from sqlalchemy import MetaData
from flask_mail import Mail
import os

# set name conventions for database migrations
convention = {
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s",
}

metadata = MetaData(naming_convention=convention)

login_manager = LoginManager()
db = SQLAlchemy(metadata=metadata)
migrate = Migrate()
mail = Mail()


def create_app():
    """Base configurations for flask app"""

    app = Flask("__name__", template_folder="templates", static_folder="static")

    base_dir = os.path.dirname(os.path.realpath(__file__))

    app.config["MAIL_SERVER"] = "smtp.gmail.com"
    app.config["MAIL_PORT"] = 465
    app.config["MAIL_USERNAME"] = "givetimeng@gmail.com"
    app.config["MAIL_PASSWORD"] = os.environ.get("MAILPASSWORD")
    app.config["MAIL_USE_TLS"] = False
    app.config["MAIL_USE_SSL"] = True

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(
        base_dir, "givetimeStorage.db"
    )
    app.secret_key = os.environ.get("SECRET_KEY")

    db.init_app(app)

    login_manager.init_app(app)
    mail.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        # Determine which model to load the user from based on the
        # blueprint name
        from givetime.models.modified_model import Nonprofit, Volunteer

        user = Nonprofit.query.get(str(user_id))
        if user is None:
            user = Volunteer.query.get(str(user_id))

        return user

    # Registering App blueprints
    from givetime.auth.nonprofit_auth import nonprofit_bp
    from givetime.auth.volunteer_auth import volunteer_bp
    from givetime.dashboard.nonprofit_dashboard import dashboard_bp

    app.register_blueprint(nonprofit_bp)
    app.register_blueprint(volunteer_bp)
    app.register_blueprint(dashboard_bp)

    login_manager.login_view = "volunteer_auth.volunteer_login"
    # sets login view for nonprofit blueprint
    login_manager.blueprint_login_views = {
        "nonprofit_auth": "nonprofit_auth.nonprofit_login",
        "volunteer_auth": "volunteer_auth.volunteer_login",
    }

    @app.route("/")
    def index():
        """Renders template for home page"""
        from givetime.models.modified_model import Opportunity
        from sqlalchemy.orm import joinedload

        opportunities = Opportunity.query.options(
            joinedload(Opportunity.nonprofits), joinedload(Opportunity.categories)
        ).all()

        return render_template("index.html", opportunities=opportunities)

    @app.route("/apply/<nonprofit_name>/<string:id>")
    def apply(nonprofit_name, id):
        """Renders template for application page.

        Arguments:
        -Name of nonprofit
        -ID of opportunity

        Returns:
        -Template for application

        Requires-import joinedload from sqlalchemy.orm, Opportunity object
        """
        from givetime.models.modified_model import Opportunity
        from sqlalchemy.orm import joinedload

        user = id

        # Using joinedload function to form join view of
        # nonprofits and categories tables
        opportunities = (
            Opportunity.query.options(
                joinedload(Opportunity.nonprofits), joinedload(Opportunity.categories)
            )
            .filter(Opportunity.opp_id == user)
            .one()
        )

        return render_template("apply.html", opportunities=opportunities)

    @app.route("/application/<string:opp_id>")
    @login_required
    def application(opp_id):
        """Route for handling indivitual applicatons.

        Arguments:
        -ID of opportunity

        Returns:
        -Prints the "Successful" when executed without errors

        Requires-import Application object
        """
        user_id = current_user.volunteer_id

        from givetime.models.modified_model import Application

        # Creates new application instance
        Application.create(opportunity_id=opp_id, volunteer_id=user_id)

        return "Successful!"

    @app.route("/registration")
    def register():
        """Renders the html template for the explore page"""
        return render_template("registration.html")

    @app.route("/about")
    def about():
        """Renders template for about page"""
        return render_template("about.html")

    with app.app_context():
        # creates all tables within application context
        from givetime.models.modified_model import (
            Nonprofit,
            Category,
            Recommendation,
            Volunteer,
            VolunteerCategory,
            Application,
            Opportunity,
            OpportunityCategory,
        )

        db.create_all()

    migrate.init_app(app, db)

    return app
