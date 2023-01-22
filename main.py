from flask import Flask, jsonify, render_template, request
from model.utils import DiabetesDisease
import config

app = Flask(__name__)

@app.route('/')
def hello_flask():
    print("Welcome")
    return render_template("index.html")
    # return "Success"

@app.route('/predicted_diabetes',methods = ['GET','POST'])
def get_Diabetes_Disease():
    if request.method == 'GET':
        print('we are using Get method')
    
        data = request.form
        print("Data-->",data)

        # Glucose = data["Glucose"]
        # BloodPressure = data["BloodPressure"]
        # SkinThickness = data["SkinThickness"]
        # Insulin = data["Insulin"]
        # BMI = data["BMI"]
        # DiabetesPedigreeFunction = data["DiabetesPedigreeFunction"]
        # Age = data["Age"]

        Glucose = int(request.args.get('Glucose'))
        BloodPressure = int(request.args.get('BloodPressure'))
        SkinThickness = int(request.args.get('SkinThickness'))
        Insulin = int(request.args.get('Insulin'))
        BMI = float(request.args.get('BMI'))
        DiabetesPedigreeFunction = float(request.args.get('DiabetesPedigreeFunction'))
        Age = int(request.args.get('Age'))

        print('Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age',Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age)

        dd = DiabetesDisease(Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age)
        disease = dd.get_Diabetes_Disease()
        if disease == 0:
            print("The patient has no symptoms of diabetes,he is well.")
            return render_template("index.html", prediction='The patient has no symptoms of diabetes.')
        else:
            print("The patient has symptoms of diabetes,he should seek treatment.")
            return render_template("index.html", prediction='The patient has symptoms of diabetes.')

    else: 
        print('we are using POST method')
     

        Glucose = int(request.form.get('Glucose'))
        BloodPressure = int(request.form.get('BloodPressure'))
        SkinThickness = int(request.form.get('SkinThickness'))
        Insulin = int(request.form.get('Insulin'))
        BMI = float(request.form.get('BMI'))
        DiabetesPedigreeFunction = float(request.form.get('DiabetesPedigreeFunction'))
        Age = int(request.form.get('Age'))

        print('Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age',Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age)

        dd = DiabetesDisease(Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age)
        disease = dd.get_Diabetes_Disease()

        # if disease =='yes':
        #     return jsonify({"Result" : f"{disease}: This is Dibetics patient"})
        # else:
        #     return jsonify({"Result" : f"{disease}: This is not Dibetics patient"})
        
        if disease == 0:           
            return render_template("index.html", prediction='The patient has no symptoms of diabetes,he is well.')
        else:
            return render_template("index.html", prediction='The patient has symptoms of diabetes,he should seek treatment.')
  

  

if __name__ == "__main__":
    app.run(host = '0.0.0.0', port = 5050, debug = True)