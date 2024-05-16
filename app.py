from flask import Flask, render_template, request, jsonify
import folium

app = Flask(__name__)

countries_and_capitals = {
    "Afganistán": "Kabul",
    "Armenia": "Ereván",
    "Azerbaiyán": "Bakú",
    "Baréin": "Manama",
    "Bangladés": "Daca",
    "Bután": "Timbu",
    "Brunéi": "Bandar Seri Begawan",
    "Camboya": "Nom Pen",
    "China": "Pekín",
    "Chipre": "Nicosia",
    "Georgia": "Tiflis",
    "India": "Nueva Delhi",
    "Indonesia": "Yakarta",
    "Irán": "Teherán",
    "Irak": "Bagdad",
    "Israel": "Jerusalén",
    "Japón": "Tokio",
    "Jordania": "Ammán",
    "Kazajistán": "Nursultán",
    "Kuwait": "Ciudad de Kuwait",
    "Kirguistán": "Biskek",
    "Laos": "Vientián",
    "Líbano": "Beirut",
    "Malasia": "Kuala Lumpur",
    "Maldivas": "Malé",
    "Mongolia": "Ulán Bator",
    "Birmania": "Naipyidó",
    "Nepal": "Katmandú",
    "Corea del Norte": "Pionyang",
    "Omán": "Mascate",
    "Pakistán": "Islamabad",
    "Palestina": "Jerusalén Este",
    "Filipinas": "Manila",
    "Catar": "Doha",
    "Rusia": "Moscú",
    "Arabia Saudita": "Riad",
    "Singapur": "Singapur",
    "Corea del Sur": "Seúl",
    "Sri Lanka": "Sri Jayawardenepura Kotte",
    "Siria": "Damasco",
    "Taiwán": "Taipéi",
    "Tayikistán": "Dusambé",
    "Tailandia": "Bangkok",
    "Timor Oriental": "Dili",
    "Turquía": "Ankara",
    "Turkmenistán": "Asjabad",
    "Emiratos Árabes Unidos": "Abu Dabi",
    "Uzbekistán": "Taskent",
    "Vietnam": "Hanói",
    "Yemen": "Saná"
}

@app.route('/')
def index():
    return render_template('index.html', countries=list(countries_and_capitals.keys()))

@app.route('/check', methods=['POST'])
def check():
    data = request.get_json()
    country = data['country']
    capital = data['capital'].strip()
    correct = countries_and_capitals.get(country) == capital
    return jsonify({"correct": correct, "capital": countries_and_capitals.get(country)})

@app.route('/map')
def create_map():
    m = folium.Map(location=[34.0479, 100.6197], zoom_start=4)
    for country, capital in countries_and_capitals.items():
        folium.Marker(location=[34.0479, 100.6197], popup=f"{country}: {capital}").add_to(m)
    m.save("templates/asia_map.html")
    return render_template('asia_map.html')

if __name__ == '__main__':
    app.run(debug=True)

