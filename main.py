

from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from exa_py import Exa



app = Flask(__name__, static_folder='static')
CORS(app)  # Enable CORS for all routes (optional, but harmless now)
exa = Exa('b78dbb23-5e40-44da-bbf0-b77d5ff62be3')
@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/<path:path>')
def static_proxy(path):
    return send_from_directory(app.static_folder, path)

@app.route('/search', methods=['POST'])
def search():
    data = request.get_json()
    query = data.get('query', '')
    if not query:
        return jsonify({'error': 'No query provided'}), 400
    response = exa.search(query, num_results=10)
    results = [
        {'title': r.title, 'url': r.url}
        for r in response.results
    ]
    return jsonify({'results': results})

if __name__ == '__main__':
    app.run(debug=True)