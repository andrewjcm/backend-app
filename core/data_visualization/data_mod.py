import pandas as pd
import numpy as np


def get_data():
    """ CSV data to pandas dataframe. """
    return pd.read_csv("covid.csv")


def rename_columns(df):
    """ Rename data columns. """
    return df.rename(columns={
        "date_died": "died",
        "intubed": "ventilator",
        "contact_other_covid": "covid_contact",
        "covid_res": "covid_positive"
    })


def adjust_values(df):
    """ Clean data. """
    # Convert death dates to died
    df['died'] = [0 if date == "9999-99-99" else 1 for date in df['died']]

    # Replace all unknowns to NaN
    df = df.replace([97, 98, 99, 3], np.nan)

    # Replace all 2 to 0 (Female = 1, Male = 0, Outpatient = 1, Inpatient =0, Yes = 1, No = 0)
    return df.replace(2, 0)


def cleaned_data(df):
    """ Rename columns and clean data. """
    df = rename_columns(df)
    return adjust_values(df)


def process_data():
    """ Clean and process data. Return a dictionary. """
    df = get_data()
    df = cleaned_data(df)
    df_survived = df[df.died == 0]
    df_died = df[df.died == 1]
    # Assign survival rate
    survival_rate = (1 - df_died.size / df_survived.size) * 100
    print(survival_rate)
    # Assign died only df
    died_covid_only_df = df_died[df_died.covid_positive == 1]
    #
    died_covid_age = died_covid_only_df.groupby('age').count().died
    died_covid_only_df = died_covid_only_df[
        [
            'pneumonia',
            'diabetes',
            'copd',
            'asthma',
            'inmsupr',
            'hypertension',
            'other_disease',
            'cardiovascular',
            'obesity',
            'renal_chronic',
            'tobacco'
        ]]
    died_covid_only_df = died_covid_only_df.replace(0, np.nan)
    comorbidity_counts = died_covid_only_df.count()
    return {
        "survival_rate": survival_rate,
        "died_covid_age": died_covid_age.to_dict(),
        "comorbidity": comorbidity_counts.to_dict()
            }
