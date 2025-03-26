from flask import Flask, request, jsonify
from recommendation_model import recommend_product  # Importing recommendation logic

app = Flask(__name__)

@app.route('/recommend', methods=['POST'])
def get_recommendation():
    try:
        user_data = request.json  # Get JSON input
        recommendations = recommend_product(user_data)  # Get recommendations
        return jsonify(recommendations)  # Return response as JSON
    except Exception as e:
        return jsonify({"error": str(e)}), 400  # Handle errors gracefully

if __name__ == '__main__':
    app.run(debug=True)
