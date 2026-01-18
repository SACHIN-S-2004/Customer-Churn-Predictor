from flask import Flask, render_template, request
import pickle
import pandas as pd

app = Flask(__name__)

# Load your trained pipeline model
with open("customerChurn_model.pkl", "rb") as f:
    model = pickle.load(f)

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    churn_prob = None
    stay_prob = None

    if request.method == "POST":
        input_data = {
            "Age": int(request.form["age"]),
            "Gender": request.form["gender"],
            "Tenure": int(request.form["tenure"]),
            "Usage Frequency": int(request.form["usage"]),
            "Support Calls": int(request.form["support"]),
            "Payment Delay": int(request.form["delay"]),
            "Subscription Type": request.form["subscription"],
            "Contract Length": request.form["contract"],
            "Total Spend": float(request.form["spend"]),
            "Last Interaction": int(request.form["interaction"])
        }

        df = pd.DataFrame([input_data])

        probs = model.predict_proba(df)[0]
        stay_prob = round(probs[0] * 100, 2)
        churn_prob = round(probs[1] * 100, 2)

        prediction = "Churn 🚨" if churn_prob > stay_prob else "No Churn ✅"

    return render_template(
        "index.html",
        prediction=prediction,
        churn_prob=churn_prob,
        stay_prob=stay_prob
    )

if __name__ == "__main__":
    app.run(debug=True)
