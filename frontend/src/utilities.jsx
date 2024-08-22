import axios from "axios";

//creating a base url api to our backend
export const api = axios.create({
  baseURL:"http://127.0.0.1:8000/api/v1/",
});
// --------------SIGN UP --------------------
export const signUp = async(email, password) => {
  let response = await api.post("user/signup/", {
    email: email,
    password: password,
  });
  //storing user's cookies / token through the local storage if user created
  if (response.status === 201) {
    let { user, token } = response.data;
    localStorage.setItem("token", token);
    api.defaults.headers.common["Authorization"] = `Token ${token}`;
    return user;
  }
  alert("Credentials failed! Try again.")
  return null;
};

// --------------SIGN IN --------------------
export const log_in = async(email, password) => {
  let response = await api.post("user/login/", {
    email: email,
    password: password,
  });
  //storing user's cookies / token through the local storage if user created
  if (response.status === 200) {
    let { user, token } = response.data;
    localStorage.setItem("token", token);
    api.defaults.headers.common["Authorization"] = `Token ${token}`;
    return user;
  }
  alert("Credentials failed! Try again.")
  return null;
};

// --------------IF USER IS LOGGED IN --------------------
export const confirmUser = async () => {
  let token = localStorage.getItem("token");
  if (token) {
    api.defaults.headers.common["Authorization"] = `Token ${token}`;
    let response = await api.get("user/info");
    console.log(response.data.email);
    return response.data.email;
  }
  return null;
};


// --------------IF USER IS LOGGING OUT  --------------------
export const logOut = async () => {
    let response = await api.post("user/logout/");
    if (response.status === 204){
        localStorage.removeItem("token")
        delete api.defaults.headers.common["Authorization"]
        alert("Logged out successfully! :( ")
        return null
    }
    alert("Something went wrong! Try logging out again")
};

//------TO TEST IF THERE IS A BACKEND CONNECTION
// import { useEffect } from "react";

// export default function App() {
//   useEffect(() => {
//     // Replace with your backend API URL
//     fetch("http://localhost:5000/api/test")
//       .then((response) => response.json())
//       .then((data) => console.log("Success:", data))
//       .catch((error) => console.error("Error:", error));
//   }, []);

//   return (
//     <div>
//       <h1>Testing Backend Connection</h1>
//     </div>
//   );
// }
