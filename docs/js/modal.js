// Modal open/close logic
document.addEventListener('DOMContentLoaded', function () {
    var modal = document.getElementById("myModal");
    var btn = document.getElementById("contact-link");
    var span = document.getElementsByClassName("close")[0];

    // Open modal on "Contact" click
    if (btn) {
        btn.onclick = function (e) {
            e.preventDefault();
            modal.style.display = "block";
        };
    }

    // Close modal on × click
    if (span) {
        span.onclick = function () {
            modal.style.display = "none";
        };
    }

    // Close modal when clicking outside of modal content
    window.onclick = function (event) {
        if (event.target == modal) {
            modal.style.display = "none";
        }
    };
});