from flask import Flask, render_template, request, jsonify
import random
import math

app = Flask(__name__)

countries_and_capitals = {
    "Afganistán": {"capital": "Kabul", "coords": [34.5553, 69.2075]},
    "Armenia": {"capital": "Ereván", "coords": [40.1792, 44.4991]},
    "Azerbaiyán": {"capital": "Bakú", "coords": [40.4093, 49.8671]},
    "Baréin": {"capital": "Manama", "coords": [26.2235, 50.5876]},
    "Bangladés": {"capital": "Daca", "coords": [23.8103, 90.4125]},
    "Bután": {"capital": "Timbu", "coords": [27.4728, 89.6390]},
    "Brunéi": {"capital": "Bandar Seri Begawan", "coords": [4.9031, 114.9398]},
    "Camboya": {"capital": "Nom Pen", "coords": [11.5564, 104.9282]},
    "China": {"capital": "Pekín", "coords": [39.9042, 116.4074]},
    "Chipre": {"capital": "Nicosia", "coords": [35.1856, 33.3823]},
    "Georgia": {"capital": "Tiflis", "coords": [41.7151, 44.8271]},
    "India": {"capital": "Nueva Delhi", "coords": [28.6139, 77.2090]},
    "Indonesia": {"capital": "Yakarta", "coords": [6.2088, 106.8456]},
    "Irán": {"capital": "Teherán", "coords": [35.6892, 51.3890]},
    "Irak": {"capital": "Bagdad", "coords": [33.3152, 44.3661]},
    "Israel": {"capital": "Jerusalén", "coords": [31.7683, 35.2137]},
    "Japón": {"capital": "Tokio", "coords": [35.6895, 139.6917]},
    "Jordania": {"capital": "Ammán", "coords": [31.9539, 35.9106]},
    "Kazajistán": {"capital": "Nursultán", "coords": [51.1694, 71.4491]},
    "Kuwait": {"capital": "Ciudad de Kuwait", "coords": [29.3759, 47.9774]},
    "Kirguistán": {"capital": "Biskek", "coords": [42.8746, 74.5698]},
    "Laos": {"capital": "Vientián", "coords": [17.9757, 102.6331]},
    "Líbano": {"capital": "Beirut", "coords": [33.8938, 35.5018]},
    "Malasia": {"capital": "Kuala Lumpur", "coords": [3.1390, 101.6869]},
    "Maldivas": {"capital": "Malé", "coords": [4.1755, 73.5093]},
    "Mongolia": {"capital": "Ulán Bator", "coords": [47.8864, 106.9057]},
    "Birmania": {"capital": "Naipyidó", "coords": [19.7633, 96.0785]},
    "Nepal": {"capital": "Katmandú", "coords": [27.7172, 85.3240]},
    "Corea del Norte": {"capital": "Pionyang", "coords": [39.0392, 125.7625]},
    "Omán": {"capital": "Mascate", "coords": [23.5880, 58.3829]},
    "Pakistán": {"capital": "Islamabad", "coords": [33.6844, 73.0479]},
    "Palestina": {"capital": "Jerusalén Este", "coords": [31.7683, 35.2137]},
    "Filipinas": {"capital": "Manila", "coords": [14.5995, 120.9842]},
    "Catar": {"capital": "Doha", "coords": [25.276987, 51.520008]},
    "Rusia": {"capital": "Moscú", "coords": [55.7558, 37.6173]},
    "Arabia Saudita": {"capital": "Riad", "coords": [24.7136, 46.6753]},
    "Singapur": {"capital": "Singapur", "coords": [1.3521, 103.8198]},
    "Corea del Sur": {"capital": "Seúl", "coords": [37.5665, 126.9780]},
    "Sri Lanka": {"capital": "Sri Jayawardenepura Kotte", "coords": [6.9271, 79.8612]},
    "Siria": {"capital": "Damasco", "coords": [33.5138, 36.2765]},
    "Taiwán": {"capital": "Taipéi", "coords": [25.0330, 121.5654]},
    "Tayikistán": {"capital": "Dusambé", "coords": [38.5598, 68.7870]},
    "Tailandia": {"capital": "Bangkok", "coords": [13.7563, 100.5018]},
    "Timor Oriental": {"capital": "Dili", "coords": [8.5569, 125.5603]},
    "Turquía": {"capital": "Ankara", "coords": [39.9334, 32.8597]},
    "Turkmenistán": {"capital": "Asjabad", "coords": [37.9601, 58.3261]},
    "Emiratos Árabes Unidos": {"capital": "Abu Dabi", "coords": [24.4539, 54.3773]},
    "Uzbekistán": {"capital": "Taskent", "coords": [41.2995, 69.2401]},
    "Vietnam": {"capital": "Hanói", "coords": [21.0285, 105.8542]},
    "Yemen": {"capital": "Saná", "coords": [15.3694, 44.1910]}
}

def is_close(coords1, coords2, tolerance=0.5):
    return math.sqrt((coords1[0] - coords2[0]) ** 2 + (coords1[1] - coords2[1]) ** 2) <= tolerance

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/countries_and_capitals')
def countries_and_capitals_endpoint():
    return jsonify(countries_and_capitals)

@app.route('/start_round')
def start_round():
    questions = random.sample(list(countries_and_capitals.keys()), 15)
    return jsonify(questions)

@app.route('/check_answer', methods=['POST'])
def check_answer():
    data = request.get_json()
    country = data['country']
    capital = data['capital'].strip()
    coords = data['coords']
    correct_name = countries_and_capitals.get(country, {}).get('capital') == capital
    correct_location = is_close(countries_and_capitals.get(country, {}).get('coords'), coords)
    correct = correct_name and correct_location
    return jsonify({"correct": correct, "correct_name": correct_name, "correct_location": correct_location, "capital": countries_and_capitals.get(country, {}).get('capital')})

if __name__ == '__main__':
    app.run(debug=True)
