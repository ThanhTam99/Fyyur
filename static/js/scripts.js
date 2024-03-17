document.addEventListener("DOMContentLoaded", function () {
    document.querySelectorAll("#shows-table tbody tr").forEach(function (row) {
        row.addEventListener("click", function () {

            document.querySelectorAll("#shows-table tbody tr").forEach(r => r.classList.remove("highlight"));

            this.classList.add("highlight");

            const showId = this.getAttribute("data-show-id");
            const artistId = this.getAttribute("data-artist-id");
            const venueId = this.getAttribute("data-venue-id");
            const startTime = this.getAttribute("data-start-time");
            const endTime = this.getAttribute("data-end-time");
            const ticketPrice = this.getAttribute("data-ticket-price");


            document.getElementById("artist_id").value = artistId;
            document.getElementById("venue_id").value = venueId;
            document.getElementById("start_time").value = startTime;
            document.getElementById("end_time").value = endTime;
            document.getElementById("ticket_price").value = ticketPrice;


            const form = document.getElementById("show-form");
            form.action = `/edit_show/${showId}`;
            document.getElementById("form-title").textContent = 'Edit Show';
            document.getElementById("submit-button").textContent = 'Update';
        });
    });


    document.getElementById("clear-show").addEventListener("click", function () {
        
        document.querySelectorAll("#shows-table tbody tr").forEach(r => r.classList.remove("highlight"));
        document.getElementById("artist_id").selectedIndex = 0;
        document.getElementById("venue_id").selectedIndex = 0;
        document.getElementById("start_time").value = '';
        document.getElementById("end_time").value = ''; 
        document.getElementById("ticket_price").value = '';

        const form = document.getElementById("show-form");
        form.action = "{{ url_for('add_show') }}";
        document.getElementById("form-title").textContent = 'Add Show';
        document.getElementById("submit-button").textContent = 'Create';
    });
});