document.addEventListener('DOMContentLoaded', function () {
  const searchInput = document.getElementById('searchInput');
  const resultsDiv = document.getElementById('searchResults');
  const originalCards = document.querySelectorAll('.card.blog-card');
  const pageContent = document.getElementById('pageContent');

  if (!searchInput || !resultsDiv) return;

  const searchPath = window.location.pathname.includes('/posts/')
    ? '../search.json'
    : 'search.json';

  fetch(searchPath)
    .then(response => response.json())
    .then(posts => {
      const isLocal =
        window.location.hostname.startsWith('127.') ||
        window.location.hostname === 'localhost' ||
        window.location.hostname.startsWith('192.168.');
      const urlPrefix = isLocal ? '/docs' : '';

      const stopWords = [
        "the", "if", "when", "i", "and", "or", "a", "an", "to", "is", "it", "of", "in", "on", "for", "with"
      ];

      function filterStopWords(query) {
        return query
          .toLowerCase()
          .split(/\s+/)
          .filter(word => !stopWords.includes(word))
          .join(' ');
      }

      searchInput.addEventListener('input', function () {
        const query = this.value.toLowerCase();

        // input listener start

        if (query) {
          const filteredQuery = filterStopWords(query);

          const results = posts.filter(post =>
            post.title.toLowerCase().includes(filteredQuery) ||
            post.excerpt.toLowerCase().includes(filteredQuery) ||
            post.tags.join(',').toLowerCase().includes(filteredQuery)
          );

          if (!filteredQuery.trim()) {
            resultsDiv.innerHTML = '<p style="text-align:center; margin-top:24px; color: #ffffff;">No results found.</p>';
            resultsDiv.classList.add('has-results');
            originalCards.forEach(card => card.style.display = 'none');
            if (pageContent) pageContent.style.display = 'none';
            return;
          }

          if (results.length > 0) {
            resultsDiv.innerHTML = results.map(post => `
      <div class="card blog-card">
        <h2 class="blog-title">${post.title}</h2>
        ${post.image ? `<img src="${post.image}" alt="${post.image_alt || 'Blog image'}" class="card-img">` : ''}
        <div class="card-content">
          <p class="blog-meta">
            <span class="blog-tags">
              ${post.tags.map(tag => `<a href="${urlPrefix}/tag-${tag.toLowerCase()}.html" class="blog-tag">${tag}</a>`).join(' ')}
            </span>
          </p>
          <div class="blog-excerpt">${post.excerpt}</div>
          <a href="${urlPrefix}${post.url}" class="blog-readmore">Read more →</a>
        </div>
      </div>
    `).join('');
            resultsDiv.classList.add('has-results');
          } else {
            resultsDiv.innerHTML = '<p style="text-align:center; margin-top:24px; color: #ffffff;">No results found.</p>';
            resultsDiv.classList.add('has-results');
          }

          originalCards.forEach(card => card.style.display = 'none');
          if (pageContent) pageContent.style.display = 'none';
        } else {
          resultsDiv.innerHTML = '';
          resultsDiv.classList.remove('has-results');
          originalCards.forEach(card => card.style.display = '');
          if (pageContent) pageContent.style.display = '';
        }

        // input listener end

      });
    })
    .catch(err => {
      console.error('Failed to load search.json:', err);
    });
});