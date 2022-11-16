from flask import flask ,jsonify,request
import csv

all_movie = []
with open("Movie.csv") as f:
    reader = csv.reader(f)
    data = list(reader)
    all_movie = data[1:]

liked_movie = []
unliked_movie = []
not_watched = []

app = Flask(__name__)

@app.route("/get-movie")
def get_movie():
    return jsonify({
        "data": all_movie[0],
        "status": "sucess"
    })

@app.route("/liked-movie",methods = ["POST"])
def liked_movie():
    movie = all_movie[0]
    all_movie = all_movie[1:]
    liked_movie.append(movie)
    return jsonify({
        "status": "sucess"
    }),201

@app.route("/unliked-movie",methods = ["POST"])
def unliked_movie():
    movie = all_movie[0]
    all_movie = all_movie[1:]
    unliked_movie.append(movie)
    return jsonify({
        "status": "sucess"
    }),201

@app.route("/not-watch-movie",methods = ["POST"])
def not_watched_movie():
    movie = all_movie[0]
    all_movie = all_movie[1:]
    not_watched_movie.append(movie)
    return jsonify({
        "status": "sucess"
    }),201



if __name__ == "__main__":
    app.run()