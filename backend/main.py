import json
import os
from stockfish import Stockfish
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/")
@cross_origin()
def home():
    return "Hello, World!"

@app.route('/stockfishmove', methods=['POST'])
@cross_origin() 
def next_move():
    stockfish = Stockfish()
    data = request.json
    user_id = data['user_id']
    current_fen = data['fen']

    stockfish.set_elo_rating(1350)
    stockfish.set_fen_position(current_fen)

    best_move = stockfish.get_best_move()

    return jsonify({
        'user_id': f"{user_id}",
        'best_move': f"{best_move}"
    })

if __name__ == "__main__":
    app.run(debug=True)


