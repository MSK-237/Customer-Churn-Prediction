# Customer Churn Prediction

This project predicts whether a telecom customer will churn or not using Machine Learning and Deep Learning models.

## Project Features
- Data preprocessing
- Feature engineering
- Logistic Regression
- Random Forest
- XGBoost
- Deep Learning (ANN)
- Model comparison
- Streamlit deployment
- Hugging Face deployment

## Technologies
- Python
- Pandas
- Scikit-learn
- TensorFlow
- XGBoost
- Streamlit

## Models Performance

| Model | Accuracy |
|---|---|
| Logistic Regression | 0.81 |
| Random Forest | 0.81 |
| XGBoost | 0.78 |
| Deep Learning | 0.77 |

## Hugging Face Demo

https://huggingface.co/spaces/MSK34/Customer-churn-prediction

## Project Structure

```text
Customer-Churn-Prediction/
│
├── Customer Churn Prediction.ipynb
├── Customer-Churn.csv
├── requirements.txt
├── README.md
│
└── src/
    ├── app.py
    ├── churn_model.pkl
    ├── churn_dl_model.h5
    └── feature_columns.pkl