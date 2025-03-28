from flask import Flask, request, jsonify

app = Flask(__name__)

# Function to convert km to miles
def km_to_miles(km):
    return km * 0.621371

@app.route('/convert', methods=['POST'])
def convert():
    data = request.get_json()
    km = data.get('km')

    if km is None:
        return jsonify({"error": "Invalid input"}), 400

    miles = km_to_miles(km)
    return jsonify({"km": km, "miles": miles})

if __name__ == '__main__':
    app.run(debug=True)
