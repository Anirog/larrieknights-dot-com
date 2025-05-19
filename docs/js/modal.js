// modal.js

document.addEventListener('DOMContentLoaded', function () {
  var modal = document.getElementById('myModal');
  var contactLink = document.getElementById('contact-link');
  var closeBtn = document.querySelector('.modal .close');

  // Open modal on nav link click
  if (contactLink) {
    contactLink.addEventListener('click', function (e) {
      e.preventDefault();
      modal.classList.add('open');

      // If mobile menu is open, close it
      var navToggle = document.getElementById('nav-toggle');
      if (navToggle && navToggle.checked) navToggle.checked = false;
    });
  }

  // Close modal on X click
  if (closeBtn) {
    closeBtn.addEventListener('click', function () {
      modal.classList.remove('open');
    });
  }

  // Close modal when clicking outside the modal content
  window.addEventListener('click', function (event) {
    if (event.target === modal) {
      modal.classList.remove('open');
    }
  });

  // Optional: close modal with Escape key
  window.addEventListener('keydown', function (event) {
    if (event.key === "Escape") {
      modal.classList.remove('open');
    }
  });
});