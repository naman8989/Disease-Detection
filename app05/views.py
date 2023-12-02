from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.template import loader
import requests

import pandas as pd;
import numpy as np;
from sklearn import linear_model;
from sklearn.linear_model import LogisticRegression;
from sklearn.model_selection import train_test_split;

diaFile = pd.read_csv('app05/app05/diabetes_012_health_indicators_BRFSS2015.csv');
lungCancerFile = pd.read_csv('app05/app05/lung_Cancer.csv');
lungCancerFile = lungCancerFile.drop(columns='index',axis=1);
lungCancerFile = lungCancerFile.drop(columns='Patient Id',axis=1);
lungCancerFile['Level'].replace(to_replace=["Low", "Medium", "High"], value = [1, 2, 3], inplace = True);


y_diabetes = diaFile['Diabetes_012'];
x_diabetes = diaFile.drop(columns='Diabetes_012', axis=1);
y_lungCancer = lungCancerFile['Level'];
x_lungCancer = lungCancerFile.drop(columns='Level', axis=1);


x_train_diabetes, x_test_diabetes, y_train_diabetes, y_test_diabetes = train_test_split(x_diabetes,y_diabetes,test_size=0.001,train_size=0.001, random_state=3500)
x_train_lungCancer, x_test_lungCancer, y_train_lungCancer, y_test_lungCancer = train_test_split(x_lungCancer,y_lungCancer,test_size=0.1,train_size=0.1, random_state=100)


logReg_diabetes = linear_model.LogisticRegression()
logReg_diabetes.fit(x_train_diabetes.values,y_train_diabetes.values)
logReg_lungCancer = linear_model.LogisticRegression()
logReg_lungCancer.fit(x_train_lungCancer.values,y_train_lungCancer.values)




def members(request):
    return HttpResponse("Hello world!")


template = loader.get_template('home.html')
def homePage(request):
    return render(request,'home.html')


def diabetesPage(request):
    print('in diabetesPage');
    predictResult = None;
    try:
        if request.method == 'GET':
            print(request.method)

            HighBP = int(request.GET['HighBP']);
            HighChol = int(request.GET['HighChol']);
            CholCheck = int(request.GET['CholCheck']);
            bodyBMI = int(request.GET['bodyBMI']);
            Smoker = int(request.GET['Smoker']);
            Stroke = int(request.GET['Stroke']);
            HeartDiseaseAttack = int(request.GET['HeartDiseaseAttack']);
            PhysActivity = int(request.GET['PhysActivity']);
            Fruits = int(request.GET['Fruits']);
            Veggies = int(request.GET['Veggies']);
            HvyAlcoholCons = int(request.GET['HvyAlcoholCons']);
            AnyHealthCare = int(request.GET['AnyHealthCare']);
            NoDocbcCost = int(request.GET['NoDocbcCost']);
            GenHelth = int(request.GET['GenHelth']);
            MentHlth = int(request.GET['MentHlth']);
            PhyHlth = int(request.GET['PhyHlth']);
            DiffWalk = int(request.GET['DiffWalk']);
            Sex = int(request.GET['Sex']);
            Age = int(request.GET['Age']);
            Education = int(request.GET['Education']);
            Income = int(request.GET['Income']);
            # print(HighBP,HighChol,CholCheck,bodyBMI,Smoker,Stroke,HeartDiseaseAttack,PhysActivity,Fruits,Veggies,HvyAlcoholCons,AnyHealthCare,NoDocbcCost,GenHelth,MentHlth,PhyHlth,DiffWalk,Sex,Age,Education,Income);
            # http://127.0.0.1:8080/?HighBP=0&HighChol=0&CholCheck=0&bodyBMI=50&Smoker=1&Stroke=1&HeartDiseaseAttack=1&PhysActivity=0&Fruits=0&Veggies=0&HvyAlcoholCons=1&AnyHealthCare=0&NoDocbcCost=1&GenHelth=5&MentHlth=20&PhyHlth=15&DiffWalk=0&Sex=1&Age=1&Education=3&Income=1
            predictResult = logReg_diabetes.predict( ( [ [HighBP,HighChol,CholCheck,bodyBMI,Smoker,Stroke,HeartDiseaseAttack,PhysActivity,Fruits,Veggies,HvyAlcoholCons,AnyHealthCare,NoDocbcCost,GenHelth,MentHlth,PhyHlth,DiffWalk,Sex,Age,Education,Income]   ] ) );
            # print('predicted Result is :- ',predictResult)
            predictResult = int(predictResult[0])

        else:
            print('not in get')
    except:
        print('not found in get')

    if predictResult is not None:
        if predictResult == 1:
            pred_comment = 'There is some possibility that you might have diabetes. Please consult a doctor as soon as possible'
        elif predictResult == 0:
            pred_comment = 'There is none possibility that you might have diabetes but if you doesn\'t feel confident about our result, it better to consult a doctor and take a test.'
        elif predictResult == 2:
            pred_comment = 'There is High posibility that you may have diabetes.'
        else:
            pred_comment = 'Some Error came up. Try again !'
    else:
        pred_comment = 'No input !!'
        predictResult = 'None'

    diabetes_send = {
        "predicted": predictResult,
        "predicted_comment": pred_comment
    }

    # return render(request,'home.html',{'predictResult': json.dumps(diabetes_send)},content_type='application/html')
    return JsonResponse(diabetes_send)


