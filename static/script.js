document.getElementById('searchForm').addEventListener('submit', async function(e) {
    e.preventDefault();
    const query = document.getElementById('query').value;
    const resultsDiv = document.getElementById('results');
    resultsDiv.innerHTML = '<p>Searching...</p>';
    try {
        const response = await fetch('/search', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ query })
        });
        const data = await response.json();
        if (data.results && data.results.length > 0) {
            resultsDiv.innerHTML = data.results.map(r => `
                <div class="result">
                    <a href="${r.url}" class="result-title" target="_blank">${r.title}</a>
                </div>
            `).join('');
        } else {
            resultsDiv.innerHTML = '<p>No results found.</p>';
        }
    } catch (err) {
        resultsDiv.innerHTML = '<p>Error fetching results.</p>';
    }
});
