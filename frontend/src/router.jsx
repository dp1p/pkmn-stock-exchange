//router.jsx
import { createBrowserRouter } from "react-router-dom";
import App from "./App";
import Home from "./pages/Home.jsx";
import Login from "./pages/Login.jsx";
import SignUp from "./pages/SignUp.jsx"
import NotFound from "./pages/NotFound.jsx"
import Watchlist from "./pages/Watchlist.jsx";
//for tailwind
import "./index.css";


const router = createBrowserRouter([
  {
    path: "/",
    element: <App />,
    children: [
      {
        index: true,
        element: <Home/>,
      },
      {
        path: "/login",
        element: <Login />,
      },
      {
        path: "/signup",
        element: <SignUp/>
      },
      {
        path:"/watchlist",
        element: <Watchlist/>
      },
    ],
    errorElement: <NotFound/>,
  },
]);

export default router;
