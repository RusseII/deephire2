import os
import subprocess
from flask import Flask,flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
from flask_socketio import SocketIO, send, emit, join_room, leave_room, \
            Namespace
import json

from db import db
import string
#from lstm import *
#sls=lstm("bestsem.p",load=True,training=False)
async_mode = None

app = Flask(__name__)
socketio = SocketIO(app, async_mode=async_mode)



@app.route('/', methods=['GET', 'POST'] )
def upload_file():
    return render_template("index.html", async_mode=socketio.async_mode)


@app.route('/sim', methods=['GET', 'POST'] )
def return_sim():
    data = json.loads(request.data)
    print data
    sa = str(data["sa"])
    sb = str(data["sb"])
    sa=sa.translate(None, string.punctuation)
    sb=sb.translate(None, string.punctuation)
    print sa
    print sb
    return sa
   # index= sls.predict_similarity(sa,sb)*4.0+1.0
   # print index 
    #return str(index)
    #print sls.chkterr2(test) #Mean Squared Error,Pearson, Spearman


@app.route('/json', methods=['GET', 'POST'] )
def test():
    x= { "people": [ {"name": "Russell", "score" : 2.2}, {"name": "Nick", "score" : 1.5}]}
    print type(x)
    return json.dumps(x)
    
if __name__ == "__main__":
    socketio.run(app, host='0.0.0.0', port=5555) 
