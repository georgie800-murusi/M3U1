from flask import Flask
import random

app = Flask(__name__)

@app.route("/random_fact")
def random_fact():
    facts_list = [
        "Социальные сети имеют как позитивные, так и негативные стороны, и мы должны быть более осознанными в использовании этих платформ.",
        "Изучение технологической зависимости является одной из наиболее актуальных областей научных исследований в настоящее время.",
        "Один из способов борьбы с технологической зависимостью - это поиск занятий, которые приносят удовольствие и улучшают настроение."
]
    return f'<p>{random.choice(facts_list)}</p>'

@app.route("/coin_flip")
def coin():
    coins = ['Орёл', 'Решка']
    return f'<p>{random.choice(coins)}</p>'

@app.route("/")
def index():
    return f'<h1><a href="/random_fact">Посмотреть случайный факт!</a><h1> <p><a href="/coin_flip">Бросить монетку?<a></p>'

app.run(debug=True)