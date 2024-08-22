import axios from "axios";

export const api = axios.create({
  baseURL: "http://127.0.0.1:8000/api/",
});

export const signUp = async (email, password) => {
  let response = await api.post("users/signup/", {
    email: email,
    password: password,
  });
  if (response.status === 201) {
    let { user, token } = response.data;
    localStorage.setItem("token", token);
    api.defaults.headers.common["Authorization"] = `Token ${token}`;
    return user;
  }
  alert("credentials failed");
  return null;
};

//creating a base url api to our backend
export const api = axios.create({
  baseURL:"http://120.0.0.1:8000/api/v1/",
});
