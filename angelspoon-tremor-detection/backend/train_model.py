from pathlib import Path
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import joblib

from app.simulator import generate_imu_data
from app.feature_extraction import extract_features


def build_dataset(samples_per_class: int = 120):
    rows = []

    for _ in range(samples_per_class):
        tremor_df = generate_imu_data(tremor=True)
        features = extract_features(tremor_df)
        features["label"] = 1
        rows.append(features)

        normal_df = generate_imu_data(tremor=False)
        features = extract_features(normal_df)
        features["label"] = 0
        rows.append(features)

    return pd.DataFrame(rows)


def train():
    dataset = build_dataset()
    X = dataset.drop(columns=["label"])
    y = dataset["label"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=42, stratify=y
    )

    random_forest = RandomForestClassifier(n_estimators=100, random_state=42)
    random_forest.fit(X_train, y_train)

    svm = SVC(probability=True, random_state=42)
    svm.fit(X_train, y_train)

    rf_accuracy = accuracy_score(y_test, random_forest.predict(X_test))
    svm_accuracy = accuracy_score(y_test, svm.predict(X_test))

    print("Random Forest Accuracy:", round(rf_accuracy, 4))
    print("SVM Accuracy:", round(svm_accuracy, 4))
    print("\\nRandom Forest Report:")
    print(classification_report(y_test, random_forest.predict(X_test)))

    model_dir = Path("models")
    model_dir.mkdir(exist_ok=True)

    joblib.dump(random_forest, model_dir / "tremor_model.joblib")
    dataset.to_csv("data/simulated_imu_dataset.csv", index=False)

    print("\\nSaved model to models/tremor_model.joblib")
    print("Saved dataset to data/simulated_imu_dataset.csv")


if __name__ == "__main__":
    train()
