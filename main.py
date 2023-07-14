from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/dns", methods=['POST'])
def dns_handler():
    data = request.get_json()

    x = float(data['x'])
    y = float(data['y'])
    z = float(data['z'])
    vel = float(data['vel'])
    sector_id = 1 #replace with your constant SectorID

    loc = (x*sector_id + y*sector_id + z*sector_id) + vel

    response = {
        'loc' : loc
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run()

