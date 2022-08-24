
# TODO: connect to a local postgresql database
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

#----------------------------------------------------------------------------#
# Models.
#----------------------------------------------------------------------------#

venue_genre = db.Table('venue_genre', 
                      db.Column('genre_id', db.Integer, db.ForeignKey('genres.id', ondelete="CASCADE")),
                      db.Column('venue_id', db.Integer, db.ForeignKey('venues.id', ondelete="CASCADE"))
                      )

class Genre(db.Model):
      __tablename__ = 'genres'

      id = db.Column(db.Integer, primary_key=True)
      name = db.Column(db.String(100))

      def __repr__(self) -> str:
             return f'<Genre {self.id} {self.name}>'
class Venue(db.Model):
    __tablename__ = 'venues'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    genres = db.Column(db.String(120))
    address = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    image_link = db.Column(db.String(500), nullable=True, default="https://images.unsplash.com/photo-1497032205916-ac775f0649ae?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=750&q=80")
    facebook_link = db.Column(db.String(120), nullable=True, default="")
    website = db.Column(db.String(120), nullable=True, default="")
    genres = db.relationship('Genre', secondary=venue_genre, backref='venues')
    shows = db.relationship('Show', backref='venues')

    def __repr__(self) -> str:
           return f'<Venue: {self.id} {self.name}>'

    # TODO: implement any missing fields, as a database migration using Flask-Migrate

artist_show = db.Table('artist_show',
                      db.Column('artist_id', db.Integer, db.ForeignKey('artists.id')),
                      db.Column('show_id', db.Integer, db.ForeignKey('shows.id', ondelete="CASCADE"))
                      )

class Artist(db.Model):
    __tablename__ = 'artists'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    genres = db.Column(db.String(120))
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))


    # TODO: implement any missing fields, as a database migration using Flask-Migrate

# TODO Implement Show and Artist models, and complete all model relationships and properties, as a database migration.

class Show(db.Model):
      __tablename__ = 'shows'

      id = db.Column(db.Integer, primary_key=True)
      date = db.Column(db.DateTime, nullable=False)
      image_link = db.Column(db.String(500))
      artists = db.relationship('Artist', secondary=artist_show, backref='shows')
      venue_id = db.Column(db.Integer, db.ForeignKey('venues.id', ondelete="CASCADE"))