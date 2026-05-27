import React, { useEffect, useState } from "react";
import { LineChart, Line, XAxis, YAxis, Tooltip, CartesianGrid } from "recharts";

export default function TremorDashboard() {
  const [prediction, setPrediction] = useState(null);
  const [sensorData, setSensorData] = useState([]);

  async function fetchPrediction() {
    try {
      const response = await fetch("http://127.0.0.1:8000/predict-tremor?tremor=true");
      const data = await response.json();
      setPrediction(data.prediction);
    } catch (error) {
      console.error("Backend not running yet:", error);
    }
  }

  async function fetchSensorData() {
    try {
      const response = await fetch("http://127.0.0.1:8000/simulate?tremor=true");
      const data = await response.json();
      setSensorData(data);
    } catch (error) {
      console.error("Backend not running yet:", error);
    }
  }

  useEffect(() => {
    fetchPrediction();
    fetchSensorData();
  }, []);

  return (
    <main style={{ fontFamily: "Arial", padding: "32px", maxWidth: "1000px", margin: "auto" }}>
      <h1>AngelSpoon Tremor Detection Dashboard</h1>
      <p>
        Real-time analytics concept for Parkinsonian tremor detection using simulated IMU sensor data.
      </p>

      <section style={{ display: "flex", gap: "16px", marginBottom: "24px" }}>
        <div style={{ padding: "16px", border: "1px solid #ddd", borderRadius: "12px", flex: 1 }}>
          <h3>Tremor Detected</h3>
          <p>{prediction ? String(prediction.tremor_detected) : "Loading..."}</p>
        </div>

        <div style={{ padding: "16px", border: "1px solid #ddd", borderRadius: "12px", flex: 1 }}>
          <h3>Probability</h3>
          <p>{prediction ? prediction.tremor_probability : "Loading..."}</p>
        </div>

        <div style={{ padding: "16px", border: "1px solid #ddd", borderRadius: "12px", flex: 1 }}>
          <h3>Severity Score</h3>
          <p>{prediction ? prediction.severity_score : "Loading..."}</p>
        </div>
      </section>

      <section>
        <h2>Simulated Accelerometer Signal</h2>
        <LineChart width={900} height={300} data={sensorData}>
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis dataKey="time" />
          <YAxis />
          <Tooltip />
          <Line type="monotone" dataKey="accel_x" dot={false} />
        </LineChart>
      </section>
    </main>
  );
}
