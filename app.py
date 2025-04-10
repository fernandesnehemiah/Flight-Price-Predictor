from flask import Flask, request, render_template
import sklearn
import pickle
import pandas as pd
import os


app = Flask(__name__)

model_path = os.path.join("notebook", "flight.pkl")
with open(model_path, "rb") as file:
    model = pickle.load(file)


@app.route("/")
def index():
    accuracy_path = os.path.join("notebook", "AccuracyValues.txt")
    with open(accuracy_path, "r") as f:
        lines = f.readlines()


    accuracy_ETR = round(float(lines[0].strip()),3)
    accuracy_LM = round(float(lines[1].strip()),3)
    accuracy_RF = round(float(lines[2].strip()),3)
    accuracy_XGB = round(float(lines[3].strip()),3)
    r2_score_etr = round(float(lines[4].strip()),3)
    r2_score_lr = round(float(lines[5].strip()),3)
    r2_score_rf = round(float(lines[6].strip()),3)
    r2_score_xgb = round(float(lines[7].strip()),3)

    return render_template("index.html" , accuracy_etr = accuracy_ETR , accuracy_lr = accuracy_LM , accuracy_rf = accuracy_RF , accuracy_xgb = accuracy_XGB , r2_score_etr = r2_score_etr , r2_score_lr = r2_score_lr , r2_score_rf = r2_score_rf , r2_score_xgb = r2_score_xgb)

