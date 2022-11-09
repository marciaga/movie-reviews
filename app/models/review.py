from app import db

class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    text = db.Column(db.String)
    rating = db.Column(db.Integer)
    movie_id = db.Column(db.Integer, db.ForeignKey("movie.id"))
    movie = db.relationship("Movie", back_populates="reviews")

    def to_dict(self):
        review_dict = dict(
            id=self.id,
            text=self.text,
            rating=self.rating
        )

        return review_dict

    @classmethod
    def from_dict(cls, data_dict):
        return cls(text=data_dict["text"], rating=data_dict["rating"])
