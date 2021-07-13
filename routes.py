from flask import Flask, render_template
import requests
from weather_cards import city1, current_tempcels1

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/weather')
def weather_page():
    import weather_cards
    return render_template('weather.html', city1=city1, current_temperature1=current_tempcels1)

@app.route('/weather-updates', methods=['GET', 'POST'])
def weather_update():
           return render_template('weather_update.html')

if __name__ == '__main__':
    app.run(debug=True)

