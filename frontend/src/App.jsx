// App.jsx
import { Outlet, useLocation } from "react-router-dom"; // use location will allow us to grab path of file
import Navbar from "./components/Navbar.jsx"

export default function App() {
  const location = useLocation(); 

  //store the path files in an array
  const hideNavbar = ["/login/", "/signup/"].includes(location.Login, location.SignUp)

  
  return (
    <>
      <Navbar/>
      <Outlet />
    </>
  );
}