# app/model.py
import joblib

class SugarModel:
    def predict(self, image):
        # Dummy prediction logic
        return {"sugar_content": 5}

# Save the model
model = SugarModel()
joblib.dump(model, "model/sugar_model.joblib")
