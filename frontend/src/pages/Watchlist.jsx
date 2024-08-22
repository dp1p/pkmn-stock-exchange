import React, { useEffect, useState } from "react";
import { getAllWatchlists, createWatchlist, removeFromWatchlist, deleteWatchlist, updateWatchlist } from "../utilities";

export default function Watchlist() {
  const [watchlists, setWatchlists] = useState([]);
  const [newWatchlistName, setNewWatchlistName] = useState(""); // State for the new watchlist name
  const [pokemonIdOrName, setPokemonIdOrName] = useState(""); // State for Pokemon to add
  const [selectedWatchlist, setSelectedWatchlist] = useState(""); // State for the selected watchlist to add Pokemon to

  // fetches all watchlists
  useEffect(() => {
    const fetchWatchlists = async () => {
      const data = await getAllWatchlists();
      if (data) {
        setWatchlists(data);
      } else {
        alert("Failed to fetch watchlists.");
      }
    };
    fetchWatchlists();
  }, []);

  // creating a new watchlist
  const handleCreateWatchlist = async (e) => {
    e.preventDefault();
    if (newWatchlistName === "") {
      alert("Watchlist name cannot be empty.");
      return;
    }
    const result = await createWatchlist(newWatchlistName);
    if (result) {
      setWatchlists([...watchlists, result]); // Update the watchlists state with the new watchlist
      setNewWatchlistName(""); // Clear the input field
      alert(`Watchlist '${newWatchlistName}' created!`);
    } else {
      alert("Failed to create watchlist.");
    }
  };

  // adding a pokemon to a watchlist
  const handleAddPokemon = async (e) => {
    e.preventDefault();
    if (selectedWatchlist === "" || pokemonIdOrName === "") {
      alert("Watchlist name and Pokemon ID/Name cannot be empty.");
      return;
    }
    const result = await updateWatchlist(selectedWatchlist, pokemonIdOrName);
    if (result) {
      const updatedWatchlists = watchlists.map(watchlist =>
        watchlist.name === selectedWatchlist ? result : watchlist
      );
      setWatchlists(updatedWatchlists);
      setPokemonIdOrName(""); // clears the input field
      alert(`Pokemon '${pokemonIdOrName}' added to '${selectedWatchlist}'!`);
    } else {
      alert("Failed to update watchlist.");
    }
  };

  // removing pokemon from a watchlist
  const handleRemovePokemon = async (watchlistName, pokemonName) => {
    const result = await removeFromWatchlist(watchlistName, pokemonName);
    if (result) {
      const updatedWatchlists = watchlists.map(watchlist =>
        watchlist.name === watchlistName ? result : watchlist
      );
      setWatchlists(updatedWatchlists);
      alert(`Pokemon '${pokemonName}' removed from '${watchlistName}'!`);
    } else {
      alert("Failed to remove Pokemon from watchlist.");
    }
  };

  // deleting a watchlist
  const handleDeleteWatchlist = async (watchlistName) => {
    const result = await deleteWatchlist(watchlistName);
    if (result) {
      setWatchlists(watchlists.filter(watchlist => watchlist.name !== watchlistName));
      alert(`Watchlist '${watchlistName}' deleted!`);
    } else {
      alert("Failed to delete watchlist.");
    }
  };

  return (
    <div>
      <h1>Your Watchlists</h1>

      {/* form to create a new watchlist */}
      <form onSubmit={handleCreateWatchlist} className="mb-4">
        <div className="flex">
          <input
            type="text"
            value={newWatchlistName}
            onChange={(e) => setNewWatchlistName(e.target.value)}
            placeholder="New Watchlist Name"
            className="form-control mr-2"
          />
          <button type="submit" className="btn btn-primary">
            Create Watchlist
          </button>
        </div>
      </form>

      {/*form add a Pokemon to a watchlist */}
      <form onSubmit={handleAddPokemon} className="mb-4">
        <div className="flex">
          <select
            value={selectedWatchlist}
            onChange={(e) => setSelectedWatchlist(e.target.value)}
            className="form-control mr-2"
          >
            <option value="">Select a Watchlist</option>
            {watchlists.map((watchlist) => (
              <option key={watchlist.name} value={watchlist.name}>
                {watchlist.name}
              </option>
            ))}
          </select>
          <input
            type="text"
            value={pokemonIdOrName}
            onChange={(e) => setPokemonIdOrName(e.target.value)}
            placeholder="Enter Pokemon ID or Name"
            className="form-control mr-2"
          />
          <button type="submit" className="btn btn-success">
            Add Pokemon
          </button>
        </div>
      </form>

      {watchlists.length === 0 ? (
        <div>No watchlists available.</div>
      ) : (
        watchlists.map((watchlist) => (
          <div key={watchlist.name} className="border p-4 mb-4">
            <div className="flex justify-between items-center">
              <h2>{watchlist.name}</h2>
              <button
                onClick={() => handleDeleteWatchlist(watchlist.name)}
                className="btn btn-danger"
              >
                Delete Watchlist
              </button>
            </div>
            <ul>
              {watchlist.pokemon.map((pokemon) => (
                <li key={pokemon.name} className="flex justify-between">
                  <span>
                    {pokemon.name} - ₽{pokemon.base_price}
                  </span>
                  <button
                    onClick={() => handleRemovePokemon(watchlist.name, pokemon.name)}
                    className="btn btn-warning"
                  >
                    Remove
                  </button>
                </li>
              ))}
            </ul>
          </div>
        ))
      )}
    </div>
  );
}