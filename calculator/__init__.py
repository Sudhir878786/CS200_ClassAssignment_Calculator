import json
from flask import Flask, render_template, request, jsonify   

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("InputOutput.html")        

@app.route("/add", methods=["POST"])
def ADD(): 
    jsonStr = request.get_json()
    jsonObj = json.loads(jsonStr)
    
    a=int(jsonObj['N1'])
    b=int(jsonObj['N2'])
    sum=a+b
    response = "sum of 2 numbers = " + str(sum)
    return response
    
@app.route("/xyz", methods=["POST"])
def XYZ(): 
    jsonStr = request.get_json()
    jsonObj = json.loads(jsonStr)
    
    a=int(jsonObj['N1'])
    b=int(jsonObj['N2'])
    
    # Logic for function assigned to you as in pdf
    
    return 1

@app.route("/bitAND", methods=["POST"])
def bitAND(): 
    jsonStr = request.get_json()
    jsonObj = json.loads(jsonStr)

    a=int(jsonObj['N1'])
    b=int(jsonObj['N2'])
    num=a&b
    response = "And operator of 2 numbers is " + str(num)
    return response
@app.route("/bitOR",methods=["POST"])
def bitOR():
    jsonStr=request.get_json()
    jsonObj=json.loads(jsonStr)
    a=int(jsonObj['N1'])
    b=int(jsonObj['N2'])
    num=a^b
    response="The Bitwise OR of the two numbers is "+str(num)
    return response

if __name__== "__main__":
    app.run()
