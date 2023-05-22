#https://colab.research.google.com/drive/1CEeS2rjK00jspuxPCpvZoEM3XQBe31PM?usp=sharing
#for API search got to http://bilalgul.pythonanywhere.com/
#to make API request for a json response http://bilalgul.pythonanywhere.com/search?keyword=<your_keywrord>
#code found at https://github.com/bilalgul99/Medium-Article-Web-Scraping-Api
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
