from datetime import datetime
from givetime import db
from flask_login import UserMixin


class Volunteer(db.Model, UserMixin):
    """Model for volunteer table"""
    __tablename__ = 'volunteers'
    volunteer_id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    skill = db.Column(db.String(60), nullable=True)
    location = db.Column(db.String(60), nullable=True)
    password = db.Column(db.String(60), nullable=False)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    applications = db.relationship(
        'Application', backref='volunteers', cascade='all, delete-orphan')
    
    def get_id(self):
           return (self.volunteer_id)

    # static methid for creating a new instance and saving it to the detabase
    @staticmethod
    def create(first_name=None, last_name=None,
               email=None, password=None, skill=None, location=None):
        """Creates new entry"""
        volunteer = Volunteer(first_name=first_name,
                              last_name=last_name,
                              email=email,
                              password=password, skill=skill,
                              location=location)

        db.session.add(volunteer)
        db.session.commit()


class Category(db.Model):
    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

    # static methid for creating a new instance and saving it to the detabase
    @staticmethod
    def create(name=None):
        """Creates new entry"""
        category = Category(name=name)

        db.session.add(category)
        db.session.commit()


class VolunteerCategory(db.Model):
    """Model for volunteer table"""
    __tablename__ = 'volunteer_category'
    volunteer_id = db.Column(db.Integer, db.ForeignKey(
        'volunteers.volunteer_id'), primary_key=True)
    category_id = db.Column('category_id', db.Integer,
                            db.ForeignKey('categories.id'), primary_key=True)


class Nonprofit(db.Model, UserMixin):
    """Model for nonprofit table"""
    __tablename__ = 'nonprofits'
    nonprofit_id = db.Column(db.Integer, primary_key=True)
#   user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    website = db.Column(db.String(200), nullable=False)
    opportunities = db.relationship(
        'Opportunity', backref='nonprofits', cascade='all, delete-orphan')
    
    

    def get_id(self):
           return (self.nonprofit_id)

    # static methid for creating a new instance and saving it to the detabase
    @staticmethod
    def create(name=None, description=None,
               email=None, password=None, website=None):
        """Creates new entry"""
        nonprofit = Nonprofit(name=name, website=website,
                              email=email, description=description,
                              password=password)

        db.session.add(nonprofit)
        db.session.commit()


# class User(db.Model):
#    """Model for User table"""
#    __tablename__ = 'users'
#    user_id = db.Column(db.Integer, primary_key=True)
#    role = db.Column(db.Enum('volunteer', 'nonprofit'))
#    nonprofits = db.relationship('Nonprofit', backref='users', cascade='all, delete-orphan')
#    volunteers = db.relationship('Volunteer', backref='users', cascade='all, delete-orphan')


class Opportunity(db.Model):
    """Model for opportunities entity"""
    __tablename__ = 'opportunities'
    opp_id = db.Column(db.Integer, primary_key=True)
    nonprofit_id = db.Column(db.Integer, db.ForeignKey(
        'nonprofits.nonprofit_id'), nullable=False)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey(
        'categories.id'), nullable=False)
    location = db.Column(db.String(255), nullable=False)
    date = db.Column(db.Date, nullable=False, default=datetime.utcnow())
    status = db.Column(db.Enum('open', 'closed'), default='open', nullable=False)

    # static methid for creating a new instance and saving it to the detabase
    @staticmethod
    def create(title=None, description=None, location=None, nonprofit_id=None, category_id=None, status=None):
        """Creates new entry"""
        opportunity = Opportunity(title=title, description=description,
                                  location=location, nonprofit_id=nonprofit_id, category_id=category_id, status=status)

        db.session.add(opportunity)
        db.session.commit()


class Application(db.Model):
    """Model for application entity"""
    __tablename__ = 'applications'
    application_id = db.Column(db.Integer, primary_key=True)
    opportunity_id = db.Column(db.Integer, db.ForeignKey(
        'opportunities.opp_id', ondelete='CASCADE'), nullable=False)
    volunteer_id = db.Column(db.Integer, db.ForeignKey(
        'volunteers.volunteer_id', ondelete='CASCADE'), nullable=False)
    status = db.Column(db.Enum('pending', 'accepted',
                       'declined'), default='pending', nullable=False)


class Recommendation(db.Model):
    """Model for recommendation entity"""
    __tablename__ = 'recommendations'
    id = db.Column(db.Integer, primary_key=True)
    volunteer_id = db.Column(db.Integer, db.ForeignKey(
        'volunteers.volunteer_id'), nullable=False)
    opportunity_id = db.Column(db.Integer, db.ForeignKey(
        'opportunities.opp_id'), nullable=False)
