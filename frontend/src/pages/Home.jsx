import { useEffect, useState } from "react";
import { useNavigate, useOutletContext } from "react-router-dom";
import { viewPortfolio } from "../utilities";

export default function Home() {
  const { user } = useOutletContext();
  const navigate = useNavigate();
  const [portfolio, setPortfolio] = useState(null);
  const [sprites, setSprites] = useState({}); // Store sprites for each Pokemon

  useEffect(() => {
    if (!user) {
      navigate("/login"); // go to login if the user is logged out
      return;
    }

    // grab portfolio if the user is logged in
    const fetchPortfolio = async () => {
      const portfolioData = await viewPortfolio();
      if (portfolioData) {
        setPortfolio(portfolioData);

        // grab sprites for each Pokemon
        portfolioData.pokemon.forEach((pkmn) => {
          fetchSprite(pkmn.pokedex_id);
        });
      }
    };

    fetchPortfolio();
  }, [user, navigate]);

  // grab sprite from PokeAPI
  const fetchSprite = async (pokedexId) => {
    try {
      const response = await fetch(`https://pokeapi.co/api/v2/pokemon/${pokedexId}`);
      const data = await response.json();
      const spriteUrl = data.sprites.front_default; // Use the front_default sprite
      setSprites((prevSprites) => ({
        ...prevSprites,
        [pokedexId]: spriteUrl,
      }));
    } catch (error) {
      console.error("Failed to fetch the Pokemon sprite:", error);
    }
  };

  if (!portfolio) {
    return (
      <div className="flex justify-center items-center min-h-screen bg-gray-100">
        <div className="text-lg text-gray-700">Loading portfolio...</div>
      </div>
    ); // show loading state when fetching
  }

  return (
    <div className="min-h-screen bg-gray-100 py-8">
      <div className="max-w-4xl mx-auto bg-white p-6 rounded-lg shadow-lg">
        <h1 className="text-3xl font-bold text-blue-600 mb-6">Welcome, {user}!</h1>

        <div className="mb-6">
          <h2 className="text-xl font-semibold text-gray-800">Portfolio Overview</h2>
          <p className="text-lg text-gray-600">Total Portfolio Value: <span className="font-bold">₽{portfolio.total_portfolio}</span></p>
          <p className="text-lg text-gray-600">Buying Power: <span className="font-bold">₽{portfolio.buying_power}</span></p>
        </div>

        <div>
          <h3 className="text-xl font-semibold text-gray-800 mb-4">Pokemon in Portfolio</h3>
          <ul>
            {portfolio.pokemon.map((pkmn) => (
              <li key={pkmn.pokedex_id} className="mb-4 flex items-center p-4 bg-gray-50 rounded-lg shadow-md">
                <img
                  src={sprites[pkmn.pokedex_id]} // sprite
                  alt={`${pkmn.pokemon} sprite`}
                  className="w-16 h-16 mr-4 rounded-lg border border-gray-300"
                />
                <div className="flex-1">
                  <p className="text-lg font-semibold text-gray-800">{pkmn.pokemon}</p>
                  <p className="text-sm text-gray-600">Shares: {pkmn.shares}</p>
                  <p className="text-sm text-gray-600">Total Cost: ₽{pkmn.total_price}</p>
                  <p className="text-sm text-gray-600">Price Per Share: ₽{pkmn.price_per_share}</p>
                </div>
              </li>
            ))}
          </ul>
        </div>
      </div>
    </div>
  );
}