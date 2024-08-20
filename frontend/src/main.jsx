// main.jsx
import ReactDOM from 'react-dom/client'
//for page navigation 
import { RouterProvider } from "react-router-dom";
import router from "./router.jsx";
//for bootstramp
import "bootstrap/dist/css/bootstrap.min.css";
//for tailwind
import "./index.css";


ReactDOM.createRoot(document.getElementById("root")).render(
  <RouterProvider router={router} />
);
