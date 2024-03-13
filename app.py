from flask import Flask,request, url_for, redirect, render_template
import pickle
import numpy as np

model=pickle.load(open('lr_model.pkl','rb'))

app = Flask(__name__,template_folder='templates')
@app.route("/")
def home():
    return render_template('homepage.html')

@app.route('/predict',methods=['POST','GET'])
def predict():
    if request.method == "POST":
        l = []
        gender = int(request.form["gender"])
        pneu = int(request.form["pneu"])
        age = int(request.form["age"])
        preg = int(request.form["preg"])
        asth = int(request.form["asth"])
        card = int(request.form["card"])
        obs = int(request.form["obs"])
        icu = int(request.form["icu"])
        l.append(gender)
        l.append(pneu)
        l.append(age)
        l.append(preg)
        l.append(asth)
        l.append(card)
        l.append(obs)
        l.append(icu)
        final=[np.array(l)]
        print(l)
        print(final)
        output=model.predict(final)[0]
        return render_template('homepage.html',pred='Your Forest is in Danger.\nProbability of fire occuring is {}'.format(output))

   
    

app.run(debug=True) 

