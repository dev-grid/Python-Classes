import React, { useState } from "react";

const Calculator = () => {
    const [num1, setNum1] = useState("");
    const [num2, setNum2] = useState("");
    const [operation, setOperation] = useState("addition");
    const [result, setResult] = useState(null);
    const [error, setError] = useState(null);

    const calculate = async () => {
        setError(null);
        setResult(null);

        try {
            const response = await fetch("http://127.0.0.1:8000/api/calculate/", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ num1, num2, operation }),
            });

            const data = await response.json();
            if (response.ok) {
                setResult(data.result);
            } else {
                setError(data.error);
            }
        } catch (error) {
            setError("Failed to connect to server.");
        }
    };

    return (
        <div>
            <h2>Calculator</h2>
            <input type="number" value={num1} onChange={(e) => setNum1(e.target.value)} placeholder="First number" />
            <input type="number" value={num2} onChange={(e) => setNum2(e.target.value)} placeholder="Second number" />
            <select value={operation} onChange={(e) => setOperation(e.target.value)}>
                <option value="addition">Addition</option>
                <option value="subtraction">Subtraction</option>
                <option value="multiplication">Multiplication</option>
                <option value="division">Division</option>
            </select>
            <button onClick={calculate}>Calculate</button>

            {result !== null && <h3>Result: {result}</h3>}
            {error && <p style={{ color: "red" }}>{error}</p>}
        </div>
    );
};

export default Calculator;
