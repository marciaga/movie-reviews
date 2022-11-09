from flask import Blueprint, jsonify, abort, make_response, request

from app import db
from app.models.review import Review

bp = Blueprint("reviews_bp", __name__, url_prefix="/reviews")


@bp.route("", methods=["GET"])
def get_all_reviews():
    reviews = Review.query.all()
    result = [review.to_dict() for review in reviews]

    return jsonify(result)


@bp.route("", methods=["POST"])
def create_one_review():
    request_body = request.get_json()

    if "text" not in request_body or "rating" not in request_body or "movie_id" not in request_body:
        return jsonify("invalid request"), 400

    new_review = Review(
        text=request_body["text"],
        rating=request_body["rating"],
        movie_id=request_body["movie_id"]
    )


    db.session.add(new_review)
    db.session.commit()

    return jsonify(f"Review for movie with id {new_review.movie_id} successfully created"), 200

