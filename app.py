from flask import Flask,request,jsonify
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

company_data = [
          {'name':'amazon','probab':0.9},
          {'name':'google','probab':0.7},
          {'name':'hsbc','probab':0.6},
          {'name':'oracle','probab':0.4},
          {'name':'yahoo','probab':0.1},
          {'name':'amazon','probab':0.9},
          {'name':'google','probab':0.7},
          {'name':'hsbc','probab':0.6},
          {'name':'oracle','probab':0.4},
          {'name':'yahoo','probab':0.1},
          {'name':'amazon','probab':0.9},
          {'name':'google','probab':0.7},
          {'name':'hsbc','probab':0.6},
          {'name':'oracle','probab':0.4},
          {'name':'yahoo','probab':0.1},
          {'name':'amazon','probab':0.9},
          {'name':'google','probab':0.7},
          {'name':'hsbc','probab':0.6},
          {'name':'oracle','probab':0.4},
          {'name':'yahoo','probab':0.1},
          {'name':'amazon','probab':0.9},
          {'name':'google','probab':0.7},
          {'name':'hsbc','probab':0.6},
          {'name':'oracle','probab':0.4},
          {'name':'yahoo','probab':0.1},
          {'name':'amazon','probab':0.9},
          {'name':'google','probab':0.7},
          {'name':'hsbc','probab':0.6},
          {'name':'oracle','probab':0.4},
          {'name':'yahoo','probab':0.1}
]

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
      
      return jsonify(
          message='extracted successfully',
          success='ok',
          company_data = company_data[:num]
      )

if __name__ == '__main__':
    app.run()