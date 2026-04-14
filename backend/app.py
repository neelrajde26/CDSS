from flask import Flask, request, jsonify
from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
import numpy as np

app = Flask(__name__)

FEATURE_NAMES = [
    "Pregnancies",
    "Glucose",
    "Blood Pressure",
    "Skin Thickness",
    "Insulin",
    "BMI",
    "Diabetes Pedigree Function",
    "Age",
]


def create_model():
    X, y = make_classification(
        n_samples=800,
        n_features=len(FEATURE_NAMES),
        n_informative=6,
        n_redundant=2,
        n_classes=2,
        class_sep=1.3,
        weights=[0.55, 0.45],
        random_state=42,
    )
    model = make_pipeline(StandardScaler(), LogisticRegression(solver="liblinear"))
    model.fit(X, y)
    return model


model = create_model()




@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()

    values = [
        float(data["pregnancies"]),
        float(data["glucose"]),
        float(data["blood_pressure"]),
        float(data["skin_thickness"]),
        float(data["insulin"]),
        float(data["bmi"]),
        float(data["diabetes_pedigree"]),
        float(data["age"]),
    ]

    input_data = np.array([values])
    probability = model.predict_proba(input_data)[0][1]

    prediction = "High risk of diabetes" if probability >= 0.5 else "Low risk of diabetes"

    return jsonify({
        "prediction": prediction,
        "probability": round(probability * 100, 2)
    })
    except ValueError:
        return render_template(
            "result.html",
            prediction=None,
            probability=None,
            error="Please enter valid numeric values for all fields.",
            values={},
        )

    input_data = np.array([values])
    probability = model.predict_proba(input_data)[0][1]
    prediction = "High risk of diabetes" if probability >= 0.5 else "Low risk of diabetes"

    return render_template(
        "result.html",
        prediction=prediction,
        probability=f"{probability * 100:.1f}%",
        values={
            "Pregnancies": values[0],
            "Glucose": values[1],
            "Blood Pressure": values[2],
            "Skin Thickness": values[3],
            "Insulin": values[4],
            "BMI": values[5],
            "Diabetes Pedigree Function": values[6],
            "Age": values[7],
        },
        error=None,
    )


if __name__ == "__main__":
    app.run(debug=True)
