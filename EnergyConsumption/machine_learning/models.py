import os
from joblib import load

# Get the directory of the current script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Define the file paths relative to the current directory
SVM_typical_to_high_path = os.path.join(current_dir, 'SVM_typical_to_high.joblib')
SVM_typical_to_low_path = os.path.join(current_dir, 'SVM_typical_to_low.joblib')
ActiveEnergy_LinearRegression_path = os.path.join(current_dir, 'ActiveEnergy_LinearRegression.joblib')

# Load the saved models from files
loaded_SVM_typical_to_high = load(SVM_typical_to_high_path)
loaded_SVM_typical_to_low = load(SVM_typical_to_low_path)
loaded_linear_reg_model = load(ActiveEnergy_LinearRegression_path)