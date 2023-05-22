from flask import Flask, request
import pandas as pd

app = Flask(__name__)

# Load the CSV file into a pandas DataFrame
df = pd.read_csv('your_csv_file.csv')

@app.route('/search')
def search():
    # Get the search query from the request parameters
    query = request.args.get('q')

    # Filter the DataFrame based on the search query
    filtered_df = df[df['Title'].str.contains(query)]

    # Convert the filtered DataFrame to a JSON object
    json_result = filtered_df.to_json(orient='records')

    # Return the JSON object as the API response
    return json_result

if __name__ == '__main__':
    app.run()
