from flask import Blueprint, jsonify, abort, make_response, request

from app import db
from app.models.movie import Movie

bp = Blueprint("bp", __name__, url_prefix="/movies")


@bp.route("", methods=["GET"])
def get_all_movies():
    movies = Movie.query.all()
    result = [movie.to_dict() for movie in movies]

    return jsonify(result)


@bp.route("/<id>", methods=["GET"])
def get_one_movie(id):
    return jsonify({"message": "success"})


@bp.route("", methods=["POST"])
def create_movie():
    request_body = request.get_json()

    if "title" not in request_body:
        return jsonify("invalid request"), 400

    new_movie = Movie.from_dict(request_body)

    db.session.add(new_movie)
    db.session.commit()

    return jsonify(f"Movie {new_movie.title} successfully created"), 200


@bp.route("/<id>", methods=["PUT"])
def update_one_movie(id):
    return jsonify({"message": "success"})


@bp.route("/<id>", methods=["PATCH"])
def update_one_or_more_movie_fields(id):
    return jsonify({"message": "success"})


@bp.route("/<id>", methods=["DELETE"])
def delete_movie(id):
    return jsonify({"message": "success"})


@bp.route("/<id>/reviews", methods=["GET"])
def get_reviews_for_a_movie(id):
    movie = Movie.query.get(id)
    movie_reviews = [review.to_dict() for review in movie.reviews]

    return jsonify(movie_reviews)
