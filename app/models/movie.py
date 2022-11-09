from app import db


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String)
    genre = db.Column(db.String, nullable=True)
    year = db.Column(db.Integer, nullable=True)
    description = db.Column(db.String, nullable=True)
    duration = db.Column(db.Integer, nullable=True)
    reviews = db.relationship("Review", back_populates="movie")

    def to_dict(self):
        movie_dict = dict(
            id=self.id,
            title=self.title,
            genre=self.genre,
            year=self.year,
            description=self.description,
            duration=self.duration,
        )

        return movie_dict

    @classmethod
    def from_dict(cls, data_dict):
        return cls(title=data_dict["title"],
                   genre=data_dict.get("genre"),
                   year=data_dict.get("year"),
                   description=data_dict.get("description"),
                   duration=data_dict.get("duration"))
