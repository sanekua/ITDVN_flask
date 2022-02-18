"""
SELECT QUERIES

"""
from sqlalchemy import and_

from src import db
from src.database import models2

films = db.session.query(models2.Film).order_by(models2.Film.rating.desc()).all()
print(films)

harry_potter = db.session.query(models2.Film).filter(
    models2.Film.title == "Avatar"
).first()

harry_potter2 = db.session.query(models2.Film).filter_by(
    title="Seven"
).first()

print(harry_potter2)

statement=db.session.query(models2.Film).filter(
    models2.Film.title != 'Avatar' or "Seven",
    models2.Film.rating >= 9.0
).all()


statement_and=db.session.query(models2.Film).filter(
    and_(
        models2.Film.title != 'Avatar' or "Seven",
        models2.Film.rating >= 9.0)
).all()

print('-----------------')

for i in statement_and:
    print(i)
# print(statement, len(statement))

print('---------------'
      'Matrix')
matrix = db.session.query(models2.Film).filter(
    models2.Film.title.ilike("%matrix%")
).all()


print([i for i in matrix])

print('#############')
length= db.session.query(models2.Film).filter(
    ~models2.Film.length.in_(range(180,270))
)[:3]

print('length', length)


films_with_actor=db.session.query(models2.Film).join(models2.Film.children).all(
)

print(films_with_actor)