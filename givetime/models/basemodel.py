"""Module defines class methods for all models"""
from givetime import db


class BaseModel(db.Model):
    """utility methods for models"""
    __abstract__ = True

    @classmethod
    def create(cls, **kwargs):
        """Creates new class instance"""
        instance = cls(**kwargs)
        db.session.add(instance)
        db.session.commit()

    @classmethod
    def update(cls):
        """Creates new class instance"""
        db.session.commit()

    @classmethod
    def delete(cls, **kwargs):
        """Creates new class instance"""
        instance = cls(**kwargs)
        db.session.delete(instance)
        db.session.commit()
