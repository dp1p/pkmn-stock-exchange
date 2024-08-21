import { NavLink } from "react-router-dom";

export default function SignUp() {
  return (
    <>
    <div className="border border-primary container d-flex justify-content-center align-items-center vh-100">
        <form>
          <h1 className="d-flex justify-content-center">Welcome!</h1>
          <div className="form-group mt-4">
            <label for="InputEmail">Email address</label> 
            <input type="email" className="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" placeholder="Enter email"/>
          </div>
          <div className="form-group mt-4 mb-1">
            <label for="InputPassword">Password</label>
            <input type="password" className="form-control" id="exampleInputPassword1" placeholder="Password"/>
          </div>
          <div className="d-flex justify-content-center mt-3 mb-4">
              <span> Click to <NavLink to="/signup">Sign Up</NavLink></span>
          </div>
          <div className="d-flex justify-content-center">
            <button type="submit" className="btn btn-primary">Login</button>
          </div>
        </form>
    </div>
    </>
  );
}

