import { useState } from "react";
import { NavLink, useOutletContext, useNavigate } from "react-router-dom";
import { log_in } from "../utilities";

export default function Login() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const { setUser } = useOutletContext();
  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const user = await log_in(email, password);
      setUser(user);
      alert("Success! Welcome!");
      navigate("/");
    } catch (error) {
      alert("Wrong password or Account Does Not Exist!");
    }
  };

  return (
    <>
      {/* to make background red */}
      <div className="bg-red-500">
        {/* to make the form aligned */}
        <div className="container d-flex justify-content-center align-items-center vh-100">
          {/* to add custom css to the form */}
          <div className="bg-white rounded-xl custom-form p-5">
            {/* to handle submission of the form */}
            <form onSubmit={(e) => handleSubmit(e)}>
              {/* Align and resize the Pokeball image */}
              <div className="d-flex justify-content-center mb-4">
                <img
                  src="/pokeball.png"  // Use absolute path for images in the public folder
                  alt="Pokeball"
                  className="w-24 h-24" // Tailwind: change sizes as needed
                  style={{ width: "100px", height: "100px" }} // Inline styles (if not using Tailwind)
                />
              </div>
              <h1 className="d-flex justify-content-center">Welcome!</h1>
              {/* email input */}
              <div className="form-group mt-4">
                Email Address
                <input
                  value={email}
                  onChange={(e) => setEmail(e.target.value)}
                  type="email"
                  className="form-control"
                  id="exampleInputEmail1"
                  aria-describedby="emailHelp"
                  placeholder="Enter email"
                  required
                />
              </div>
              {/* password input */}
              <div className="form-group mb-1">
                Password
                <input
                  value={password}
                  onChange={(e) => setPassword(e.target.value)}
                  type="password"
                  className="form-control"
                  id="exampleInputPassword1"
                  placeholder="Password"
                  required
                />
              </div>
              {/* click to login */}
              <div className="d-flex justify-content-center mt-3 mb-4">
                <span>
                  Click to <NavLink to="/signup">Sign Up</NavLink>
                </span>
              </div>
              {/* submit button */}
              <div className="d-flex justify-content-center">
                <button
                  type="submit"
                  className="btn btn-outline-primary"
                  value="Login"
                >
                  Login
                </button>
              </div>
            </form>
          </div>
        </div>
      </div>
    </>
  );
}
