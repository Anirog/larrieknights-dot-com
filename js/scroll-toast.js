    window.addEventListener('DOMContentLoaded', function () {
      const toast = document.getElementById('scroll-toast');
      // Only show if the user hasn't seen it before
      if (!localStorage.getItem('scrollToastSeen')) {
        toast.style.display = 'block';
        setTimeout(() => toast.classList.add('show'), 100); // Animate in

        function hideToast() {
          toast.classList.remove('show');
          setTimeout(() => toast.style.display = 'none', 400); // Hide after fade out
          localStorage.setItem('scrollToastSeen', 'yes');
          window.removeEventListener('scroll', hideToast);
          window.removeEventListener('touchmove', hideToast);
        }

        window.addEventListener('scroll', hideToast);
        window.addEventListener('touchmove', hideToast);
        // Or hide after 4 seconds if user doesn't scroll
        setTimeout(hideToast, 4000);
      }
    });