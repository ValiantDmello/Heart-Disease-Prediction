from flask import Flask, render_template, url_for, request, redirect
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

app = Flask(__name__)

@app.route('/')
def index():
   return render_template('index.html')

@app.route('/success/<res>')
def success(res):
   return render_template('success.html', result = res)
#def success(namei, agei, sexi, cpi, trestbpsi, choli, fbsi, restcgi, thalachi, exangi, oldpeaki,slopei, cai, thali):
#   return render_template('heartsuccess.html', name1 = namei, age1 = agei, sex1 = sexi, cp1 = cpi, trestbps1 = trestbpsi,
#            chol1 = choli, fbs1 = fbsi, restcg1 = restcgi, thalach1 = thalachi, exang1 = exangi, oldpeak1 = oldpeaki,slope1 = slopei, ca1 = cai, thal1 = thali)



@app.route('/heartpred')
def heartpred():
   return render_template('HeartPred.html')

@app.route('/heartresults', methods = ['POST', 'GET'])
def heartresults():
   if request.method == 'POST':
      name = request.form['name']
      age = request.form['age']
      sex = request.form['sex']
      cp = request.form['cp']
      trestbps = request.form['trestbps']
      chol = request.form['chol']
      fbs = request.form['fbs']
      restecg = request.form['restecg']
      thalach = request.form['thalach']
      exang = request.form['exang']
      oldpeak  = request.form['oldpeak']
      slope = request.form['slope']
      ca = request.form['ca']
      thal = request.form['thal']

      if(sex=='Female'):
         sex=0
      else:
         sex=1
      
      if(cp == 'typical anigna'):
         cp = 0
      elif(cp == 'atypical anigna'):
         cp = 1
      elif(cp == 'non-anignal pain'):
         cp = 2
      else:
         cp = 3

      if (int(fbs)>120):
         fbs = 1
      else: 
         fbs = 0

      if(restecg == 'NORMAL'):
         restecg = 0
      elif(restecg == 'HAVING ST-T ABNORMALITY'):
         restecg = 1
      else:
         restecg = 2

      if(exang == 'YES'):
         exang = 1
      else:
         exang = 0

      if(slope == 'UNSLOPING'):
         slope = 0
      elif(slope == 'FLAT'):
         slope = 1
      else:
         slope = 2

      if(thal == 'NORMAL'):
         thal = 1
      elif(thal == 'FIXED DEFECT'):
         thal = 2
      else:
         thal = 3
      
      

      lis = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]
      

      

      datas = pd.read_csv("heart1.csv")
      datas.head(10)

      X = datas.iloc[:,:-1].values
      y = datas.iloc[:,-1].values

      from sklearn.preprocessing import StandardScaler
      sc_X = StandardScaler()
      XSc = sc_X.fit_transform(X)

      from sklearn.neighbors import KNeighborsClassifier
      knn = KNeighborsClassifier(n_neighbors=13)
      knn.fit(XSc,y)

      #vals = np.array([lis])

      pred = knn.predict(np.array([lis]))
      if (pred[0]==0):
         strin = "Not Detected"
      else:
         strin = "Detected"

      return redirect(url_for('success', res = strin))
      #return redirect(url_for('heartsuccess',namei = name , agei = age, sexi = sex, cpi = cp, trestbpsi = trestbps,
      #     choli = chol, fbsi = fbs, restcgi = restecg, thalachi = thalach, exangi = exang, oldpeaki = oldpeak,slopei = slope, cai = ca, thali = thal))
      

if __name__ == '__main__':
   app.run(debug=True)
