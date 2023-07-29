from flask import Flask, request, jsonify, render_template
from utils import Churn
import config

app = Flask(__name__)

@app.route('/churn_model')
def home1():
    
    return render_template('churn_model.html')


@app.route('/predict_churn', methods = ['GET', 'POST'])
def predict_churn():

    if request.method == 'GET':
        data = request.args.get
        print("Data :",data)
        CreditScore = float(data('CreditScore'))
        Age = float(data('Age'))
        Tenure = float(data('Tenure'))
        Balance = float(data('Balance'))
        NumOfProducts = float(data('NumOfProducts'))
        HasCrCard = float(data('HasCrCard'))
        IsActiveMember = float(data('IsActiveMember'))
        EstimatedSalary = float(data('EstimatedSalary'))
        Geography = data('Geography')
        Gender = data('Gender')

        Obj = Churn(CreditScore,Age,Tenure,Balance,NumOfProducts,HasCrCard,IsActiveMember,EstimatedSalary,Geography,Gender)
        pred_churn = Obj.get_predicted_churn()
        
    
        return render_template('churn_model.html', prediction = pred_churn)

    elif request.method == 'POST':
        data = request.form
        print("Data :",data)
        CreditScore = data['CreditScore']
        Age = data['Age']
        Tenure = data['Tenure']
        Balance = data['Balance']
        NumOfProducts = data['NumOfProducts']
        HasCrCard = data['HasCrCard']
        IsActiveMember = data['IsActiveMember']
        EstimatedSalary = data['EstimatedSalary']
        EstimatedSalary = data['Geography']
        Gender = data['Gender']
    

        Obj = Churn(CreditScore,Age,Tenure,Balance,NumOfProducts,HasCrCard,IsActiveMember,EstimatedSalary,Geography,Gender)
        pred_churn = Obj.get_predicted_churn()
        
    
        return render_template('churn_model.html', prediction = pred_churn)

    return jsonify({"Message" : "Unsuccessful"})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=config.PORT_NUMBER)