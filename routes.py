# Imports
from backend.application import application

from data.db_sesions import main_session
from data.models import *

from flask import render_template


@application.route("/", methods=["GET"])
def print_users() -> str:
    users = main_session.query(User).all()
    images = []
    for user in users:
        if user.image is None:
            images.append("None")
        else:
            images.append(main_session.query(Image).filter(Image.id == user.image).first().description)

    data = zip(users, images)

    return render_template("users.html", data=data)


@application.route("/<string:name>/<int:age>", methods=["GET"])
def add_user(name: str, age: int) -> str:
    user = User(name=name, age=age)
    main_session.add(user)
    main_session.commit()

    return render_template("users.html", users=[user])

