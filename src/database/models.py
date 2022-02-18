# import uuid
#
# from sqlalchemy import MetaData
# #
# from config import Config
# from src import db
#
# metadata = MetaData()
# #
# #
# # #
# from sqlalchemy import Table, Column, Integer, ForeignKey
# from sqlalchemy.orm import relationship
# from sqlalchemy.ext.declarative import declarative_base
#
# Base = declarative_base()
# # association_table = Table('association', Base.metadata,
# #     Column('left_id', ForeignKey('left.id'), primary_key=True),
# #     Column('right_id', ForeignKey('right.id'), primary_key=True)
# # )
# #
# # class Parent(db.Model):
# #     #__tablename__ = 'left'
# #     id = Column(Integer, primary_key=True)
# #     children = relationship("Child",
# #                     secondary=association_table,
# #                     backref="parentsuuuuuuuuuuuuuuu")
# #
# # class Child(db.Model):
# #     #__tablename__ = 'right'
# #     id = Column(Integer, primary_key=True)
# #
# # #
# # movies_actors = db.Table(
# #     'movies_actors',metadata,
# #     db.Column('actor_id', db.ForeignKey('actors.id'), primary_key=True),
# #     db.Column('film_id', db.ForeignKey('films.id'), primary_key=True)
# #
# # )
# # #
# # #
# # # from flask_login import UserMixin
# # # from flask_security import RoleMixin
# # #
#
#
#
#
#
#
#
#
#
# association_table = Table('association', Base.metadata,
#     Column('left_id', ForeignKey('left.id')),
#     Column('right_id', ForeignKey('right.id'))
# )
#
#
#
#
#
#
#
#
# class Actor(db.Model):
#     __tablename__ = 'actors'
#     __table_args__ = {'extend_existing': True}
#
#     id = db.Column(db.Integer, primary_key=True,unique=True)
#     name = db.Column(db.String(58), unique=True, nullable=False)
#     birthday = db.Column(db.Date)
#     is_active = db.Column(db.Boolean, default=False)
#     #parents = db.relationship('Film', secondary=movies_actors, back_populates='actors')
#
#     def __repr__(self):
#         return f"Actor({self.name}, {self.birthday})"
#
#
# class Film(db.Model):
#     __tablename__ = 'films'
#     __table_args__ = {'extend_existing': True}
#
#     id = db.Column(db.Integer, primary_key=True,unique=True)
#     title = db.Column(db.String(120), nullable=False)
#     release_date = db.Column(db.Date, index=True, nullable=False)
#     uuid = db.Column(db.String(36), unique=True)
#     description = db.Column(db.Text)
#     distributed_by = db.Column(db.String(120), nullable=False)
#     length = db.Column(db.Float)
#     rating = db.Column(db.Float)
#     # children = relationship("Actor",
#     #                 secondary=association_table,
#     #                 backref="parents")
#     #cats = db.relationship('Actor', secondary=movies_actors,lazy="subquery", backref=db.backref('films', lazy=True))
#     # children = relationship("Child",
#     #                 secondary=movies_actors,
#     #                 backref="parentsuuuuuuuuuuuuuuu")
# #     actors = db.relationship('Actor', secondary=movies_actors, back_populates='parents')
#     #actors = relationship("Actor", secondary=movies_actors,backref=db.backref('parents'))#, secondary=movies_actors, backref="hollywood")
# #
# #
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
#
#
