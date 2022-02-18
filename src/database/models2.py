import uuid

from sqlalchemy import Table, Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from werkzeug.security import generate_password_hash, check_password_hash

Base = declarative_base()

print(23)
from src import db

#
# association_table = Table('association', Base.metadata,
#     Column('left_id', ForeignKey('left.id')),
#     Column('right_id', ForeignKey('right.id'))
# )

# class Association(db.Model):
#     __tablename__ = 'association'
#     __table_args__ = {'extend_existing': True}
#
#     left_id = Column(ForeignKey('films.id'), primary_key=True)
#     right_id = Column(ForeignKey('actors.id'), primary_key=True)
#     extra_data = Column(String(50))
#
#     child = relationship("Film", backref="parent_associations")
#     parent = relationship("Actor", backref="child_associations")
#
#
# class Film(db.Model):
#     __tablename__ = 'films'
#     __table_args__ = {'extend_existing': True}
#
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(120), nullable=False)
#     release_date = db.Column(db.Date, index=True, nullable=False)
#     uuid = db.Column(db.String(36), unique=True)
#     description = db.Column(db.Text)
#     distributed_by = db.Column(db.String(120), nullable=False)
#     length = db.Column(db.Float)
#     rating = db.Column(db.Float)
#     children = relationship("Actor",backref=db.backref('films')
#                             primaryjoin="Film.id == Association.left_id")
#     # children = relationship("Actor",
#     #                 secondary=association_table,
#     #                 backref="parents",)
#     #                 #primaryjoin="Film.id == src.database.models2.association_table.left_id")
#
#
#     def __init__(self, title, release_date, description, distributed_by, length, rating, actors=None):
#         self.title = title
#         self.release_date = release_date
#         self.description = description
#         self.distributed_by = distributed_by
#         self.length = length
#         self.rating = rating
#         self.uuid = str(uuid.uuid4())
#         if not actors:
#             self.actors = []
#         else:
#             self.actors = actors
#
#     def __repr__(self):
#         return f'Film({self.title}, {self.uuid}, {self.distributed_by}, {self.release_date})'
#
#
# class Actor(db.Model):
#     __tablename__ = 'actors'
#     __table_args__ = {'extend_existing': True}
#
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(58), unique=True, nullable=False)
#     birthday = db.Column(db.Date)
#     is_active = db.Column(db.Boolean, default=False)
#
#     def __repr__(self):
#         return f"Actor({self.name}, {self.birthday})"

movies_table = Table(
    "movies_table",
    Base.metadata,
    db.Column("film_id", db.Integer, ForeignKey("films.id"), primary_key=True),
    db.Column("actor_id", db.Integer, ForeignKey("actors.id"), primary_key=True),
)


class Association(db.Model):
    __tablename__ = "association"
    __table_args__ = {"extend_existing": True}

    filmsss = Column(db.Integer, ForeignKey("films.id"), primary_key=True)
    actorsss = Column(db.Integer, ForeignKey("actors.id"), primary_key=True)
    # extra_data = Column(String(50))

    # child = relationship("Actor", backref="parent_associations")
    # parent = relationship("Film", backref="child_associations")


class Film(db.Model):
    __tablename__ = "films"
    __table_args__ = {"extend_existing": True}
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    release_date = db.Column(db.Date, index=True, nullable=False)
    uuid = db.Column(db.String(36), unique=True)
    description = db.Column(db.Text)
    distributed_by = db.Column(db.String(120), nullable=False)
    length = db.Column(db.Float)
    rating = db.Column(db.Float)
    # child=relationship("Actor", backref="parent_associations")
    # parent=relationship("Film", backref="child_associations")
    children = db.relationship(
        "Actor",
        secondary=Association.__tablename__,
        lazy="subquery",
        backref=db.backref("films", lazy=True),
        viewonly=True,
        overlaps="child,parent_associations",
    )

    # children=db.relationship("Association", backref='films_k')

    def __init__(
        self,
        title,
        release_date,
        description,
        distributed_by,
        length,
        rating,
        children=None,
    ):
        self.title = title
        self.release_date = release_date
        self.description = description
        self.distributed_by = distributed_by
        self.length = length
        self.rating = rating
        self.uuid = str(uuid.uuid4())
        if not children:
            self.children = []
        else:
            self.children = children
        print(children)

    def __repr__(self):
        return f"Film({self.title}, {self.uuid}, {self.distributed_by}, {self.release_date}, {self.rating},{self.children})"


class Actor(db.Model):
    __tablename__ = "actors"
    __table_args__ = {"extend_existing": True}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(58), unique=True, nullable=False)
    birthday = db.Column(db.Date)
    is_active = db.Column(db.Boolean, default=False)
    # child=relationship("Actor", backref="parent_associations"),
    # parent=relationship("Film", backref="child_associations")

    def __repr__(self):
        return f"Actor({self.name}, {self.birthday})"


class User(db.Model):
    __tablename__ = "users"
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(254), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)
    uuid = db.Column(db.String(36), unique=True)

    def __init__(self, username, email, password, is_admin=False):
        self.username = username
        self.email = email
        self.password = generate_password_hash(password)
        self.is_admin = is_admin
        self.uuid = str(uuid.uuid4())

    def __repr__(self):
        return f"User({self.username}, {self.email}, {self.uuid})"

    @classmethod
    def find_user_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_user_by_uuid(cls, uuid):
        return cls.query.filter_by(uuid=uuid).first()
