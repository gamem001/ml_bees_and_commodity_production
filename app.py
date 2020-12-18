import flask
import numpy as np
import pandas as pd
import sqlalchemy
from flask import Flask, jsonify, render_template
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine


engine = create_engine("sqlite:///the_hive.db")
session = Session(engine)

app = Flask(__name__)


@app.route("/", methods=['GET'])
def homepage():
    return render_template('index.html')

@app.route("/home", methods=['GET'])
def welcome():
    return(
        f"The Hive<br/>"
        f"Avaialble Routes:<br/>"
        f"/api/v1.0/col<br/>"
        f"/api/v1.0/commo<br/>"
        f"/api/v1.0/honey<br/>"
        f"/api/v1.0/mrkt<br/>"
        f"/api/v1.0/temp<br/>"
        f"/api/v1.0/decline<br/>"
)

@app.route("/api/v1.0/col", methods=['GET'])
def colonies():
    colony_data = pd.read_sql('SELECT * FROM colony', con=engine)
    
    colony_dict = colony_data.to_dict('records')

    return jsonify(colony_dict)
    
    session.close()
    

@app.route("/api/v1.0/commo", methods=['GET'])
def commodities():
    return

@app.route("/api/v1.0/honey", methods=['GET'])
def honey():
    honey_data = pd.read_sql('SELECT * FROM honey_prod', con=engine)
    
    honey_dict = honey_data.to_dict('records')

    return jsonify(honey_dict)
    
    session.close()
    



@app.route("/api/v1.0/mrkt", methods=['GET'])
def mrkt():
    return
    


@app.route("/api/v1.0/temp", methods=['GET'])
def temp():
    return


@app.route("/api/v1.0/decline", methods=['GET'])
def decline():
    decline_data = pd.read_sql('SELECT * FROM decline WHERE year = 2019', con=engine)
    
    decline_dict = decline_data.to_dict('records')

    return jsonify(decline_dict)
    
    session.close()

if __name__ == "__main__":
    app.run(debug=True)