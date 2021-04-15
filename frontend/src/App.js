import './App.css';
import Chessboard from "chessboardjsx";
import { ChessInstance } from "chess.js";
import axios from "axios"
import React, { Component } from 'react'

const Chess = require("chess.js");

export default class PersonList extends Component {
  state = {
    persons: []
  }

  componentDidMount() {
    // const api = 'https://nzv8s9m7vk.execute-api.eu-west-1.amazonaws.com/staging';
    // const data = { "name" : "Mike" };
    // axios
    //   .post(api, data)
    //   .then((response) => {
    //     console.log(response);
    //   })
    //   .catch((error) => {
    //     console.log(error);
    //   });
    // }
  }

  render() {
    const chess = new Chess("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1")
    let fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
    const handleMove = (move) => {
      chess.move(move)
      fen = chess.fen
    }
    return (
      <div className="App">
         <Chessboard
          width={400}
          position="rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
          onDrop={(move) =>
            handleMove({
              from: move.sourceSquare,
              to: move.targetSquare,
              promotion: "q",
            })
          }
        />
      </div>
    );
  }
}
