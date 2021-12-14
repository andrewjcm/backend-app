import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix


def cleaned_data():
    df = pd.read_csv("covid.csv")

    # rename columns
    df.rename(columns={
        "date_died": "died",
        "intubed": "ventilator",
        "contact_other_covid": "covid_contact",
        "covid_res": "covid_positive"
    }, inplace=True)
    df = df[['sex', 'patient_type', 'died', 'age',
             'ventilator', 'pneumonia', 'pregnancy', 'diabetes', 'copd',
             'asthma', 'inmsupr', 'hypertension', 'other_disease', 'cardiovascular',
             'obesity', 'renal_chronic', 'tobacco', 'covid_contact',
             'covid_positive', 'icu']]

    # Convert death dates to died
    df['died'] = [0 if date == "9999-99-99" else 1 for date in df['died']]

    # Replace all unknowns to NaN
    df = df.replace([97, 98, 99, 3], np.nan)

    # Replace all 2 to 0 (Female = 1, Male = 0, Outpatient = 1, Inpatient =0, Yes = 1, No = 0)
    df = df.replace(2, 0)

    # Drop non-confirmed cases
    df = df[df['covid_positive'] == 1]

    # Drop columns with too many unknowns
    df.drop(columns=["ventilator", "pregnancy", "covid_contact", "icu"], inplace=True)

    # Drop remaining rows with not enough data
    df.dropna(inplace=True)
    return df


class PredictSurvival:
    def __init__(self, features):
        self.features = features
        self.data = cleaned_data()
        self.lr_model = self.trained_model()
        self.result = self.prediction()

    def trained_model(self):
        # Separate training DF and answer DF
        X = self.data[['sex', 'patient_type', 'age', 'pneumonia', 'diabetes', 'copd',
                'asthma', 'inmsupr', 'hypertension', 'other_disease', 'cardiovascular',
                'obesity', 'renal_chronic', 'tobacco', ]]

        y = self.data['died']

        # train and test data
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

        # Instantiate the model
        lm = LogisticRegression(max_iter=200)

        # Fit data
        lm.fit(X_train, y_train)

        return lm

    def prediction(self):
        features_df = pd.DataFrame(self.features, index=[0])

        # Predict
        predict = self.lr_model.predict([features_df.iloc[0]])

        return predict[0]
