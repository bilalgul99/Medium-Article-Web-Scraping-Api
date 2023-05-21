import csv
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Load CSV file into memory
csv_file = 'medium_articles_data.csv'
data = []
with open(csv_file, 'r', encoding='utf-8') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        data.append(row)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['GET'])
def search_articles():
    keyword = request.args.get('keyword', '')

    # Search for matching articles
    results = []
    for article in data:
        if keyword.lower() in article['Title'].lower():
            results.append(article)

    return jsonify(results)

if __name__ == '__main__':
    app.run()
