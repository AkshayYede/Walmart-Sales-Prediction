from flask import Flask, render_template, request, flash
import pickle
import numpy as np

app = Flask(__name__)
app.secret_key = "your_secret_key"  # Required for flash messages

# Load the trained model and scaler
model = pickle.load(open("model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))  # Used only for selected features

# Define feature names and scaling columns
FEATURE_NAMES = ["Store", "CPI", "Unemployment", "Temperature", "Holiday_Flag"]
SCALING_FEATURES = ["CPI", "Unemployment", "Temperature"]

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        try:
            # Extract inputs
            store = int(request.form["Store"])
            cpi = float(request.form["CPI"])
            unemployment = float(request.form["Unemployment"])
            temperature = float(request.form["Temperature"])
            holiday_flag = int(request.form["Holiday_Flag"])

            # Validate inputs
            if store < 1 or store > 45:
                flash("Error: Store value must be between 1 and 45", "danger")
                return render_template("index.html")

            if holiday_flag not in [0, 1]:
                flash("Error: Holiday Flag must be 0 or 1", "danger")
                return render_template("index.html")

            # Create input array
            input_data = np.array([[store, cpi, unemployment, temperature, holiday_flag]])

            # Apply scaling only to required features
            input_data[:, 1:4] = scaler.transform(input_data[:, 1:4])

            # Make prediction
            prediction = model.predict(input_data)[0]

            # Flash the prediction message
            flash(f"Predicted Sales: ${prediction:,.2f}", "success")

        except ValueError:
            flash("Error: Please enter valid numerical values.", "danger")

    return render_template("index.html")
  
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)