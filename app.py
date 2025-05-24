from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

# Храним последнее местоположение
last_location = {'lat': 55.751244, 'lon': 37.618423}  # Москва по умолчанию

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', lat=last_location['lat'], lon=last_location['lon'])

@app.route('/update_location', methods=['POST'])
def update_location():
    data = request.get_json()
    last_location['lat'] = data.get('lat', last_location['lat'])
    last_location['lon'] = data.get('lon', last_location['lon'])
    return jsonify({'status': 'ok'})

@app.route('/location', methods=['GET'])
def get_location():
    return jsonify(last_location)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000) 