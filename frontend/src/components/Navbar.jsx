import { NavLink } from "react-router-dom"; // Unlike href, it does not send a whole request / refresh the browser, allowing seamless integration. navlink adds more stylizations
import { logOut } from "../utilities";

export default function Navbar() {
  return (
    <>
    <nav className="navbar bg-danger">
      {/* right side */}
      <div>
        <NavLink to="/" activeClassName="active" className="navbar-brand text-white ml-3">
          <img src="pokeball.png" width="30" height="30" className="d-inline-block align-top mr-3" alt=""/>
          <span className="navbar-item">Home</span>
        </NavLink>
        <NavLink to="watchlist/" activeClassName="active" className="navbar-item text-white">
          Watchlist
        </NavLink>
      </div>

      {/* center */}
      <div>
          <form className="d-flex">
            <input className="form-control me-2" type="search" placeholder="Search" aria-label="Search"></input>
            <button className="btn btn-outline-warning" type="submit">
              <i className="bi bi-search"></i>
            </button>
          </form>
        </div>

       {/* right */}
            <button type="button" onClick={logOut} className="btn btn-warning mr-3">Logout</button>
    </nav>
    </>
  );
}