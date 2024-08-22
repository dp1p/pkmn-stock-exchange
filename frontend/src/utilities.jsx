import axios from "axios";

//creating a base url api to our backend
export const api = axios.create({
  baseURL:"http://127.0.0.1:8000/api/v1/",
});
// --------------SIGN UP --------------------
export const signUp = async(email, password) => {
  let response = await api.post("user/signup/", {
    email: email,
    password: password,
  });
  //storing user's cookies / token through the local storage if user created
  if (response.status === 201) {
    let { user, token } = response.data;
    localStorage.setItem("token", token);
    api.defaults.headers.common["Authorization"] = `Token ${token}`;
    return user;
  }
  alert("Credentials failed! Try again.")
  return null;
};

// --------------SIGN IN --------------------
export const log_in = async(email, password) => {
  let response = await api.post("user/login/", {
    email: email,
    password: password,
  });
  //storing user's cookies / token through the local storage if user created
  if (response.status === 200) {
    let { user, token } = response.data;
    localStorage.setItem("token", token);
    api.defaults.headers.common["Authorization"] = `Token ${token}`;
    return user;
  }
  alert("Credentials failed! Try again.")
  return null;
};

// --------------IF USER IS LOGGED IN --------------------
export const confirmUser = async () => {
  let token = localStorage.getItem("token");
  if (token) {
    api.defaults.headers.common["Authorization"] = `Token ${token}`;
    let response = await api.get("user/info");
    console.log(response.data.email);
    return response.data.email;
  }
  return null;
};


// --------------IF USER IS LOGGING OUT  --------------------
export const logOut = async () => {
    let response = await api.post("user/logout/");
    if (response.status === 204){
        localStorage.removeItem("token")
        delete api.defaults.headers.common["Authorization"]
        alert("Logged out successfully! :( ")
        return null
    }
    alert("Something went wrong! Try logging out again")
};

//-------------------------------------------------------
//-------------------------------------------------------
//-------------------------------------------------------
//--------------- GRAB POKEMON ---------------------------

export const fetchPokemonInfo = async (pokemon_id) => {
  try {
    // Make a GET request to the API endpoint for fetching Pokémon info
    const response = await api.get(`pkmn/${pokemon_id}/`);
    return response.data; // Return the data received from the API
  } catch (error) {
    console.error("Failed to fetch Pokémon info:", error);
    return null; // Return null if there was an error
  }
};
// -------------- VIEW PORTFOLIO --------------------
export const viewPortfolio = async () => {
  try {
    const response = await api.get("portfolio/");
    return response.data;
  } catch (error) {
    console.error("Failed to load portfolio:", error);
    return null;
  }
};

// -------------- BUY POKEMON --------------------
export const buyPokemon = async (pokemonIdOrName, shares) => {
  try {
    const response = await api.post("portfolio/buy/", {
      pokemon_id_or_name: pokemonIdOrName,
      shares,
    });
    return response.data;
  } catch (error) {
    console.error("Failed to buy Pokémon:", error);
    return null;
  }
};

// -------------- SELL POKEMON --------------------
export const sellPokemon = async (pokemonIdOrName, shares) => {
  try {
    const response = await api.delete("portfolio/sell/", {
      data: { pokemon_id_or_name: pokemonIdOrName, shares },
    });
    return response.data;
  } catch (error) {
    console.error("Failed to sell Pokémon:", error);
    return null;
  }
};



// -------------- CREATE NEW WATCHLIST  --------------------

export const createWatchlist = async (watchlistName) => {
  try {
    const response = await api.post('watchlist/create/', { name: watchlistName }); // Send the name in the request body
    return response.data;
  } catch (error) {
    console.error('Failed to create watchlist:', error);
    return null;
  }
};

// -----------GET ALL WATCHLIST  --------------------

export const getAllWatchlists = async () => {
  try {
    const response = await api.get('watchlist/');
    return response.data;
  } catch (error) {
    console.error('Failed to fetch watchlists:', error);
    return null;
  }
};

// -----------GET  SPECIFIC WATCHLIST  --------------------
export const getWatchlist = async (watchlistName) => {
  try {
    const response = await api.get(`watchlist/read/${watchlistName}/`);
    return response.data;
  } catch (error) {
    console.error(`Failed to fetch watchlist '${watchlistName}':`, error);
    return null;
  }
};

// ----------- UPDATE A WATCHLIST  --------------------
export const updateWatchlist = async (watchlistName, pokemonIdOrName) => {
  try {
    const response = await api.put(`watchlist/update/${watchlistName}/`, {
      pokemon_id_or_name: pokemonIdOrName,
    });
    return response.data;
  } catch (error) {
    console.error(`Failed to update watchlist '${watchlistName}':`, error);
    return null;
  }
};

// ----------- REMOVE A PKMN FROM A WATCHLIST  --------------------
export const removeFromWatchlist = async (watchlistName, pokemonIdOrName) => {
  try {
    const response = await api.delete(`watchlist/delete/${watchlistName}/pkmn/`, {
      data: { pokemon_id_or_name: pokemonIdOrName },
    });
    return response.data;
  } catch (error) {
    console.error(`Failed to remove Pokémon from watchlist '${watchlistName}':`, error);
    return null;
  }
};

// ----------- DELETE AN ENTIRE WATCHLIST  --------------------
export const deleteWatchlist = async (watchlistName) => {
  try {
    const response = await api.delete(`watchlist/delete/${watchlistName}/`);
    return response.data;
  } catch (error) {
    console.error(`Failed to delete watchlist '${watchlistName}':`, error);
    return null;
  }
};


//------TO TEST IF THERE IS A BACKEND CONNECTION
// import { useEffect } from "react";

// export default function App() {
//   useEffect(() => {
//     // Replace with your backend API URL
//     fetch("http://localhost:5000/api/test")
//       .then((response) => response.json())
//       .then((data) => console.log("Success:", data))
//       .catch((error) => console.error("Error:", error));
//   }, []);

//   return (
//     <div>
//       <h1>Testing Backend Connection</h1>
//     </div>
//   );
// }
