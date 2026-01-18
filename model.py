from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import GradientBoostingClassifier
import pickle
import pandas as pd

df = pd.read_csv("customer_churn_dataset-training-master.csv")
X = df.drop(['CustomerID', 'Churn'], axis=1)
y = df['Churn']

mask = y.notna()
X = X[mask]
y = y[mask]

categorical_cols = ["Gender", "Subscription Type", "Contract Length"]
numerical_cols = ["Age", "Tenure", "Usage Frequency", "Support Calls", "Payment Delay","Total Spend", "Last Interaction"]

preprocessor = ColumnTransformer(
    transformers=[
        ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_cols),
        ("num", "passthrough", numerical_cols)
    ]
)

gb_model = Pipeline(
    steps=[
        ("preprocessing", preprocessor),
        ("regressor", GradientBoostingClassifier(
            n_estimators=200,
            learning_rate=0.1,
            random_state=42
        ))
    ]
)

gb_model.fit(X, y)

with open("customerChurn_model.pkl", "wb") as f:
    pickle.dump(gb_model, f)

print("Model trained and saved!")
