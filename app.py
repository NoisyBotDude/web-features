from flask import Flask, render_template, redirect, url_for
from flask import request
from flask import flash
import requests
from weather.weather_cards import cities, current_temperature, status
from weather.weather_cards import wind, humidity, feels_like
from datetime import datetime
from youtube.youtube import Audio, PlayList, Video, Youtube

app = Flask(__name__)
app.config['SECRET_KEY'] = "4c89becdb81a33b40cdc6d5a"

now = datetime.now()
current_time = now.strftime("%H:%M")
today = datetime.today()
current_date = today.strftime("%d-%b-%Y")
current_day = datetime.today().strftime("%A")

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('weather/home.html')

@app.route('/weather', methods=['GET', 'POST'])
def weather_page():
    if request.method == 'POST':
        global city
        city = request.form['city']
        return redirect(url_for('weather_update'))

    else:
        import weather.weather_cards
        return render_template('weather/weather.html', cities=cities,
                        current_temperature=current_temperature,
                        status=status, wind=wind, humidity=humidity,
                        feels_like=feels_like, current_time=current_time)

@app.route('/weather-updates', methods=['GET', 'POST'])
def weather_update():
    api_key = "5d52a94d4dcb8a2a52599d68a443e1f7"
    base_url = "https://api.openweathermap.org/data/2.5/weather?"

    if request.method == 'POST':
        global location
        location = request.form['location']
        complete_url = f"{base_url}appid={api_key}&q={location}"

    else:
        complete_url = f"{base_url}appid={api_key}&q={city}"

    response = requests.get(complete_url)
    json_response = response.json()

    main = json_response['main']
    weather_status = json_response['weather'][0]['main']
    wind_speed = int(json_response['wind']['speed'] * 1.85)

    current_tempcels = int(main['temp'] - 273.15)
    humidity_status = main['humidity']
    feels_like_status = int(main['feels_like'] - 273.15)
    clouds = json_response['clouds']['all']

    if request.method == 'POST':
        return render_template('weather/weather_update.html', current_tempcels=current_tempcels,
                           wind_speed=wind_speed, clouds=clouds,
                           feels_like_status=feels_like_status,
                           humidity_status=humidity_status,
                           weather_status=weather_status,
                           city=location.capitalize(),
                           current_time=current_time,
                           current_date=current_date,
                           current_day=current_day)

    else:
        return render_template('weather/weather_update.html', current_tempcels=current_tempcels,
                           wind_speed=wind_speed, clouds=clouds,
                           feels_like_status=feels_like_status,
                           humidity_status=humidity_status,
                           weather_status=weather_status,
                           city=city.capitalize(),
                           current_time=current_time,
                           current_date=current_date,
                           current_day=current_day)

@app.route('/youtube', methods=['GET', 'POST'])
def youtubeDownload():
    if request.method == "POST":
        video_url = request.form.get('video_url')
        playlist_url = request.form.get('playlist_url')
        youtube = Youtube(video_url)

        if video_url:
            if request.form.get("video_download"):
                video = Video(youtube.url)
                video.downloadVideo()
                flash("Video successfully downloaded")
                return redirect(url_for('youtubeDownload'))

            elif request.form.get("audio_download"):
                audio = Audio(youtube.url)
                audio.downloadAudio()
                flash("Audio successfully downloaded")
                return redirect(url_for('youtubeDownload'))

            else:
                return render_template("youtube/home.html")

        elif not playlist_url == "":
            youtube = Youtube(playlist_url)
            playlist = PlayList(youtube.url)
            playlist.downloadPlaylist()
            flash("Playlist successfully downloaded")
            return redirect(url_for('youtubeDownload'))

        else:
                return render_template("youtube/home.html")

    else:
        return render_template("youtube/home.html")

if __name__ == '__main__':
    app.run(debug=True)

