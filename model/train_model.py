import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import joblib
import os

# CSV File
DATASET = "student_data.csv"

# Save Model
MODEL_FILE = "student_model.pkl"


def train_model():

    data = pd.read_csv(DATASET)

    X = data[
        [
            "study_hours",
            "attendance",
            "math",
            "science",
            "english",
            "computer"
        ]
    ]

    y = data["performance_score"]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    model = RandomForestRegressor(
        n_estimators=200,
        random_state=42
    )

    model.fit(X_train, y_train)

    score = model.score(X_test, y_test)

    print("Model Accuracy:", score)

    joblib.dump(model, MODEL_FILE)

    print("Model Saved Successfully")


if __name__ == "__main__":
    train_model()