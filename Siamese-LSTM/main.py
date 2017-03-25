import os
import subprocess
from flask import Flask,flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
from flask_socketio import SocketIO, send, emit, join_room, leave_room, \
            Namespace
import json

from lstm import *
sls=lstm("bestsem.p",load=True,training=False)
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
    sa = data["sa"]
    sb = data["sa"]
    print sls.predict_similarity(sa,sb)*4.0+1.0
    
    print sls.chkterr2(test) #Mean Squared Error,Pearson, Spearman
    
if __name__ == "__main__":
    socketio.run(app, host='0.0.0.0') 
