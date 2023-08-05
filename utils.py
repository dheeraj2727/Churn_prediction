import pickle
import json
import numpy as np
import config


class Churn():
    def __init__(self,CreditScore,Age,Tenure,Balance,NumOfProducts,HasCrCard,IsActiveMember,EstimatedSalary,Geography,Gender):
        print("** INIT Function ***")
        self.CreditScore = CreditScore
        self.Age = Age
        self.Tenure = Tenure
        self.Balance = Balance
        self.NumOfProducts = NumOfProducts
        self.HasCrCard = HasCrCard
        self.IsActiveMember = IsActiveMember
        self.EstimatedSalary = EstimatedSalary
        self.Geography = Geography
        self.Gender = Gender

    def __load_saved_data(self):

        with open(config.MODEL_FILE_PATH,'rb') as f:
            self.model = pickle.load(f)

        with open(config.JSON_FILE_PATH,'r') as f:
            self.json_data = json.load(f)

    def get_predicted_churn(self):
        self.__load_saved_data()

        Geography='Geography_'+ self.Geography
        Gender='Gender_'+ self.Gender

        Geography_index = self.json_data["Column Names"].index(Geography)
        Gender_index = self.json_data["Column Names"].index(Gender)



        test_array = np.zeros([1,self.model.n_features_in_])
        test_array[0,0] = self.CreditScore
        test_array[0,1] = self.Age
        test_array[0,2] = self.Tenure
        test_array[0,3] = self.Balance
        test_array[0,4] = self.NumOfProducts
        test_array[0,5] = self.HasCrCard
        test_array[0,6] = self.IsActiveMember
        test_array[0,7] = self.EstimatedSalary
        test_array[0,Geography_index] = 1
        test_array[0,Gender_index] = 1

        predicted_churn = self.model.predict(test_array)[0]
        if predicted_churn == 1:
            Final_prediction = "Cusotmer will be retained"
        else:
            Final_prediction = "Cusotmer will not be retained"
        
        return Final_prediction
