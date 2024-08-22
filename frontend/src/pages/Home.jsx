import { useEffect, useState } from "react";
import { useNavigate, useOutletContext } from "react-router-dom";
import { view_portfolio } from "../utilities";

export default function Home() {
  const { user } = useOutletContext();
  const navigate = useNavigate();
  const [portfolio, setPortfolio] = useState(null);

  useEffect(() => {
    if (!user) {
      navigate("/login"); //if user is logged out
      return;
    }

    // grab portfolio if the user is logged in
    const fetchPortfolio = async () => {
      const portfolioData = await view_portfolio();
      if (portfolioData) {
        setPortfolio(portfolioData);
      }
    };

    fetchPortfolio();
  }, [user, navigate]);
  if (!portfolio) {
    return <div>Loading portfolio...</div>; //  loading state while fetching
  }

  return (
    <div>
      <h1 className="text-blue-500">Homepage of: {user}</h1>
      <h2>Your Portfolio</h2>
      <p>Buying Power: {portfolio.buying_power}</p>
      <p>Total Portfolio Value: {portfolio.total_portfolio}</p>
      <ul>
        {portfolio.pokemon_list &&
          portfolio.pokemon_list.map((item, index) => (
            <li key={index}>
              {item.pokemon_name}: {item.shares} shares at ${item.total_price}
            </li>
          ))}
      </ul>
    </div>
  );
}
