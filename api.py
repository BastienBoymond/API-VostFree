from flask import Flask, jsonify, request
from VostfreeScrapperPy.page import getLastNewsPage, getAnimesByGenreAndPage
from VostfreeScrapperPy.anime import getAnimeById, getAnimeByUrl
from VostfreeScrapperPy.search import getSearchTerm

app = Flask(__name__)

@app.route('/anime/<int:id>', methods=['GET'])
def AnimeById(id):
    return jsonify(getAnimeById(id)) , 200

@app.route('/anime/url', methods=['GET'])
def AnimeByUrl():
    url = request.args.get('url')
    return jsonify(getAnimeByUrl(url)) , 200

@app.route('/anime/search', methods=['GET'])
def AnimeSearch():
    term = request.args.get('term')
    return jsonify(getSearchTerm(term)) , 200

@app.route('/anime/lastnews', methods=['GET'])
def AnimeLastNews():
    return jsonify(getLastNewsPage(1)) , 200

@app.route('/anime/news/<int:page>', methods=['GET'])
def AnimeNews(page):
    return jsonify(getLastNewsPage(page)) , 200

@app.route('/anime/genre/<string:genre>/<int:page>', methods=['GET'])
def AnimeGenre(genre, page):
    return jsonify(getAnimesByGenreAndPage(genre, page)) , 200

app.run(host='0.0.0.0', port=2900)
