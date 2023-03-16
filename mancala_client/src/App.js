import { Dialog, DialogTitle, DialogContent, } from "@mui/material";
import { useEffect, useState } from "react";
import "./App.css";
import Pit from "./components/Pit";
import Store from "./components/Store";
import { api } from "./services/api";

function App() {
  const [isOpen, setIsOpen] = useState(false);
  const [rules, setRules] = useState([]);
  const [showRuleDialog, setShowRuleDialog] = useState(false);
  const handleOpen = () => {
    setIsOpen(true);
  };

  const handleClose = () => {
    setIsOpen(false);
    setGameStarted(false);
    fetchData();
  };

  const handleCloseRuleDialog = () => {
    setShowRuleDialog(false);
  };

  const [gameID, setGameID] = useState(null);
  const [board, setBoard] = useState([]);
  const [gameOver, setGameOver] = useState(null);
  const [message, setMessage] = useState("");
  const [player1, setPlayer1] = useState("");
  const [player1Score, setPlayer1Score] = useState(0);
  const [player2, setPlayer2] = useState("");
  const [player2Score, setPlayer2Score] = useState(0);
  const [playerTurn, setPlayerTurn] = useState(0);
  const [winner, setWinner] = useState("");
  const [gameStarted, setGameStarted] = useState(false);

  const map = {
    0: 13,
    1: 12,
    2: 11,
    3: 10,
    4: 9,
    5: 8,
    6: 7,
    7: 0,
    8: 1,
    9: 2,
    10: 3,
    11: 4,
    12: 5,
    13: 6,
  };

  const dialogStyle = {
    backgroundColor: '#282c34',
    color: 'white',
    borderRadius: '8px',
  };

  function renderBoard(board) {
    return board.map((element, index) => {
      if (index === 0) {
        return (
          <div key={index} className="grid-item grid-item--first-column">
            <Store numberOfStones={board[map[index]]}></Store>
          </div>
        );
      } else if (index === 13) {
        return (
          <div key={index} className="grid-item grid-item--last-column">
            <Store numberOfStones={board[map[index]]}></Store>
          </div>
        );
      } else {
        if (playerTurn === 0) {
          if (index >= 7 && index <= 12) {
            return (
              <div key={index} className="grid-item">
                <Pit
                  makeMove={makeMove}
                  gameID={gameID}
                  pitIndex={map[index]}
                  numberOfStones={board[map[index]]}
                ></Pit>
              </div>
            );
          }
          else {
            return (
              <div key={index} className="grid-item">
                  <Pit
                    numberOfStones={board[map[index]]}
                  ></Pit>
              </div>
            )
          }
        }
        else {
          if (index >= 1 && index <= 6) {
            return (
              <div key={index} className="grid-item">
                <Pit
                  makeMove={makeMove}
                  gameID={gameID}
                  pitIndex={map[index]}
                  numberOfStones={board[map[index]]}
                ></Pit>
              </div>
            );
          }
          else {
            return (
              <div key={index} className="grid-item">
                  <Pit
                    numberOfStones={board[map[index]]}
                  ></Pit>
              </div>
            )
          }
        }
        
      }
    });
  }

  async function makeMove(index, gameID) {
    const requestBody = { game_id: gameID, pit_index: index };
    const moveResponse = await api.makeMove(requestBody);
    setBoard(moveResponse["board"]);
    console.log("sa");
    setPlayerTurn(moveResponse["player_turn"]);
    setPlayer1Score(moveResponse["player_1_score"])
    setPlayer2Score(moveResponse["player_2_score"])
    setGameOver(moveResponse["game_over"])
    setWinner(moveResponse["winner"])
    if(moveResponse["game_over"]) {
      setIsOpen(true);
    }
  }
  async function fetchData() {
    const {
      game_id,
      board,
      game_over,
      message,
      player_1,
      player_1_score,
      player_2,
      player_2_score,
      player_turn,
      winner,
    } = await api.initializeGame();
    setGameOver(game_over);
    setMessage(message);
    setPlayer1(player_1);
    setPlayer2(player_2);
    setPlayer1Score(player_1_score);
    setPlayer2Score(player_2_score);
    setPlayerTurn(player_turn);
    setWinner(winner);
    setBoard(board);
    setGameID(game_id);

    const rules = await api.getRules();
    setRules(rules['message']);

  }

  useEffect(() => {
    fetchData();
  }, []);


  if(gameStarted) {
    return (
      <div className="App">
        <Dialog open={isOpen} onClose={handleClose} PaperProps={{ style: dialogStyle }}>
          <DialogTitle>GAME OVER!</DialogTitle>
          <DialogContent>Winner is: {winner}</DialogContent>
        </Dialog>
        <Dialog className="dialog" open={showRuleDialog} onClose={handleCloseRuleDialog} PaperProps={{ style: dialogStyle }}>
          <DialogTitle> Mancala Rules </DialogTitle>
          <DialogContent>
            <ul>
            {
              rules.map((rule, index) => {
                if(index === 0 || index === 5 || index === 8) {
                  return <h5> { rule } </h5>
                }
                return <li> {rule} </li>
              })
            }
            </ul>
          </DialogContent>
        </Dialog>
        <header className="App-header">
          <div style={{display: 'flex', width: '920px'}}>
            <div style={{width: '43%'}} />
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', width: '57%' }}>
              <p> {playerTurn === 1 ? `${player2}'s Turn` : player2} </p>
              <p> {`Score: ${player2Score}`} </p>
            </div>
          </div>
          <div className="board">{renderBoard(board)}</div>
          <div style={{display: 'flex', width: '920px'}}>
            <div style={{width: '43%'}} />
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', width: '57%' }}>
              <p> {playerTurn === 0 ? `${player1}'s Turn` : player1} </p>
              <p> {`Score: ${player1Score}`} </p>
            </div>
          </div>
          <div style={{display: 'flex', justifyContent: 'flex-end', width: '920px'}}>
            <button className="cool-button" onClick={() => setShowRuleDialog(!showRuleDialog)}> Help </button>
          </div>
        </header>
      </div>
    );
  }
  else {
    return(<div className="App"><header className="App-header"> <p>Click here to play!</p><button className="cool-button" onClick={() => setGameStarted(true)}> Start Game </button> </header></div>)
  }
}

export default App;
