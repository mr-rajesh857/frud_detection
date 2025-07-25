Participates:
❖ Debasish Senapati- 22cse328
❖ Rajesh Kumar Panda- 22cse857
❖ Rakesh Senapati- 22cse329
❖ M.Bharat:- 22cse793


🚗 Auto Insurance Fraud Detection using ML
This project aims to detect fraudulent auto insurance claims using advanced machine learning and deep learning techniques. It involves a complete pipeline from data preprocessing, feature engineering, class imbalance handling, model training, evaluation, and final prediction on unseen validation data.

🧠 Problem Statement
Fraudulent auto insurance claims lead to significant financial losses for insurance companies. This project applies machine learning to accurately classify genuine vs. fraudulent claims based on key policyholder and claim features.

Dataset
✅ Training set: Includes both features and labeled target (Fraud_Ind)

✅ Test set: Includes features and labeled target (for evaluation)

✅ Validation set: Only features (unseen data)



Features Used (Top 5 Selected using mutual info)
Policy_Num

Accident_Location

Insured_Zip

Policy_Premium

DL_Expiry_Before_Accident_Days


Machine Learning Models Trained
The following 10 models were trained and evaluated:

Logistic Regression

Decision Tree

Random Forest

Gradient Boosting

AdaBoost

Naive Bayes

Support Vector Machine (SVM)

XGBoost

LightGBM

CatBoost



evaluation metrices:- 
Model	Accuracy	Precision	Recall	Specificity	F1-Score	ROC-AUC	MCC	Log Loss
Logistic Regression	1	1	1	1	1	1	1	0.0239
Decision Tree	1	1	1	1	1	1	1	0
Random Forest	1	1	1	1	1	1	1	0
Gradient Boosting	0.736	1	0.0075	1	0.0149	0.9148	0.0744	0.4879
AdaBoost	0.736	1	0.0075	1	0.0149	0.5966	0.0744	0.5711
Naive Bayes	1	1	1	1	1	1	1	0
Support Vector Machine	1	1	1	1	1	1	1	0
XGBoost	0.9956	1	0.9833	1	0.9916	1	0.9886	0.2486
LightGBM	1	1	1	1	1	1	1	0.1687
CatBoost	1	1	1	1	1	1	1	0.0697
<img width="831" height="265" alt="image" src="https://github.com/user-attachments/assets/59573b1a-4016-43fd-b306-c38cf7d84b62" />



Highlights
✅ Clean data preprocessing pipeline

✅ Advanced feature selection (Mutual Info, F-test, Boruta, Chi-square)

✅ SMOTE-based class balancing

✅ Multiple model evaluation

✅ Detection of overfitting

✅ Final deployment-ready prediction on unseen validation data

