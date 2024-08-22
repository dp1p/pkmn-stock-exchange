import { useEffect } from "react";
import { useNavigate, useOutletContext } from "react-router-dom";

export default function Home() {
  const { user } = useOutletContext();
  const navigate = useNavigate();

  useEffect(() => {
    if (!user) {
      navigate("/login"); // if there is no user logged in
    }
  }, [user, navigate]);

  return (
    <div>{user && <h1 className="text-blue-500">Homepage of: {user}</h1>}</div>
  );
}
