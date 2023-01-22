import pickle
import json
import pandas as pd
import numpy as np
import config


class DiabetesDisease():
    def __init__(self,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age):
        self.Glucose = Glucose
        self.BloodPressure = BloodPressure
        self.SkinThickness = SkinThickness
        self.Insulin = Insulin
        self.BMI = BMI
        self.DiabetesPedigreeFunction = DiabetesPedigreeFunction
        self.Age = Age

    def load_model(self):
        with open(config.MODEL_FILE_PATH, "rb") as f:
            self.model = pickle.load(f)

        with open(config.JSON_FILE_PATH, "r") as f:
            self.json_data = json.load(f)


    def get_Diabetes_Disease(self):

        self.load_model()  # calling load_file method to get

        array = np.zeros(len(self.json_data['column']))

        array[0] = self.Glucose
        array[1] = self.BloodPressure
        array[2] = self.SkinThickness
        array[3] = self.Insulin
        array[4] = self.BMI
        array[5] = self.DiabetesPedigreeFunction
        array[6] = self.Age

        print("Test Array -->\n",array)
        DiabetesDisease = self.model.predict([array])[0]
        return np.around(DiabetesDisease, 2)
    





if __name__ == "__main__":

    Glucose = 188
    BloodPressure= 55
    SkinThickness = 25
    Insulin = 0
    BMI = 25.600
    DiabetesPedigreeFunction = 0.52
    Age = 45

    dd = DiabetesDisease(Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age)
    disease = dd.get_Diabetes_Disease()
    print()
    print(f"Patient predicted as diabetes disease {disease}")
    # if disease == 1:
    #     print('yes patient has a heart disease')
    # else:
    #     print('patient has not a heart disease')
