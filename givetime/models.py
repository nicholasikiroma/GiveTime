from givetime import create_app
from datetime import datetime
from uuid import uuid4

db = create_app().db

class Nonprofit(db.Model):
    """Models nonprofit"""
    __tablename__ = 'nonprofit'

    id = uuid4()
    nonprofit_id = db.Column(db.String, primary_key=True, default=id)
    name = db.Column(db.String(255), nullable=False, unique=True)
    description = db.Column(db.Text, nullable=False)
    email = db.Column(db.String(45), nullable=False, unique=True)
    phone = db.Column(db.String(45), nullable=False)
    website = db.Column(db.String(255), nullable=True)
    address = db.Column(db.String(255), nullable=False)
    city = db.Column(db.String, nullable=False)
    state = db.Column(db.String, nullable=False)
    social_media_links = db.Column(db.String(255), nullable=True)
    registration_date = db.Column(db.DateTime, nullable=False,
                                  default=datetime.utcnow())
    verification_status = db.Column(db.Boolean, nullable=False, default=False)
    password_hash = db.Column(db.String(255), nullable=False)
    volunteers = db.relationship("Volunteer", secondary="nonprofit_volunteer", back_populates="nonprofits")


class Volunteer(db.Model):
    """Schema for volunteer"""
    __tablename__ = 'volunteer'
    id = uuid4()
    volunteer_id = db.Column(db.Integer, primary_key=True, default=id)
    first_name = db.Column(db.String(256), nullable=False)
    last_name = db.Column(db.String(256), nullable=False)
    skill = db.Column(db.String(45), nullable=False)
    city = db.Column(db.String, nullable=False)
    state = db.Column(db.String, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(45), nullable=False, unique=True)
    category = db.relationship("Interest", secondary="volunteer_interest", back_populates="volunteers")
    nonprofits = db.relationship("Nonprofit", secondary="nonprofit_volunteer", back_populates="volunteers")


class VolunteerOpportunities(db.Model):
    """Schema for volunteer opportunities"""
    __tablename__ = 'volunteer_opportunities'

    id = uuid4()
    opp_id = db.Column(db.Integer, primary_key=True, default=id)
    opp_title = db.Column(db.String(45), nullable=False)
    nonprofit_id = db.Column(db.Integer, db.ForeignKey('nonprofit.nonprofit_id'), nullable=False)
    nonprofit = db.relationship("Nonprofit", back_populates="volunteer_opportunities")
    opp_description = db.Column(db.String(256), nullable=False)
    opp_location = db.Column(db.String(45), nullable=False)
    opp_start_date = db.Column(db.DateTime, nullable=False)
    opp_end_date = db.Column(db.DateTime, nullable=False)
    tags = db.relationship('Tag', secondary='volunteer_opportunities_tag', back_populates='volunteer_opportunities')


class VolunteerOpportunitiesTag(db.Model):
    """Schema for volunteer opportunities tag"""
    __tablename__ = 'volunteer_opportunities_tag'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    tag_id = db.Column(db.Integer, db.ForeignKey('tag.id'), nullable=False)
    opportunities_id = db.Column(db.Integer, db.ForeignKey('volunteer_opportunities.opp_id'))
    volunteer_opportunities = db.relationship('VolunteerOpportunities', back_populates='tags')
    tag = db.relationship('Tag', back_populates='volunteer_opportunities')


class Tag(db.Model):
    """Schema for tags"""
    __tablename__ = 'tag'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(45), nullable=False, unique=True)
    volunteer_opportunities = db.relationship('VolunteerOpportunitiesTag', back_populates='tag')
    volunteers = db.relationship("Volunteer", secondary="volunteer_interest", back_populates="category")


class Category(db.Model):
    """Schema for volunteer interests"""
    __tablename__ = 'category'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45), nullable=False)


class VolunteerInterest(db.Model):
    """Association table for Volunteer and Interest"""
    __tablename__ = 'volunteer_interest'

    volunteer_id = db.Column(db.Integer, db.ForeignKey('volunteer.volunteer_id'), primary_key=True)
    interest_id = db.Column(db.Integer, db.ForeignKey('category.id'), primary_key=True)
    volunteer = db.relationship("Volunteer", back_populates="category")
    interest = db.relationship("Interest", back_populates="volunteers")