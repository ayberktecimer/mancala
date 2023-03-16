import {  useState, useEffect } from 'react';
import './styles.css';


export default function Pit({ makeMove, gameID, pitIndex, numberOfStones }) {

  const [stones, setStones] = useState([]);

  useEffect(() => {
    const stoneDivs = [];
    for(let i = 0; i < numberOfStones; i++) {
      stoneDivs.push(<div className='stone' />)
    }
    setStones(stoneDivs);
  }, [numberOfStones]) 

  return (
    makeMove && numberOfStones > 0 ? (
      <div className='pit-container' onClick={() => makeMove(pitIndex, gameID)}>
        {stones}
      </div>
    ) : 
      <div className='pit-container-disabled'> {stones} </div>
  );
}