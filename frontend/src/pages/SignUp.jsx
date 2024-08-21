import { NavLink } from "react-router-dom";

export default function SignUp() {
  return (
    <>
    {/* to make background red */}
    <div className="bg-red-500"> 
      {/* to make the form aligned */}
      <div className="container d-flex justify-content-center align-items-center vh-100">
        {/* to add custom css to the form */}
        <div className="bg-white rounded-xl custom-form">
          <form>
            <h1 className="d-flex justify-content-center">Welcome!</h1>
            <div className="form-group mt-4">
              <label for="InputEmail">Email address</label> 
              <input type="email" className="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" placeholder="Enter email"/>
                <small id="emailHelp" className="form-text text-muted">We will not share your email to anyone.</small>
            </div>
            <div className="form-group mb-1">
              <label for="InputPassword">Password</label>
              <input type="password" className="form-control" id="exampleInputPassword1" placeholder="Password"/>
            </div>
            <div className="d-flex justify-content-center mt-3 mb-4">
                <span> Click to <NavLink to="/login/">Log in</NavLink></span>
            </div>
            <div className="d-flex justify-content-center">
              <button type="submit" className="btn btn-outline-primary">Register</button>
            </div>
          </form>
          </div>
      </div>
    </div>
    </>
  );
}

