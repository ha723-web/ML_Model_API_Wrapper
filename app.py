from flask import Flask, request, jsonify
from model import predict_price
from database import SessionLocal
from models import Prediction

app = Flask(__name__)

@app.route("/predict_price", methods=["POST"])
def predict():
    try:
        # ✅ Get JSON data from request
        data = request.get_json()

        # ✅ Debug print to see exactly what was received
        print("🧪 Incoming JSON:", data)

        # ✅ Extract values from JSON
        labor = data["labor_cost"]
        material = data["material_cost"]
        price = predict_price(labor, material)

        # ✅ Save prediction to the database
        session = SessionLocal()
        prediction = Prediction(
            labor_cost=labor,
            material_cost=material,
            predicted_price=price
        )
        session.add(prediction)
        session.commit()
        session.close()

        # ✅ Return the prediction as JSON
        return jsonify({"predicted_price": price})

    except Exception as e:
        print("❌ Error:", str(e))  # Print error in terminal
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, port=5053)
