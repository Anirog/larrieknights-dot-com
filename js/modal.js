// Modal open/close logic
document.addEventListener('DOMContentLoaded', function () {
    var modal = document.getElementById("myModal");
    var btn = document.getElementById("contact-link");
    var span = document.getElementsByClassName("close")[0];

    // Open modal
    if (btn) {
        btn.onclick = function (e) {
            e.preventDefault();
            modal.style.display = "block";
        };
    }

    // Close modal on X
    if (span) {
        span.onclick = function () {
            modal.style.display = "none";
        };
    }

    // Close modal if user clicks outside modal content
    window.onclick = function (event) {
        if (event.target == modal) {
            modal.style.display = "none";
        }
    };

    // ---- TOAST CODE ----
    function showToast(message) {
        var toast = document.getElementById("toast");
        if (!toast) return;
        toast.innerText = message;
        toast.className = "toast show";
        setTimeout(function () {
            toast.className = "toast";
        }, 3500);
    }

    // AJAX Form submission for contact form
    var form = document.querySelector('.modal form');
    if (form) {
        form.addEventListener('submit', function (e) {
            e.preventDefault();

            var formData = new FormData(form);

            fetch(form.action, {
                method: 'POST',
                body: formData,
                headers: {
                    'Accept': 'application/json'
                }
            }).then(function (response) {
                if (response.ok) {
                    showToast("Thank you! Your message has been sent.");
                    form.reset();
                    setTimeout(function () {
                        modal.style.display = "none";
                    }, 1700);
                } else {
                    showToast("Sorry, there was a problem sending your message.");
                }
            }).catch(function (error) {
                showToast("Sorry, there was a problem sending your message.");
            });
        });
    }
});