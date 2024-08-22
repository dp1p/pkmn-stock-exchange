import { useEffect, useState } from "react";
import { NavLink, useOutletContext } from "react-router-dom";
import { log_in } from "../utilities";

export default function Login() {
  const [email, setEmail] = useState('')
  const [password, setPassword] = useState("");
  //to set user what the user signs up with
  const {setUser} = useOutletContext()
  const handleSubmit = async(e) => {
    e.preventDefault()
    setUser(await log_in(email,password))
  }

  
  return (
    <>
    {/* to make background red */}
    <div className="bg-red-500"> 
      {/* to make the form aligned */}
      <div className="container d-flex justify-content-center align-items-center vh-100">
        {/* to add custom css to the form */}
        <div className="bg-white rounded-xl custom-form">
          {/* to handle submission of the form */}
          <form onSubmit={(e)=> handleSubmit(e)}> {/* calling to the utilties jsx */}
            <h1 className="d-flex justify-content-center">Welcome!</h1>
            {/* email input */}
            <div className="form-group mt-4">
              Email Address
              <input value={email} onChange={(e)=>setEmail(e.target.value)}  type="email" className="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" placeholder="Enter email" required/>
            </div>
            {/* password input */}
            <div className="form-group mb-1">
              Password
              <input value={password} onChange={(e)=>setPassword(e.target.value)} type="password" className="form-control" id="exampleInputPassword1" placeholder="Password" required/>
            </div>
            {/* click to login */}
            <div className="d-flex justify-content-center mt-3 mb-4">
                <span> Click to <NavLink to="/signup">Sign Up</NavLink></span>
            </div>
            {/* submit button */}
            <div className="d-flex justify-content-center">
              <button type="submit" className="btn btn-outline-primary" value="Login">Login</button>
            </div>
          </form>
          </div>
      </div>
    </div>
    </>
  );
}



