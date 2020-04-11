import click
from present import app, db
from present.models import User, Present, PastRecord


@app.cli.command()
@click.option("--drop")
def initdb(drop):
    if drop:
        db.drop_all()

    db.create_all()
    click.echo("Initialized Database")


@app.cli.command()
def new_record():
    past = PastRecord(name=1)
    db.session.add(past)
    db.session.commit()


@app.cli.command()
def forge():
    past = PastRecord(name=1)
    db.session.add(past)
    db.session.commit()
    # """Generate fake data."""
    # db.drop_all()
    # db.create_all()

    # name = "Grey Li"
    # movies = [
    #     {"title": "My Neighbor Totoro", "past_id": 1},
    #     {"title": "Dead Poets Society", "past_id": 1},
    #     {"title": "A Perfect World", "past_id": 1},
    #     {"title": "Leon", "past_id": 2},
    #     {"title": "Mahjong", "past_id": 2},
    #     {"title": "Swallowtail Butterfly", "past_id": 2},
    #     {"title": "King of Comedy", "past_id": 3},
    #     {"title": "Devils on the Doorstep", "past_id": 3},
    #     {"title": "WALL-E", "past_id": 3},
    #     {"title": "The Pork of Music", "past_id": 3},
    # ]

    # user = User(name=name)
    # db.session.add(user)
    # for movie in movies:
    #     movie = Present(name=movie["title"], past_id=movie["past_id"])
    #     db.session.add(movie)
    # db.session.commit()
    # click.echo("Done.")

    # past = PastRecord(name=1, binggo_name="My Neighbor Totoro")
    # db.session.add(past)
    # past = PastRecord(name=2, binggo_name="Leon")
    # db.session.add(past)
    # past = PastRecord(name=3, binggo_name="WALL-E")
    # db.session.add(past)
    # db.session.commit()
    # click.echo("Done.")
