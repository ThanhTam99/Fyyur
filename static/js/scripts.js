document.addEventListener("DOMContentLoaded", function () {
    if (sessionStorage.getItem("formTitle")) {
        document.getElementById("form-title").textContent = sessionStorage.getItem("formTitle");
    }
    if (sessionStorage.getItem("submitButton")) {
        document.getElementById("submit-button").textContent = sessionStorage.getItem("submitButton");
    }

    // Xử lý khi hàng trong bảng được click
    document.querySelectorAll("#shows-table tbody tr").forEach(function (row) {
        row.addEventListener("click", function () {
            sessionStorage.setItem("formTitle", "Update Show");
            sessionStorage.setItem("submitButton", "Update Show");
            // Xóa highlight ở tất cả các hàng
            document.querySelectorAll("#shows-table tbody tr").forEach(r => r.classList.remove("highlight"));
            // Thêm highlight vào hàng hiện tại
            this.classList.add("highlight");

            // Lấy dữ liệu từ data-* attributes
            const showId = this.getAttribute("data-show-id");
            const artistId = this.getAttribute("data-artist-id");
            const venueId = this.getAttribute("data-venue-id");
            const startTime = this.getAttribute("data-start-time");
            const endTime = this.getAttribute("data-end-time");
            const ticketPrice = this.getAttribute("data-ticket-price");

            // Điền thông tin vào form
            document.getElementById("artist_id").value = artistId;
            document.getElementById("venue_id").value = venueId;
            document.getElementById("start_time").value = startTime;
            document.getElementById("end_time").value = endTime;
            document.getElementById("ticket_price").value = ticketPrice;

            // Cập nhật form action, tiêu đề form và text của nút submit
            const form = document.getElementById("show-form");
            form.action = `/edit_show/${showId}`;
            document.getElementById("form-title").textContent = 'Update Show'; // Cập nhật tiêu đề form
            document.getElementById("submit-button").textContent = 'Update Show'; // Cập nhật text của nút
        });
    });

    // Xử lý khi nút "Add New Show" được click
    document.getElementById("clear-show").addEventListener("click", function () {
        sessionStorage.setItem("formTitle", "Add New Show");
        sessionStorage.setItem("submitButton", "Add Show");
        // Xóa highlight và reset form
        document.querySelectorAll("#shows-table tbody tr").forEach(r => r.classList.remove("highlight"));
        document.getElementById("artist_id").selectedIndex = 0;
        document.getElementById("venue_id").selectedIndex = 0;
        document.getElementById("start_time").value = '';
        document.getElementById("end_time").value = '';
        document.getElementById("ticket_price").value = '';

        // Đặt lại action cho form và cập nhật tiêu đề và text của nút
        const form = document.getElementById("show-form");
        form.action = "{{ url_for('add_show') }}";
        console.log(document.getElementById("form-title"));
        console.log(document.getElementById("submit-button"));
        document.getElementById("form-title").textContent = 'Add Show'; // Đặt lại tiêu đề form
        document.getElementById("submit-button").textContent = 'Add Show'; // Đặt lại text của nút
    });
});