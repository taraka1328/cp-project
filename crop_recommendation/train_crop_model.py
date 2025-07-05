import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
import pickle

# Load dataset
df = pd.read_csv("crop_recommendation.csv")

# ✅ Rename columns to standard format (adjust these based on your actual CSV)
df.rename(columns={
    'Nitrogen': 'N',
    'Phosphorus': 'P',
    'Potassium': 'K',
    'Temperature': 'temperature',
    'Humidity': 'humidity',
    'pH_Value': 'ph',
    'Rainfall': 'rainfall',
    'Crop': 'label'
}, inplace=True)

# ✅ Print to verify
print("✅ Renamed Columns:")
print(df.columns.tolist())

# ✅ Check if all required columns are present
required_cols = ['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall', 'label']
if not all(col in df.columns for col in required_cols):
    missing = [col for col in required_cols if col not in df.columns]
    raise ValueError(f"Missing required columns: {missing}")

# ✅ Prepare features and labels
X = df[['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall']]
y = df['label']

# ✅ Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# ✅ Train the model
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# ✅ Save the trained model
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

print("🎉 Model trained and saved as model.pkl")
