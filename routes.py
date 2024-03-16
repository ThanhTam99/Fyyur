from flask import render_template, request, redirect, url_for
from models import db, Artists, Venues  
from app import app  

@app.route('/')
def index():
    artists = Artists.query.all()  
    venues = Venues.query.all()  
    return render_template('pages/index.html', artists=artists, venues=venues)  

@app.route('/add_artist', methods=['GET', 'POST'])  
def add_artist():  
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        new_artist = Artists(username=username, email=email)  
        db.session.add(new_artist)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('pages/add_artist.html')  

@app.route('/update_artist/<int:id>', methods=['GET', 'POST'])  
def update_artist(id):  
    artist = Artists.query.get_or_404(id)  
    if request.method == 'POST':
        artist.username = request.form['username']
        artist.email = request.form['email']
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('pages/update_artist.html', artist=artist)  

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
    return render_template('pages/add_venue.html')

@app.route('/update_venue/<int:id>', methods=['GET', 'POST'])  
def update_venue(id):
    venue = Venues.query.get_or_404(id)
    if request.method == 'POST':
        venue.username = request.form['username']
        venue.email = request.form['email']
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('pages/update_venue.html', venue=venue)

@app.route('/delete_venue/<int:id>', methods=['GET', 'POST'])  
def delete_venue(id):
    venue = Venues.query.get_or_404(id)
    db.session.delete(venue)
    db.session.commit()
    return redirect(url_for('index'))
