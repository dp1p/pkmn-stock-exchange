import { NavLink, useNavigate } from "react-router-dom"; 
import { logOut } from "../utilities";
import { useState } from "react";

export default function Navbar({ user, setUser }) {
  const [searchQuery, setSearchQuery] = useState(""); // State to track the search input
  const navigate = useNavigate();

  // handle logout
  const handleClick = async () => {
    setUser(await logOut());
  };

  // hadnle input change
  const handleInputChange = (e) => {
    setSearchQuery(e.target.value);
  };

  // handles form submission 
  const handleSearch = (e) => {
    e.preventDefault();
      navigate(`/pkmn/${searchQuery}`); // goes to pkmn info
  };

  return (
    <>
      <nav className="navbar bg-danger">
        {/* left side */}
        <div>
          <NavLink to="/" activeClassName="active" className="navbar-brand text-white ml-3">
            <img src="/pokeball.png" width="30" height="30" className="d-inline-block align-top mr-3" alt=""/>
            <span className="navbar-item">Home</span>
          </NavLink>
          <NavLink to="/watchlist/" activeClassName="active" className="navbar-item text-white">
            Watchlist
          </NavLink>
        </div>

        {/* center SEARCH BAR */}
        <div>
          <form className="d-flex" onSubmit={handleSearch}>
            <input 
              className="form-control me-2" 
              type="search" 
              placeholder="Enter pokedex/name" 
              aria-label="Search" 
              value={searchQuery} 
              onChange={handleInputChange} 
            />
            <button className="btn btn-outline-warning" type="submit">
              <i className="bi bi-search"></i>
            </button>
          </form>
        </div>

        {/* right side */}
        <button onClick={handleClick} className="btn btn-warning mr-3">Logout</button>
      </nav>
    </>
  );
}