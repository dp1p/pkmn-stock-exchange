// main.jsx
import ReactDOM from 'react-dom/client'
//for page navigation 
import { RouterProvider } from "react-router-dom";
import router from "./router.jsx";


ReactDOM.createRoot(document.getElementById("root")).render(
  <RouterProvider router={router} />
);
