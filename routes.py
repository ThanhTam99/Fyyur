from models.artists import Artists
from models.venues import Venues
from models.shows import Shows
from models import db
from flask import render_template, request, redirect, url_for
from datetime import datetime
from math import ceil

def init_app(app):
    @app.route("/")
    def index():
        artists = Artists.query.all()
        venues = Venues.query.all()
        shows = Shows.query.all()

        for show_entry in shows:
            artist = Artists.query.get(show_entry.artist_id)
            venue = Venues.query.get(show_entry.venue_id)
            show_entry.artist_name = artist.name if artist else "Unknown Artist"
            show_entry.venue_name = venue.name if venue else "Unknown Venue"

        total_shows = len(shows)
        items_per_page = 5
        total_pages = ceil(total_shows / items_per_page)
        page = request.args.get("page", 1, type=int)
        shows_on_page = shows[(page - 1) * items_per_page : page * items_per_page]

        return render_template(
            "pages/index.html",
            artists=artists,
            venues=venues,
            shows=shows_on_page,
            total_pages=total_pages,
            page=page,
        )

    @app.route("/add_entry", methods=["GET", "POST"])
    def add_entry():
        entry_type = request.args.get("entry_type")
        if request.method == "POST":
            if entry_type == "artist":
                name = request.form.get("name")
                genre = request.form.get("genre")
                website = request.form.get("website")
                bio = request.form.get("bio")
                new_entry = Artists(name=name, genre=genre, website=website, bio=bio)
            elif entry_type == "venue":
                name = request.form.get("name")
                city = request.form.get("city")
                address = request.form.get("address")
                capacity = request.form.get("capacity")
                new_entry = Venues(
                    name=name, city=city, address=address, capacity=capacity
                )
            else:
                return redirect(url_for("index"))

            db.session.add(new_entry)
            db.session.commit()
            return redirect(url_for("index"))
        else:
            return render_template("pages/add_entry.html", entry_type=entry_type)

    @app.route("/add_show", methods=["POST"])
    def add_show():
        artist_id = request.form["artist_id"]
        venue_id = request.form["venue_id"]
        start_time = datetime.strptime(request.form["start_time"], "%Y-%m-%dT%H:%M")
        end_time = datetime.strptime(request.form["end_time"], "%Y-%m-%dT%H:%M")
        ticket_price = request.form["ticket_price"]

        new_show = Shows(
            artist_id=artist_id,
            venue_id=venue_id,
            start_time=start_time,
            end_time=end_time,
            ticket_price=ticket_price,
        )
        db.session.add(new_show)
        db.session.commit()
        return redirect(url_for("index"))

    @app.route("/delete/<entry_type>/<int:id>", methods=["POST"])
    def delete_entry(entry_type, id):
        if entry_type == "artist":
            entry = Artists.query.get_or_404(id)
        elif entry_type == "venue":
            entry = Venues.query.get_or_404(id)
        elif entry_type == "show":
            entry = Shows.query.get_or_404(id)
        else:
            return redirect(url_for("index"))
        db.session.delete(entry)
        db.session.commit()

        return redirect(url_for("index"))
