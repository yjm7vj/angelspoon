import React from "react";
import { createRoot } from "react-dom/client";
import TremorDashboard from "./components/TremorDashboard";

function App() {
  return <TremorDashboard />;
}

createRoot(document.getElementById("root")).render(<App />);
