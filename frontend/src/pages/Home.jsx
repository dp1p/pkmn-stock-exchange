import { useOutletContext } from "react-router-dom";

export default function Home() {
  const {user} = useOutletContext()
  return (
    <>
    <div>
        <h1 className="text-blue-500">Homepage of: {user}</h1>
    </div>
    </>
  );
}