def lungCancerPage(request):
    print('in lungCancerPage');
    predictResult = None;
    try:
        if request.method == 'GET':
            print(request.method);

            Age = int(request.GET['Age']);
            Gender = int(request.GET['Gender']);
            AirPollution = int(request.GET['AirPollution']);
            AlcoholUse = int(request.GET['AlcoholUse']);
            DustAllergy = int(request.GET['DustAllergy']);
            OccuPationalHazards = int(request.GET['OccuPationalHazards']);
            GeneticRisk = int(request.GET['GeneticRisk']);
            chronicLungDisease = int(request.GET['chronicLungDisease']);
            BalancedDiet = int(request.GET['BalancedDiet']);
            Obesity = int(request.GET['Obesity']);
            Smoking = int(request.GET['Smoking']);
            PassiveSmoker = int(request.GET['PassiveSmoker']);
            ChestPain = int(request.GET['ChestPain']);
            CoughingOfBlood = int(request.GET['CoughingOfBlood']);
            Fatigue = int(request.GET['Fatigue']);
            WeightLoss = int(request.GET['WeightLoss']);
            ShortnessOfBreath = int(request.GET['ShortnessOfBreath']);
            Wheezing = int(request.GET['Wheezing']);
            SwallowingDifficulty = int(request.GET['SwallowingDifficulty']);
            ClubbingOfFingerNails = int(request.GET['ClubbingOfFingerNails']);
            FrequentCold = int(request.GET['FrequentCold']);
            DryCough = int(request.GET['DryCough']);
            Snoring = int(request.GET['Snoring']);
            # http://127.0.0.1:8080/?Age=21&Gender=1&AirPollution=4&AlcoholUse=2&DustAllergy=2&OccuPationalHazards=3&GeneticRisk=2&chronicLungDisease=1&BalancedDiet=6&Obesity=4&Smoking=3&PassiveSmoker=3&ChestPain=1&CoughingOfBlood=3&Fatigue=2&WeightLoss=2&ShortnessOfBreath=2&Wheezing=3&SwallowingDifficulty=1&ClubbingOfFingerNails=1&FrequentCold=3&DryCough=1&Snoring=2
            predictResult = logReg_lungCancer.predict( ( [[Age,Gender,AirPollution,AlcoholUse,DustAllergy,OccuPationalHazards,GeneticRisk,chronicLungDisease,BalancedDiet,Obesity,Smoking,PassiveSmoker,ChestPain,CoughingOfBlood,Fatigue,WeightLoss,ShortnessOfBreath,Wheezing,SwallowingDifficulty,ClubbingOfFingerNails,FrequentCold,DryCough,Snoring] ] ) );
            predictResult = int(predictResult[0]);
            # print('Result of lung cancer is :- ', predictResult);
        else:
            print('not in get');
    except:
        print('not found in get')

    if predictResult is not None:
        if predictResult == 1:
            pred_comment = 'There is low possibility that you might have Lung cancer. But if you still doesn\'t feel confifent please consult a doctor. '
        elif predictResult == 2:
            pred_comment = 'There is mild possibility that you might have Lung Cancer. Please consult a doctor as soon as possible. '
        elif predictResult == 3:
            pred_comment = 'There is High posibility that you might have Lung Cancer or can get in future. Please see doctor immediately.'
        else:
            pred_comment = 'Some Error came up. Try again !'
    else:
        pred_comment = 'No input !!'
        predictResult = 'None'

    lungCancer_send = {
        "predicted": predictResult,
        "predicted_comment": pred_comment
    }
    print('the type is ',type(lungCancer_send));

    # return render(request,'home.html',{'predictResult': lungCancer_send})
    return JsonResponse(lungCancer_send)


