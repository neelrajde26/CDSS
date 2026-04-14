async function predict() {
  const data = {
    pregnancies: document.getElementById("pregnancies").value,
    glucose: document.getElementById("glucose").value,
    blood_pressure: document.getElementById("blood_pressure").value,
    skin_thickness: document.getElementById("skin_thickness").value,
    insulin: document.getElementById("insulin").value,
    bmi: document.getElementById("bmi").value,
    diabetes_pedigree: document.getElementById("diabetes_pedigree").value,
    age: document.getElementById("age").value
  };

  try {
    const response = await fetch("https://your-backend.onrender.com/predict", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify(data)
    });

    const result = await response.json();

    document.getElementById("result").innerHTML =
      `${result.prediction} (${result.probability}%)`;

  } catch (error) {
    document.getElementById("result").innerHTML =
      "Error connecting to server";
  }
}