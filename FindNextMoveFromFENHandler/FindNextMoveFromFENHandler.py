import json
import os
from stockfish import Stockfish

stockfish = Stockfish("stockfish_13_linux_x64_bmi2/stockfish_13_linux_x64_bmi2")
def lambda_handler(event, context):
    user_id = event['user_id']
    current_fen = event['fen']

    stockfish.set_elo_rating(os.environ['elo'])
    stockfish.set_fen_position(current_fen)

    best_move = stockfish.get_best_move()
    return {
        'user_id': f"{user_id}",
        'best_move': f"{best_move}"
        }