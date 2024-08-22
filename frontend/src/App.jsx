// App.jsx
import { Outlet, useLocation, useLoaderData } from "react-router-dom"; // use location will allow us to grab path of file
import Navbar from "./components/Navbar.jsx"
import { useState } from "react";

export default function App() {
  const location = useLocation();
  const hideNavbar = ["/login", "/signup", "/login/", "/signup/"].includes(location.pathname); //store the path files in an array
  const [user, setUser] = useState(useLoaderData());

  return (
    <>
      {!hideNavbar && <Navbar user = {user} setUser={setUser} />}
      <Outlet context={{user, setUser}}/>
    </>
  );
}