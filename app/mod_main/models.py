"""Defines database models."""

from app import db


class Base(db.Model):
    """Defines base parent model to inherit to other classes."""

    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
                              onupdate=db.func.current_timestamp())


class Project(Base):
    """Extend Base to include project attributes."""

    __tablename__ = 'project'

    # Project Name
    name = db.Column(db.String(70), nullable=False, unique=True)
    # Link to project
    link = db.Column(db.String(512), nullable=False, unique=True)
    # Link to source code
    src = db.Column(db.String(512), nullable=True, unique=True)
    # Description
    desc = db.Column(db.String(2000), nullable=True, unique=True)

    def __repr__(self):
        """Evaluate new instance (success/fail)."""
        return '<Project %r>' % self.name

def __init__(self, name, link, src, desc):
    """Instantiate new instance."""
    self.name = name
    self.link = link
    self.src = src
    self.desc = desc


