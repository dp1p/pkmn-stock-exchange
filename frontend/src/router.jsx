//router.jsx
import { createBrowserRouter } from "react-router-dom";
import App from "./App";
import Home from "./pages/Home.jsx";
import NotFound from "./pages/NotFound.jsx"
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
    ],
    errorElement: <NotFound />,
  },
]);

export default router;
