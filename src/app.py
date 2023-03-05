#!flask/bin/python
from flask import Flask, request, jsonify, abort
from storageutils import MySQLManager
from config import CONFIG

app = Flask(__name__)


# display movies by genre

def searchmoviebygenre(genre):
    query = "select title from Movie526 where genre=genre;"
    res = []
    try:
        res = MySQLManager.execute_query(
            query, None, **CONFIG['database']['gnits'])
    except Exception as error:
        print(error)
    return res


@app.route('/api/moviebygenre', methods=['GET', 'POST'])
def searchmoviegenre():
    if request.method == 'GET':
        return "Inside search by Genre"
    else:
        """
        input: 1.insert query
        {
            'movie_id:"sample",
            'title':"when in rome"
            'genre':'comedy',
            'director':'megan fox',
            'release_date':'1999-12-12'
        }
        """
        input_json = request.json
        # movie_id = input_json.get('movie_id', 0)
        # title = input_json.get('title', "")
        genre = input_json.get('genre', "")
        # director = input_json.get('director', "")
        # release_date = input_json.get('release_date', "")
        res = searchmoviebygenre(genre)
        return jsonify(res)


# movie details by genre

def searchmovie(inputtitle):
    query = "select genre,director,release_date from Movie526 where title=inputtitle limit 1;"
    res = []
    try:
        res = MySQLManager.execute_query(
            query, None, **CONFIG['database']['gnits'])
    except Exception as error:
        print(error)
    return res


@app.route('/api/moviedetails', methods=['GET', 'POST'])
def moviedetails():
    if request.method == 'GET':
        return "I'm Alive"
    else:
        """
        input: 1.insert query
        {
            'movie_id:"sample",
            'title':"when in rome"
            'genre':'comedy',
            'director':'megan fox',
            'release_date':'1999-12-12'
        }
        """
        input_json = request.json
        # movie_id = input_json.get('movie_id', 0)
        title = input_json.get('title', "")
        # genre = input_json.get('genre', "")
        # director = input_json.get('director', "")
        # release_date = input_json.get('release_date', "")
        res = searchmovie(title)
        return jsonify(res)


# insertion into database


def insert_data(movie_id, title, genre, director, release_date):
    query = 'insert into Movie526 values("{}","{}","{}","{}","{}");'.format(
        movie_id, title, genre, director, release_date)
    status = 'failed'
    try:
        res = MySQLManager.execute_query(
            query, None, **CONFIG['database']['gnits'])
        status = 'successful'
    except Exception as error:
        print(error)
    return status


@app.route('/api/moviedatabase', methods=['GET', 'POST'])
def mymoviedatabase():
    if request.method == 'GET':
        return "I'm Alive"
    else:
        """
        input: 1.insert query
        {
            'movie_id:"sample",
            'title':"when in rome"
            'genre':'comedy',
            'director':'megan fox',
            'release_date':'1999-12-12'
        }
        """
        input_json = request.json
        movie_id = input_json.get('movie_id', 0)
        title = input_json.get('title', "")
        genre = input_json.get('genre', "")
        director = input_json.get('director', "")
        release_date = input_json.get('release_date', "")
        res = insert_data(movie_id, title, genre, director, release_date)
        return jsonify(res)


if __name__ == '__main__':
    app.run("0.0.0.0", port=8309)
