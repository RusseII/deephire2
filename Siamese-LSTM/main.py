import os
import subprocess
from flask import Flask,flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
import json

from code.lstm import *

sls=lstm("code/bestsem.p",load=True,training=False)
async_mode = None

app = Flask(__name__)



@app.route('/', methods=['GET', 'POST'] )
def upload_file():
    return render_template("index.html")


@app.route('/sim', methods=['GET', 'POST'] )
def return_sim():
    data = json.loads(request.data)
    print data
    sa = data["sa"]
    sb = data["sb"]
    index= sls.predict_similarity(sa,sb)*4.0+1.0
    print index 
    return str(index)
    #print sls.chkterr2(test) #Mean Squared Error,Pearson, Spearman
    
@app.route('/json', methods=['GET', 'POST'] )
def test():
    x={"people": [ {"questions": ["score1","score2","score2","score3"], "answers": ["a1","a2","a3","a4"], "name": "Russell", "score" : 2.2}, {"name": "Nick", "score" : 1.5}]}
    print type(x)
    return json.dumps(x)




if __name__ == "__main__":
    app.run() 
