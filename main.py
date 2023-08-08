import os
from flask import Flask, request, jsonify

app = Flask(__name__)

# Get the sector ID from environment variable or set a default value
sector_id = float(os.environ.get("SECTOR_ID", 123))

def is_valid_coordinate(coord):
    try:
        value = float(coord)
        return value >= 0
    except ValueError:
        return False

@app.route('/dns', methods=['POST'])
def dns_handler():
    data = request.get_json()

    # Validate input coordinates
    if not all(is_valid_coordinate(coord) for coord in [data['x'], data['y'], data['z'], data['vel']]):
        return jsonify({'error': 'Invalid input coordinates'}), 400

    x = float(data['x'])
    y = float(data['y'])
    z = float(data['z'])
    vel = float(data['vel'])

    loc = x * sector_id + y * sector_id + z * sector_id + vel

    response = {'loc': loc}

    return jsonify(response)

if __name__ == '__main__':
    app.run()
