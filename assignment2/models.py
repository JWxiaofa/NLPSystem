from flask_sqlalchemy import SQLAlchemy
from app import db

class Entity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(255), nullable=False)
    count = db.Column(db.Integer, default=1)
    # Create a relationship to the Head model, which will contain head words
    heads = db.relationship('Relationship', backref='entity', lazy='dynamic')

class Relationship(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(255), nullable=False)
    count = db.Column(db.Integer, default=1)
    relation = db.Column(db.String(50), nullable=False)
    entity_id = db.Column(db.Integer, db.ForeignKey('entity.id'), nullable=False)