from flask import Flask, render_template, url_for, redirect, request, session, flash
import requests
import json 

app = Flask(__name__)

@app.route('/')
def hello():
    return 'WELCOME to RAPIDAPI'

@app.route('/league')
def league():
	url = "https://premier-league-standings1.p.rapidapi.com/"

	headers = {
		"X-RapidAPI-Key": "d3df6dc15bmsh342cb4697f76e33p1ee0f0jsn045f39f9f64b",
		"X-RapidAPI-Host": "premier-league-standings1.p.rapidapi.com"
	}

	response = requests.get(url, headers=headers)
	jsontext = json.loads(response.text)

	# get the club name 
	teams = [i['team']['name'] for i in jsontext]

	# get wins, losses, gamesPlayed, points and rank
	wins = [i['stats']['wins'] for i in jsontext]
	losses = [i['stats']['losses'] for i in jsontext]
	gamesPlayed = [i['stats']['gamesPlayed'] for i in jsontext]
	points = [i['stats']['points'] for i in jsontext]
	ranks = [i['stats']['rank'] for i in jsontext]

	stats = zip(ranks,teams, wins, losses, gamesPlayed, points)
	return render_template('league.html', stats=stats)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='50', debug=True)
