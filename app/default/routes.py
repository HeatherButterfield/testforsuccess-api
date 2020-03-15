from flask import Blueprint, jsonify, render_template, url_for
from app import app

default_blueprint = Blueprint('default_blueprint', __name__)

@default_blueprint.route('/', methods = ['GET'])
def index():
    routes = {}
    for r in app.url_map._rules:
        routes[r.rule] = {}

    routes.pop("/static/<path:filename>")

    result = sorted(routes.items())

    return render_template("all_links.html", links=result)