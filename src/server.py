from flask import Flask
from flask import Flask, jsonify, request, flash
import sys
import gain_calculator

#from py_to_flask import data
#from main import main
#import py_to_flask
app = Flask(__name__)

@app.route("/feminism")
def members():
    #loc_data = py_to_flask.get_json()    
    #loc_data = main()
    jsonify(loc_data)
    return loc_data
    #return {"slava": ["manava", "mem2","mem3"]}

def ret_ticker(tkr):
    return tkr

@app.route('/pp', methods=['GET', 'POST'])
def get_ticker():
    print("foo!!!!!!!!", flush=True)
    print('Hello world!', file=sys.stderr)
    #ticker= request.args.get('language')
    #ticker = request.form['ticker']
    
     
    #flash(request.get_json() )
    if request.get_json() :
        t = request.get_json() #turn json sent from c# into a variable
        print(request.get_json(), file=sys.stderr)
        #print(t["ticker"], file=sys.stderr)
        #print("ticker type 't' is ", type(t))
        t = t["ticker"]
        print("what am I sending to yfinance? Is this the ticker? ", t)

        highest_gain = gain_calculator.gain(str(t))
        #highest_gain = py_to_flask.frm_flask(str(t))
        return highest_gain
        #return str(t)
        #ret_ticker(t) 
        """while(1):
            return str(t)"""
    


if __name__ == "__main__":
    app.run(debug = True)