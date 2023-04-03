from givetime import db
from sqlalchemy import event
from datetime import datetime
from flask_login import UserMixin
from uuid import uuid4


class Volunteer(db.Model, UserMixin):
    """Model for volunteer table"""
    __tablename__ = 'volunteers'
    volunteer_id = db.Column(db.String(60),
                             primary_key=True,
                             default=lambda: str(uuid4()),
                             nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    skill = db.Column(db.String(60), nullable=True)
    location = db.Column(db.String(60), nullable=True)
    password = db.Column(db.String(60), nullable=False)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    applications = db.relationship('Application',
                                   backref='volunteers',
                                   cascade='all, delete-orphan')

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
    category_id = db.Column(db.String(60),
                            primary_key=True,
                            default=lambda: str(uuid4()),
                            nullable=False)
    name = db.Column(db.String(50), nullable=False)

    # static methid for creating a new instance and saving it to the detabase
    @staticmethod
    def create(name=None):
        """Creates new entry"""
        category = Category(name=name)

        db.session.add(category)
        db.session.commit()


class VolunteerCategory(db.Model):
    """Model for volunteer category relationship"""
    __tablename__ = 'volunteer_category'
    id = db.Column(db.String(60),
                   primary_key=True,
                   default=lambda: str(uuid4()),
                   nullable=False)
    volunteer_id = db.Column(db.String(60),
                             db.ForeignKey('volunteers.volunteer_id'))
    category_id = db.Column(db.String(60),
                            db.ForeignKey('categories.category_id'))


class Nonprofit(db.Model, UserMixin):
    """Model for nonprofit table"""
    __tablename__ = 'nonprofits'
    nonprofit_id = db.Column(db.String(60),
                             primary_key=True,
                             default=lambda: str(uuid4()), nullable=False)
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


class OpportunityCategory(db.Model):
    """Association table between Opportunity and Category models"""
    __tablename__ = 'opportunity_category'

    opp_id = db.Column(db.String(60),
                       db.ForeignKey('opportunities.opp_id'),
                       primary_key=True)
    category_id = db.Column(db.String(60),
                            db.ForeignKey('categories.category_id'),
                            primary_key=True)

    @staticmethod
    def create(opp_id=None, category_id=None):
        opp_cat = OpportunityCategory(opp_id=opp_id,
                                      category_id=category_id)
        db.session.add(opp_cat)
        db.session.commit()


class Opportunity(db.Model):
    """Model for opportunities entity"""
    __tablename__ = 'opportunities'
    opp_id = db.Column(db.String(60), primary_key=True,
                       default=lambda: str(uuid4()), nullable=False)
    nonprofit_id = db.Column(db.String(60), db.ForeignKey(
        'nonprofits.nonprofit_id'), nullable=False)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    category_id = db.Column(db.String(60), db.ForeignKey(
        'categories.category_id'), nullable=False)
    location = db.Column(db.String(255), nullable=False)
    date = db.Column(db.Date, nullable=False, default=datetime.utcnow())
    status = db.Column(db.Enum('open', 'closed'),
                       default='open', nullable=False)

    categories = db.relationship('Category',
                                 secondary='opportunity_category',
                                 backref=db.backref('opportunities',
                                                    lazy='dynamic'), lazy='joined')

    # static methid for creating a new instance and saving it to the detabase

    @staticmethod
    def create(title=None, description=None,
               location=None, nonprofit_id=None,
               category_id=None, status=None):
        """Creates new entry"""
        opportunity = Opportunity(title=title, description=description,
                                  location=location,
                                  nonprofit_id=nonprofit_id,
                                  category_id=category_id,
                                  status=status)

        db.session.add(opportunity)
        db.session.commit()


class Application(db.Model):
    """Model for application entity"""
    __tablename__ = 'applications'
    application_id = db.Column(db.String(60),
                               primary_key=True,
                               default=lambda: str(uuid4()),
                               nullable=False)
    opportunity_id = db.Column(db.String(60), db.ForeignKey(
        'opportunities.opp_id', ondelete='CASCADE'), nullable=False)
    volunteer_id = db.Column(db.String(60), db.ForeignKey(
        'volunteers.volunteer_id', ondelete='CASCADE'), nullable=False)
    status = db.Column(db.Enum('pending', 'accepted',
                       'declined'), default='pending', nullable=False)

    @staticmethod
    def create(opportunity_id=None, volunteer_id=None):
        """Creates new entry"""
        appliication = Application(
            opportunity_id=opportunity_id, volunteer_id=volunteer_id)

        db.session.add(appliication)
        db.session.commit()


class Recommendation(db.Model):
    """Model for recommendation entity"""
    __tablename__ = 'recommendations'
    id = db.Column(db.String(60), primary_key=True,
                   default=lambda: str(uuid4()), nullable=False)
    volunteer_id = db.Column(db.String(60), db.ForeignKey(
        'volunteers.volunteer_id'), nullable=False)
    opportunity_id = db.Column(db.String(60), db.ForeignKey(
        'opportunities.opp_id'), nullable=False)


@event.listens_for(Opportunity, 'after_insert')
def update_opportunity_category_table(mapper, connection, target):
    opportunity_category = OpportunityCategory(
        opp_id=target.opp_id,
        category_id=target.category_id)
    connection.execute(OpportunityCategory.__table__.insert(),
                       [opportunity_category.__dict__])
