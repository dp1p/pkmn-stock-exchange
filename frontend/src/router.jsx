//router.jsx
import { createBrowserRouter } from "react-router-dom";
import App from "./App";
import Home from "./pages/Home.jsx";
import Login from "./pages/Login.jsx";
import SignUp from "./pages/SignUp.jsx"
import NotFound from "./pages/NotFound.jsx"
import Watchlist from "./pages/Watchlist.jsx";
import Pokemon from "./pages/Pokemon.jsx";
//for tailwind
import "./index.css";
//to confirm that there is a user
import { confirmUser } from "./utilities.jsx";


const router = createBrowserRouter([
  {
    path: "/",
    loader: confirmUser,
    element: <App />,
    children: [
      {
        index: true,
        element: <Home />,
      },
      {
        path: "/login",
        element: <Login />,
      },
      {
        path: "/signup",
        element: <SignUp />,
      },
      {
        path: "/watchlist",
        element: <Watchlist />,
      },
      {
        path: "/pkmn/:pokemon_id", //name is dynamic
        element: <Pokemon/>
      },
    ],
    errorElement: <NotFound />,
  },
]);

export default router;
