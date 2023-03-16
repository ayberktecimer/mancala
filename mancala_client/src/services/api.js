import axios from 'axios';
const url = "http://0.0.0.0:80"
export const api = {

  

  async initializeGame() {
    const response = await axios.get(`${url}/initialize_game`);
    return response.data;
  },
  
  async makeMove(body) {
    const response = await axios.post(`${url}/make_move`, body);
    return response.data;
  },

  async getRules() {
    const response = await axios.get(`${url}/get_rules`);
    return response.data;
  }
};
