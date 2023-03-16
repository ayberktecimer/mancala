import { useState, useEffect } from 'react';
import './styles.css';

export default function Store({numberOfStones}) {

  const [stones, setStones] = useState([]);

  useEffect(() => {
    const stoneDivs = [];
    for(let i = 0; i < numberOfStones; i++) {
      stoneDivs.push(<div className='stone' />)
    }
    setStones(stoneDivs);
  }, [numberOfStones]) 

  return(
    <div className='store-container'>
      {stones}
    </div>
  );

}