#!/usr/bin/python3
"""Base Flask Application for GiveTime"""
from flask import Flask, render_template, request
import os
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate


login_manager = LoginManager()
db = SQLAlchemy()
migrate = Migrate()


opportunities = [
    {
    "title": "Eco-Village",
    "category": "Environment/Sustainability",
    "description": "GreenThumb's Eco-Village project aims to create sustainable living spaces in urban areas, promoting eco-friendly living and reducing carbon footprints. The project involves constructing eco-friendly buildings, providing community gardens, and educating residents on sustainable living practices.",
    "nonprofit_name": "GreenThumb"
    },
    {
    "title": "Mobile Medical Clinic",
    "category": "Healthcare",
    "description": " HealthFirst's Mobile Medical Clinic project aims to provide healthcare services to underserved communities by bringing medical professionals and resources to them. The project involves equipping and operating mobile clinics to offer services such as medical consultations, vaccinations, and health screenings.",
    "nonprofit_name": "HealthFirst"
    },
    {
    "title": "Wildlife Rehabilitation",
    "category": "Animal Welfare",
    "description": "Animal Allies' Wildlife Rehabilitation project aims to rescue, rehabilitate, and release injured and orphaned wild animals back into their natural habitats. The project involves setting up rehabilitation centers staffed by trained professionals to provide medical care and support for wildlife in need.",
    "nonprofit_name": "Animal Allies"
    },
    {
    "title": "Career Training Program",
    "category": "Youth Development",
    "description": "YouthBuilders' Career Training Program project aims to provide young people with the skills and training they need to succeed in the workforce. The project involves offering vocational training and mentorship programs to help youth gain practical skills, experience, and confidence.",
    "nonprofit_name": "YouthBuilders"
    },
    {
    "title": "Homeless Shelter Expansion",
    "category": "Community Development",
    "description": "HomeSafe's Homeless Shelter Expansion project aims to expand the organization's shelter facilities to provide more safe and supportive housing for homeless individuals and families. The project involves renovating existing facilities and constructing new buildings to accommodate more people.",
    "nonprofit_name": "HomeSafe"
    },
    {
    "title": "Community Art Project",
    "category": "Arts/Culture",
    "description": "ArtReach's Community Art Project aims to engage and inspire local communities through public art installations. The project involves organizing art workshops, recruiting artists to create public art pieces, and collaborating with local organizations to bring art to public spaces.",
    "nonprofit_name": "ArtReach"
    },
    {
    "title": "Domestic Violence Counseling Program",
    "category": "Mental Health",
    "description": "HopeWorks' Domestic Violence Counseling Program project aims to provide counseling and support services to survivors of domestic violence. The project involves offering individual and group counseling, safety planning, and legal advocacy to help survivors heal and rebuild their lives.",
    "nonprofit_name": "HopeWorks"
    },
    {
    "title": "Community Garden Project",
    "category": "Food/Security",
    "description": "FoodForAll's Community Garden Project aims to increase access to fresh, healthy food for low-income communities by creating community gardens. The project involves setting up and maintaining community gardens, providing gardening education, and distributing the harvest to those in need.",
    "nonprofit_name": "FoodForAll"
    },
    {
    "title": "Digital Literacy Program",
    "category": "Education/Technology",
    "description": "TechBridge's Digital Literacy Program project aims to bridge the digital divide by providing technology education and access to underserved communities. The project involves offering computer and internet access, technology training, and digital skills workshops to help individuals and families thrive in the digital age.",
    "nonprofit_name": "TechBridge"
    },
    {
    "title": "Language Exchange Program",
    "category": "Diversity/Inclusion",
    "description": "CultureConnect's Language Exchange Program aims to promote cross-cultural understanding and language learning by connecting people from different backgrounds. The project involves pairing language learners with native speakers for conversation practice, cultural exchange events, and language classes.",
    "nonprofit_name": "CultureConnect"
    }
]


def create_app():

    app = Flask('__name__', template_folder='givetime/templates', static_folder='givetime/static')
    base_dir = os.path.dirname(os.path.realpath(__file__))
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(
        base_dir, 'givetimeStorage.db')
    app.secret_key = '8745f7abde63c4ba78c4d60c863ded4eaf4bdf239dc3d2c866364629ab07f73b'

    db.init_app(app)


    @app.route('/')
    def index():
        """Renders template for home page"""
        return render_template('index.html', opportunities=opportunities)


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


    @login_manager.user_loader
    def load_user(user_id):
        # Determine which model to load the user from based on the
        # blueprint name
        from givetime.modified_model import Nonprofit, Volunteer

        x = Nonprofit.query.get(int(user_id))
        if x == None:
            x = Volunteer.query.get(int(user_id))

        return x

    with app.app_context():
        from givetime.modified_model import Nonprofit, Category, Recommendation, Volunteer, VolunteerCategory, Application, Opportunity


    migrate.init_app(app, db)

    return app
