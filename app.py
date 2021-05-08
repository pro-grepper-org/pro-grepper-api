from flask import Flask,request,jsonify
from flask_cors import CORS, cross_origin
from predict import preprocess
import joblib

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

vectorizer = joblib.load('vectorizer_new.sav')
loaded_model = joblib.load('company_tags_lbps_lg_new.sav')

companies_30 = ['microsoft', 'zoho', 'google', 'cisco', 'adobe', 'samsung', 'amazon',
       'goldman-sachs', 'accolite', 'flipkart', 'de-shaw', 'factset',
       'makemytrip', 'snapdeal', 'vmware', 'oyo-rooms', 'walmart', 'paytm',
       'ebay', 'morgan-stanley', 'sap', 'facebook', 'oracle', 'apple',
       'linkedin', 'yahoo', 'salesforce', 'bloomberg', 'bytedance', 'uber']

@app.route('/api/companies',methods = ['POST'])
def get_company_tags():
    if request.method == 'POST':

      data = request.get_json()
      
      if 'problem-statement' not in data.keys():
        return jsonify(
            message='problem statement missing',
            success='fail'
        ) 
      if 'tags' not in data.keys():
        return jsonify(
            message='tags missing',
            success='fail'
        ) 
      if 'num-companies' not in data.keys():
        return jsonify(
            message='num companies missing',
            success='fail'
        ) 

      ps = data['problem-statement']
      tags = data['tags']
      num = int(data['num-companies'])
      
      for tag in tags:
        ps += " "
        ps += tag

      new_prob = preprocess(ps)
      print(new_prob)

      x = vectorizer.transform(new_prob)
      result = loaded_model.predict_proba(x)
      f_result = result.toarray()

      print(f_result)
      top_num = f_result.argsort()[0][-num:]

      company_data = []
      print(top_num)
      top_num = top_num[::-1]
      
      for idx in top_num:
        company_data.append({
          'name':companies_30[idx],
          'probab':f_result[0][idx]
        })

      return jsonify(
          message='extracted successfully',
          success='ok',
          company_data = company_data
      )

if __name__ == '__main__':
    app.run()