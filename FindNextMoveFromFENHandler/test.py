#!/usr/bin/env python3

from stockfish import Stockfish

stockfish = Stockfish("stockfish")
stockfish.set_fen_position("rnbqkbnr/pppp1ppp/4p3/8/4P3/8/PPPP1PPP/RNBQKBNR w KQkq - 0 2")
stockfish.get_best_move()
print(stockfish.get_board_visual())