@app.route("/predict", methods = ["GET", "POST"])
def predict():
    if request.method == "POST":

        date_dep = request.form["departure"]
        journey_day = int(pd.to_datetime(date_dep, format="%Y-%m-%dT%H:%M").day)
        journey_month = int(pd.to_datetime(date_dep, format ="%Y-%m-%dT%H:%M").month)

        dep_hour = int(pd.to_datetime(date_dep, format ="%Y-%m-%dT%H:%M").hour)
        dep_min = int(pd.to_datetime(date_dep, format ="%Y-%m-%dT%H:%M").minute)
        # print("Departure : ",Dep_hour, Dep_min)

        date_arr = request.form["arrival"]
        arrival_hour = int(pd.to_datetime(date_arr, format ="%Y-%m-%dT%H:%M").hour)
        arrival_min = int(pd.to_datetime(date_arr, format ="%Y-%m-%dT%H:%M").minute)

        Duration_hour = abs(arrival_hour - dep_hour)
        Duration_mins = abs(arrival_min - dep_min)

        Total_Stops = int(float(request.form["stopage"]))



        airline=request.form['airline']
        if(airline=='Jet Airways'):
            Airline_JetAirways = 1
            Airline_IndiGo = 0
            Airline_AirIndia = 0
            Airline_MultipleCarriers = 0
            Airline_SpiceJet = 0
            Airline_Vistara = 0
            Airline_AirAsia = 0
            Airline_GoAir = 0
            Airline_MultipleCarriersPremiumEconomy = 0
            Airline_JetAirwaysBusiness = 0
            Airline_VistaraPremiumEconomy = 0
            Airline_Trujet = 0

        elif (airline=='Indigo'):
            Airline_JetAirways = 0
            Airline_IndiGo = 1
            Airline_AirIndia = 0
            Airline_MultipleCarriers = 0
            Airline_SpiceJet = 0
            Airline_Vistara = 0
            Airline_AirAsia = 0
            Airline_GoAir = 0
            Airline_MultipleCarriersPremiumEconomy = 0
            Airline_JetAirwaysBusiness = 0
            Airline_VistaraPremiumEconomy = 0
            Airline_Trujet = 0

        elif (airline=='Air India'):
            Airline_JetAirways = 0
            Airline_IndiGo = 0
            Airline_AirIndia = 1
            Airline_MultipleCarriers = 0
            Airline_SpiceJet = 0
            Airline_Vistara = 0
            Airline_AirAsia = 0
            Airline_GoAir = 0
            Airline_MultipleCarriersPremiumEconomy = 0
            Airline_JetAirwaysBusiness = 0
            Airline_VistaraPremiumEconomy = 0
            Airline_Trujet = 0
        elif (airline=='Multiple carriers'):
            Airline_JetAirways = 0
            Airline_IndiGo = 0
            Airline_AirIndia = 0
            Airline_MultipleCarriers = 1
            Airline_SpiceJet = 0
            Airline_Vistara = 0
            Airline_AirAsia = 0
            Airline_GoAir = 0
            Airline_MultipleCarriersPremiumEconomy = 0
            Airline_JetAirwaysBusiness = 0
            Airline_VistaraPremiumEconomy = 0
            Airline_Trujet = 0
        elif (airline=='SpiceJet'):
            Airline_JetAirways = 0
            Airline_IndiGo = 0
            Airline_AirIndia = 0
            Airline_MultipleCarriers = 0
            Airline_SpiceJet = 1
            Airline_Vistara = 0
            Airline_AirAsia = 0
            Airline_GoAir = 0
            Airline_MultipleCarriersPremiumEconomy = 0
            Airline_JetAirwaysBusiness = 0
            Airline_VistaraPremiumEconomy = 0
            Airline_Trujet = 0
        elif (airline=='Vistara'):
            Airline_JetAirways = 0
            Airline_IndiGo = 0
            Airline_AirIndia = 0
            Airline_MultipleCarriers = 0
            Airline_SpiceJet = 0
            Airline_Vistara = 1
            Airline_AirAsia = 0
            Airline_GoAir = 0
            Airline_MultipleCarriersPremiumEconomy = 0
            Airline_JetAirwaysBusiness = 0
            Airline_VistaraPremiumEconomy = 0
            Airline_Trujet = 0
        elif (airline=='Air Asia'):
            Airline_JetAirways = 0
            Airline_IndiGo = 0
            Airline_AirIndia = 0
            Airline_MultipleCarriers = 0
            Airline_SpiceJet = 0
            Airline_Vistara = 0
            Airline_AirAsia = 1
            Airline_GoAir = 0
            Airline_MultipleCarriersPremiumEconomy = 0
            Airline_JetAirwaysBusiness = 0
            Airline_VistaraPremiumEconomy = 0
            Airline_Trujet = 0
        elif (airline=='GoAir'):
            Airline_JetAirways = 0
            Airline_IndiGo = 0
            Airline_AirIndia = 0
            Airline_MultipleCarriers = 0
            Airline_SpiceJet = 0
            Airline_Vistara = 0
            Airline_AirAsia = 0
            Airline_GoAir = 1
            Airline_MultipleCarriersPremiumEconomy = 0
            Airline_JetAirwaysBusiness = 0
            Airline_VistaraPremiumEconomy = 0
            Airline_Trujet = 0
        elif (airline=='Multiple carriers Premium economy'):
            Airline_JetAirways = 0
            Airline_IndiGo = 0
            Airline_AirIndia = 0
            Airline_MultipleCarriers = 0
            Airline_SpiceJet = 0
            Airline_Vistara = 0
            Airline_AirAsia = 0
            Airline_GoAir = 1
            Airline_MultipleCarriersPremiumEconomy = 0
            Airline_JetAirwaysBusiness = 0
            Airline_VistaraPremiumEconomy = 0
            Airline_Trujet = 0
        elif (airline=='Jet Airways Business'):
            Airline_JetAirways = 0
            Airline_IndiGo = 0
            Airline_AirIndia = 0
            Airline_MultipleCarriers = 0
            Airline_SpiceJet = 0
            Airline_Vistara = 0
            Airline_AirAsia = 0
            Airline_GoAir = 1
            Airline_MultipleCarriersPremiumEconomy = 0
            Airline_JetAirwaysBusiness = 0
            Airline_VistaraPremiumEconomy = 0
            Airline_Trujet = 0
        elif (airline=='Vistara Premium economy'):
            Airline_JetAirways = 0
            Airline_IndiGo = 0
            Airline_AirIndia = 0
            Airline_MultipleCarriers = 0
            Airline_SpiceJet = 0
            Airline_Vistara = 0
            Airline_AirAsia = 0
            Airline_GoAir = 1
            Airline_MultipleCarriersPremiumEconomy = 0
            Airline_JetAirwaysBusiness = 0
            Airline_VistaraPremiumEconomy = 0
            Airline_Trujet = 0

        else:
            Airline_JetAirways = 0
            Airline_IndiGo = 0
            Airline_AirIndia = 0
            Airline_MultipleCarriers = 0
            Airline_SpiceJet = 0
            Airline_Vistara = 0
            Airline_AirAsia = 0
            Airline_GoAir = 0
            Airline_MultipleCarriersPremiumEconomy = 0
            Airline_JetAirwaysBusiness = 0
            Airline_VistaraPremiumEconomy = 0
            Airline_Trujet = 1


        Source = request.form["source"]
        if (Source == 'Delhi'):
            Source_Delhi = 1
            Source_Kokata = 0
            Source_Banglore = 0
            Source_Mumbai = 0
            Source_Chennai = 0

        elif (Source == 'Kolkata'):
            Source_Delhi = 0
            Source_Kokata = 1
            Source_Banglore = 0
            Source_Mumbai = 0
            Source_Chennai = 0
        elif (Source == 'Banglore'):
            Source_Delhi = 0
            Source_Kokata = 0
            Source_Banglore = 1
            Source_Mumbai = 0
            Source_Chennai = 0
        elif (Source == 'Mumbai'):
            Source_Delhi = 0
            Source_Kokata = 0
            Source_Banglore = 0
            Source_Mumbai = 1
            Source_Chennai = 0
        else:
            Source_Delhi = 0
            Source_Kokata = 0
            Source_Banglore = 0
            Source_Mumbai = 0
            Source_Chennai = 1


        destination = request.form["destination"]
        if (destination == 'Cochin'):
            destination_Cochin =1
            destination_Banglore=0 
            destination_Delhi=0 
            destination_NewDelhi =0
            destination_Hyderabad =0
            destination_Kolkata =0
            
        elif (destination == 'Banglore'):
            destination_Cochin =0
            destination_Banglore =1
            destination_Delhi =0
            destination_NewDelhi =0
            destination_Hyderabad =0
            destination_Kolkata =0
            
        elif (destination == 'Delhi'):
            destination_Cochin =0
            destination_Banglore =0
            destination_Delhi =1
            destination_NewDelhi =0
            destination_Hyderabad =0
            destination_Kolkata =0

        elif (destination == 'New Delhi'):
            destination_Cochin =0
            destination_Banglore =0
            destination_Delhi =0
            destination_NewDelhi =1
            destination_Hyderabad =0
            destination_Kolkata =0

        elif (destination == 'Hyderabad'):
            destination_Cochin =0
            destination_Banglore =0
            destination_Delhi =0
            destination_NewDelhi =0
            destination_Hyderabad =1
            destination_Kolkata =0

        else:
            destination_Cochin =0
            destination_Banglore =0
            destination_Delhi =0
            destination_NewDelhi =0
            destination_Hyderabad =0
            destination_Kolkata =1
           

        prediction=model.predict([[
            Total_Stops,
            arrival_hour,
            arrival_min,
            dep_hour,
            dep_min,
            arrival_hour,
            arrival_min,
            Duration_hour,
            Duration_mins,
            Source_Chennai,
            Source_Delhi,
            Source_Kokata,
            Source_Mumbai,
            destination_Cochin,
            destination_Delhi,
            destination_Hyderabad,
            destination_Kolkata,
            destination_NewDelhi,
            Airline_AirIndia,
            Airline_GoAir,
            Airline_IndiGo,
            Airline_JetAirways,
            Airline_JetAirwaysBusiness,
            Airline_MultipleCarriers,
            Airline_MultipleCarriersPremiumEconomy,
            Airline_SpiceJet,
            Airline_Trujet,
            Airline_Vistara,
            Airline_VistaraPremiumEconomy,
            
        ]])

        output=round(prediction[0],2)

        return render_template('predict.html',prediction_text="Your Flight price is Rs. {}".format(output))

    return render_template("predict.html")


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  
    app.run(host="0.0.0.0", port=port)

