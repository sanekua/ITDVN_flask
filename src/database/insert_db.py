from datetime import date

from src import db
from src.database.models2 import Film, Actor


def add_films_to_db():
    avatar = Film(
        title='Avatar',
        release_date=date(2009, 7, 16),
        description='A paraplegic Marine dispatched to the moon Pandora on',
        distributed_by='Warner',
        length=253,
        rating=8.6,
    )

    shawshank = Film(
        title='The Shawshank Redemption',
        release_date=date(1994, 8, 16),
        description='Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency',
        distributed_by='HBO',
        length=144,
        rating=9.6,
    )

    batman = Film(
        title='Batman',
        release_date=date(2005, 11, 10),
        description='When the menace known as the Joker wreaks havoc and chaos on the people of Gotham, Batman must accept one of the greatest psychological and physical tests of his ability to fight injustice',
        distributed_by='HBO',
        length=150,
        rating=9.0,
    )

    seven = Film(
        title='Seven',
        release_date=date(1995, 1, 20),
        description='Two detectives, a rookie and a veteran, hunt a serial killer who uses the seven deadly sins as his motives',
        distributed_by='Pixar',
        length=120,
        rating=8.6,
    )

    godfather = Film(
        title='Godfather',
        release_date=date(1972, 9, 20),
        description='The aging patriarch of an organized crime dynasty in postwar New York City transfers control of his clandestine empire to his reluctant youngest son',
        distributed_by='Warner',
        length=140,
        rating=9.1,
    )

    pirates = Film(
        title='Pirates of Carribean',
        release_date=date(2005, 3, 22),
        description='Jack Sparrow and a team wants to be pirates',
        distributed_by='Pixar',
        length=135,
        rating=7.1,
    )

    harry_potter = Film(
        title='Harry Potter part 1',
        release_date=date(2007, 5, 22),
        description='Adventure of harry potter and philisophically stone',
        distributed_by='Warner',
        length=110,
        rating=8.6,
    )

    daniel_radcliffe = Actor(name='Daniel Radcliffe', birthday=date(1987, 7, 22), is_active=True)
    emma_watson = Actor(name='Emma Watson', birthday=date(1997, 11, 2), is_active=True)
    hue_jackman = Actor(name='Hue Jackman', birthday=date(1977, 7, 1), is_active=True)
    will_smith = Actor(name='Will Smith', birthday=date(1980, 1, 2), is_active=True)
    keanu_reaves = Actor(name='Keany Reaves', birthday=date(1970, 11, 21), is_active=True)
    rupert_grint = Actor(name='Ruper Grint', birthday=date(1970, 11, 21), is_active=True)


    harry_potter.children=[daniel_radcliffe, emma_watson, rupert_grint]
    avatar.children=[daniel_radcliffe,hue_jackman,will_smith]
    batman.children=[keanu_reaves,rupert_grint,hue_jackman,emma_watson]
    godfather.children=[will_smith,hue_jackman]
    shawshank.children=[hue_jackman, keanu_reaves]
    seven.children=[will_smith,emma_watson,daniel_radcliffe, hue_jackman, rupert_grint, keanu_reaves]
    pirates.children=[keanu_reaves, will_smith, hue_jackman]

    db.session.add(avatar)

    db.session.add(shawshank)
    db.session.add(batman)
    db.session.add(seven)
    db.session.add(godfather)
    db.session.add(pirates)
    db.session.add(harry_potter)

    db.session.add(daniel_radcliffe)
    db.session.add(emma_watson)
    db.session.add(hue_jackman)
    db.session.add(will_smith)
    db.session.add(keanu_reaves)
    db.session.add(rupert_grint)
    print(harry_potter.children)

    db.session.commit()
    db.session.close()


if __name__ == "__main__":
    print("Adding films to db")
    add_films_to_db()
    #addi()
    print('Succes')
