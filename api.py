from flask import Flask, jsonify
import json  # j

app = Flask(__name__)

@app.route('/products', methods=['GET'])
def get_products():
    try:
        with open('products.json', 'r') as file:
            products = json.load(file)
        return jsonify(products)
    except FileNotFoundError:
        return jsonify({"error": "Products file not found."}), 404

if __name__ == '__main__':
    app.run(debug=True)
