import os
import subprocess
from flask import Flask,flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
import json

from db import db
import string
from code.ats import ATS
from code.lstm import *
sls=lstm("code/bestsem.p",load=True,training=False)

app = Flask(__name__)



@app.route('/', methods=['GET', 'POST'] )
def upload_file():
    return render_template("index.html")


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
def parsedata(data):
    data=str(data)
    data=data.translate(None,string.punctuation)
    return data


@app.route('/json', methods=['GET', 'POST'] )
def test():
    x= { "people": [ {"name": "Russell", "score" : 2.2}, {"name": "Nick", "score" : 1.5}]}
    print type(x)
    return json.dumps(x)
    


#shitiest code award??
@app.route('/get_data', methods=['GET', 'POST'] )
def get_data():
    ats=ATS()
    msg=(ats.get_all())
    questions=["What is your preferred management style?", "Suppose you are on a sales call, and the customer starts getting angry. What would you do?", "How would you deal with a customer who constantly changes deadlines?"]
    answers=["My prefered managment style is hands off but the employer is avaliable for questions", "I stay calm and try to help them nicely", "I would let them know that I am trying to help but constantly changing deadlines is very expensive"]
    obj={}
    ar=[]
    scores=[]
    count=0
    for i,people in enumerate(msg):
        if people!=None:
            a1=people['answers'][0]["answer_value_01"]
            a2=people['answers'][0]["answer_value_02"]
            a3=people['answers'][0]["answer_value_03"]
            a=[a1,a2,a3]
            sa=answers[0]
            sb=parsedata(a1)
            index = sls.predict_similarity(sa,sb)*4.0+1.0
            scores.append(index)

            sa=answers[1]
            sb=parsedata(a2)
            index = sls.predict_similarity(sa,sb)*4.0+1.0
            scores.append(index)

            sa=answers[2]
            sb=parsedata(a3)
            index = sls.predict_similarity(sa,sb)*4.0+1.0
            scores.append(index)
            thescore=int(scores[i])
            thescore=(thescore-1)*100
            if thescore>100:
                thescore=100

            ar.append({"pairs" : [{"employeer_questions": questions[i], "answers": a[i], "scores":thescore}]})
        try:
            pass
        except:
            print "err"
#    return msg[0]['first_name']
        for items in scores:
            count+=count+int(items)
        total=(count-3)*100

    return str(ar)

    
if __name__ == "__main__":
    app.run(port=5555) 
