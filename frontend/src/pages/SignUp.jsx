import { useEffect, useState } from "react";
import { NavLink, useOutletContext, useNavigate } from "react-router-dom";
import { signUp } from "../utilities";

export default function SignUp() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const navigate = useNavigate();

  //-------------if user is able to create an account-----------------
  const { setUser } = useOutletContext();
  const handleSubmit = async (e) => {
    e.preventDefault();
    try { //try create account first
      const user = await signUp(email, password);
      setUser(user);
      alert("Account Created! Please log in!");
      navigate("/login");
    } catch (error) {       // if the error is an http 400 bad request, that means that there is an account
        alert("Account Already Exists!");
    }
  };
//-------------------------------------

  return (
    <>
      {/* to make background red */}
      <div className="bg-red-500">
        {/* to make the form aligned */}
        <div className="container d-flex justify-content-center align-items-center vh-100">
          {/* to add custom css to the form */}
          <div className="bg-white rounded-xl custom-form">
            {/* to handle submission of the form */}
            <form onSubmit={(e) => handleSubmit(e)}>
              {" "}
              {/* calling to the utilties jsx */}
              <h1 className="d-flex justify-content-center">Sign Up Today!</h1>
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
                <small id="emailHelp" className="form-text text-muted">
                  We will not share your email to anyone.
                </small>
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
                  {" "}
                  Click to <NavLink to="/login/">Log in</NavLink>
                </span>
              </div>
              {/* submit button */}
              <div className="d-flex justify-content-center">
                <button
                  type="submit"
                  className="btn btn-outline-primary"
                  value="Resigter"
                >
                  Register
                </button>
              </div>
            </form>
          </div>
        </div>
      </div>
    </>
  );
}



