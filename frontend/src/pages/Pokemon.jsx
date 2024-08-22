import React, { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import { fetchPokemonInfo, buyPokemon, sellPokemon } from "../utilities";

export default function Pokemon() {
  const { pokemon_id } = useParams();
  const [pokemon, setPokemon] = useState(null);
  const [sprite, setSprite] = useState(null);
  const [shares, setShares] = useState(1);
  const [currentPrice, setCurrentPrice] = useState(null);

  useEffect(() => {
    const getPokemonData = async () => {
      const data = await fetchPokemonInfo(pokemon_id);
      if (data) {
        setPokemon(data);
        setCurrentPrice(data.base_price); // initialize the current price

        try {
          const response = await fetch(
            `https://pokeapi.co/api/v2/pokemon/${pokemon_id}`
          );
          const spriteData = await response.json();

          const animatedSprite =
            spriteData.sprites.versions["generation-v"]["black-white"].animated
              .front_default;
          setSprite(animatedSprite || spriteData.sprites.front_default);
        } catch (error) {
          console.error("Failed to fetch the Pokemon sprite:", error);
        }
      } else {
        alert("Pokemon not found or Pokemon is Legendary / Mythical.");
      }
    };
    getPokemonData();
  }, [pokemon_id]);

useEffect(() => {
  // price change
  const changePrice = () => {
    const change = Math.random() * 0.1 - 0.05; // change by 5%
    const newPrice = currentPrice * (1 + change);
    setCurrentPrice(newPrice.toFixed(2)); // set the new price and round to 2 decimal places
  };
  const intervalId = setInterval(changePrice, 2000); // update price every 2 seconds
  return () => clearInterval(intervalId);
}, [currentPrice]); //whenever the price changes update

  const types = {
    normal: "bg-color-normal",
    fire: "bg-color-fire",
    water: "bg-color-water",
    grass: "bg-color-grass",
    electric: "bg-color-electric",
    ice: "bg-color-ice",
    fighting: "bg-color-fighting",
    poison: "bg-color-poison",
    ground: "bg-color-ground",
    flying: "bg-color-flying",
    psychic: "bg-color-psychic",
    bug: "bg-color-bug",
    rock: "bg-color-rock",
    ghost: "bg-color-ghost",
    dragon: "bg-color-dragon",
    dark: "bg-color-dark",
    steel: "bg-color-steel",
    fairy: "bg-color-fairy",
  };

  const handleBuyPokemon = async () => {
    if (shares <= 0) {
      alert("Please enter a valid number of shares.");
      return;
    }
    const result = await buyPokemon(pokemon.name, shares);
    if (result) {
      alert(`Successfully bought ${shares} shares of ${pokemon.name}!`);
    } else {
      alert("Failed to buy Pokemon. Please try again.");
    }
  };

  const handleSellPokemon = async () => {
    if (shares <= 0) {
      alert("Please enter a valid number of shares.");
      return;
    }
    const result = await sellPokemon(pokemon.name, shares);
    if (result) {
      alert(`Successfully sold ${shares} shares of ${pokemon.name}!`);
    } else {
      alert("Failed to sell Pokemon. Please try again.");
    }
  };

  if (!pokemon) {
    return <div>Loading Pokemon data...</div>;
  }

  return (
    <div className="flex justify-center items-center min-h-screen bg-gray-100">
      <div className="flex w-11/12 max-w-4xl bg-white rounded-lg shadow-lg overflow-hidden">
        {/* left side: sprite, price, name, and types */}
        <div className="flex flex-col items-center w-1/2 p-6 border-r justify-center">
          {sprite && (
            <img
              src={sprite}
              alt={`${pokemon.name} sprite`}
              className="w-32 h-32 mb-4"
            />
          )}
          <h1 className="text-3xl font-bold text-gray-800 mb-2">
            ₽{currentPrice}
          </h1>
          <h2 className="text-2xl font-semibold text-gray-700 mb-4">
            {pokemon.name}
          </h2>
          <div className="flex flex-wrap justify-center gap-2 mb-4">
            {pokemon.what_type.map((type) => (
              <div
                key={type}
                className={`flex items-center gap-2 px-4 py-2 rounded-full text-white ${types[type]}`}
              >
                <img
                  src={pokemon.icons[type]}
                  alt={`${type} icon`}
                  className="w-6 h-6"
                />
                <span>{type.charAt(0).toUpperCase() + type.slice(1)}</span>
              </div>
            ))}
          </div>
        </div>

        {/* right side: details */}
        <div className="flex flex-col w-1/2 p-6">
          <div>
            <h3 className="text-lg font-semibold text-gray-800 mb-2">
              Base Stats:
            </h3>
            <ul className="list-disc list-inside">
              <li>HP: {pokemon.base_stats.hp}</li>
              <li>Attack: {pokemon.base_stats.attack}</li>
              <li>Defense: {pokemon.base_stats.defense}</li>
              <li>Special Attack: {pokemon.base_stats["special-attack"]}</li>
              <li>Special Defense: {pokemon.base_stats["special-defense"]}</li>
              <li>Speed: {pokemon.base_stats.speed}</li>
            </ul>
          </div>
          <p className="mt-4 text-gray-600">Move Count: {pokemon.move_count}</p>
          <p className="mt-2 text-gray-600">
            Description: {pokemon.description}
          </p>
          <p className="mt-2 text-gray-600">
            Evolution Stages: {pokemon.evolution_stages}
          </p>

          <div className="mt-6">
            <input
              type="number"
              value={shares}
              onChange={(e) => setShares(e.target.value)}
              placeholder="Number of Shares"
              className="form-input w-full p-2 border rounded-md mb-4"
              min="1"
            />
            <div className="flex justify-between">
              <button
                type="button"
                className="btn btn-outline-success"
                onClick={handleBuyPokemon}
              >
                BUY
              </button>
              <button
                type="button"
                className="btn btn-outline-danger"
                onClick={handleSellPokemon}
              >
                SELL
              </button>
            </div>
          </div>

          <div className="mt-6 text-center">
            <button type="button" className="btn btn-outline-warning">
              ADD TO WATCHLIST
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}
