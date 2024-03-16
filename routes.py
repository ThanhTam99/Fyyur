from models.artists import Artists
from models.venues import Venues
from models.shows import Shows
from models import db
from flask import render_template, request, redirect, url_for

def init_app(app):
    @app.route('/')
    def index():
        artists = Artists.query.all()
        venues = Venues.query.all()
        shows = Shows.query.all()
        return render_template('pages/index.html', artists=artists, venues=venues, shows=shows)

    @app.route('/add_artist', methods=['GET', 'POST'])
    def add_artist():
        if request.method == 'POST':
            username = request.form['username']
            email = request.form['email']
            new_artist = Artists(username=username, email=email)
            db.session.add(new_artist)
            db.session.commit()
            return redirect(url_for('index'))
        return render_template('pages/artists/add_artist.html')

    @app.route('/update_artist/<int:id>', methods=['GET', 'POST'])
    def update_artist(id):
        artist = Artists.query.get_or_404(id)
        if request.method == 'POST':
            artist.username = request.form['username']
            artist.email = request.form['email']
            db.session.commit()
            return redirect(url_for('index'))
        return render_template('pages/artists/update_artist.html', artist=artist)

    @app.route('/delete_artist/<int:id>', methods=['GET', 'POST'])
    def delete_artist(id):
        artist = Artists.query.get_or_404(id)
        db.session.delete(artist)
        db.session.commit()
        return redirect(url_for('index'))

    @app.route('/add_venue', methods=['GET', 'POST'])
    def add_venue():
        if request.method == 'POST':
            username = request.form['username']
            email = request.form['email']
            new_venue = Venues(username=username, email=email)
            db.session.add(new_venue)
            db.session.commit()
            return redirect(url_for('index'))
        return render_template('pages/venues/add_venue.html')

    @app.route('/update_venue/<int:id>', methods=['GET', 'POST'])
    def update_venue(id):
        venue = Venues.query.get_or_404(id)
        if request.method == 'POST':
            venue.username = request.form['username']
            venue.email = request.form['email']
            db.session.commit()
            return redirect(url_for('index'))
        return render_template('pages/venues/update_venue.html', venue=venue)

    @app.route('/delete_venue/<int:id>', methods=['GET', 'POST'])
    def delete_venue(id):
        venue = Venues.query.get_or_404(id)
        db.session.delete(venue)
        db.session.commit()
        return redirect(url_for('index'))

    @app.route('/add_show', methods=['GET', 'POST'])
    def add_show():
        if request.method == 'POST':
            artist_id = request.form['artist_id']
            venue_id = request.form['venue_id']
            start_time = request.form['start_time']
            end_time = request.form['end_time']
            ticket_price = request.form['ticket_price']

            new_show = Shows(artist_id=artist_id, venue_id=venue_id, start_time=start_time, end_time=end_time, ticket_price=ticket_price)
            db.session.add(new_show)
            db.session.commit()
            return redirect(url_for('index'))
        artists = Artists.query.all()
        venues = Venues.query.all()
        return render_template('pages/shows/add_show.html', artists=artists, venues=venues)

    @app.route('/update_show/<int:id>', methods=['GET', 'POST'])
    def update_show(id):
        show = Shows.query.get_or_404(id)
        if request.method == 'POST':
            show.artist_id = request.form['artist_id']
            show.venue_id = request.form['venue_id']
            show.start_time = request.form['start_time']
            show.end_time = request.form['end_time']
            show.ticket_price = request.form['ticket_price']
            db.session.commit()
            return redirect(url_for('index'))
        artists = Artists.query.all()
        venues = Venues.query.all()
        return render_template('pages/shows/update_show.html', show=show, artists=artists, venues=venues)

    @app.route('/delete_show/<int:id>', methods=['GET', 'POST'])
    def delete_show(id):
        show = Shows.query.get_or_404(id)
        db.session.delete(show)
        db.session.commit()
        return redirect(url_for('index'))
