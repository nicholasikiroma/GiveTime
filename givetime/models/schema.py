#!/usr/bin/python3
"""Defines models for nonprofits"""
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

# Create a join table to connect volunteers with volunteering opportunities
# 



class Nonprofit(db.Model):
    """Models nonprofit"""
    __table__ = 'nonproft'

    nonprofit_id = db.Column(db.Integer, primary_key=True)
    volunteer_id = db.Column(db.Integer, db.ForeignKey('volunteer.volunteer_id'), nullable=False)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String, nullable=False)
    email = db.Column(db.String(45), nullable=False)
    phone = db.Column(db.String(45), nullable=False)
    website = db.Column(db.String(255), nullable=False)
    address = db.Column(db.String(255), nullable=False)
    social_media_links = db.Column(db.String(255))
    registration_date = db.Column(db.DateTime, nullable=False)
    verification_status = db.Column(db.Boolean, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    volunteer = db.relationship("Volunteer", back_populates="nonprofits")


class Volunteer(db.Model):
    """Schema for volunteer"""
    __tablename__ = 'volunteer'

    volunteer_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(256), nullable=False)
    last_name = db.Column(db.String(256), nullable=False)
    skill = db.Column(db.String(45), nullable=False)
    location = db.Column(db.String(45), nullable=False)
    password_hash = db.Column(db.String(45), nullable=False)
    email = db.Column(db.String(45), nullable=False)
    interests = db.Column(db.String(45), nullable=False)
    state = db.Column(db.String(45), nullable=False)
    city = db.Column(db.String(45), nullable=False)

class VolunteerOpportunities(db.Model):
    """Schema for volunteer opportunities"""
    __tablename__ = 'volunteer_opportunities'
    
    opp_id = db.Column(db.Integer, primary_key=True)
    opp_title = db.Column(db.String(45), nullable=False)
    nonprofit_id = db.Column(db.Integer, db.ForeignKey('nonprofit.nonprofit_id'), nullable=False)
    opp_description = db.Column(db.String(256), nullable=False)
    opp_location = db.Column(db.String(45), nullable=False)
    opp_start_date = db.Column(db.DateTime, nullable=False)
    opp_end_date = db.Column(db.DateTime, nullable=False)
    tags = db.relationship('VolunteerOpportunitiesTag', back_populates='opportunities')


class VolunteerOpportunitiesTag(db.Model):
    """Schema for volunteer opportunities tag"""
    __tablename__ = 'volunteer_opportunities_tag'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    tag = db.Column(db.String(45), nullable=False)
    opportunities_id = db.Column(db.Integer, db.ForeignKey('volunteer_opportunities.opp_id'))
    opportunities = db.relationship('VolunteerOpportunities', back_populates='tags')


class Tags(db.Model):
    """Schema for tags"""
    __tablename__ = 'tags'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(45), nullable=False)
    id_1 = db.Column(db.Integer, db.ForeignKey('volunteer_opportunities_tag.id'), nullable=False)
