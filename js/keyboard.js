document.addEventListener('DOMContentLoaded', () => {
  const prevLink = document.querySelector('.previous-container')?.closest('a');
  const nextLink = document.querySelector('.next-container')?.closest('a');
  const modal = document.getElementById('myModal');

  document.addEventListener('keydown', (e) => {
    // Prevent keyboard navigation if modal is visible
    if (modal && window.getComputedStyle(modal).display !== 'none') return;

    if (e.key === 'ArrowLeft' && prevLink) {
      window.location.href = prevLink.href;
    } else if (e.key === 'ArrowRight' && nextLink) {
      window.location.href = nextLink.href;
    }
  });
});