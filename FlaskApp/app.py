# Dependencies
from flask import Flask, request, jsonify
from sklearn.externals import joblib
from flask_cors import CORS,cross_origin
import traceback
import pandas as pd
import numpy as np

# Your API definition
app = Flask(__name__)
CORS(app, support_credentials=True)

@app.route('/')
def hello():
    response = '''
    <div style="background-image: url(&quot;https://www.shughal.com/wp-content/uploads/2015/08/PicMonkey-Collage2.jpg&quot;);background-color: white;background-size: 100%;height: 100%;width: 100%;" background-image="url(&quot;https://www.shughal.com/wp-content/uploads/2015/08/PicMonkey-Collage2.jpg&quot;)">
        <h1 style="
                color: #ccc;
    		background-color: red;
    		box-shadow: 2px;
    		top: 35%;
    		position: fixed;
    		left: 35%;">
        <center>Disaster Prediction System using Animal Behaviour</center>
        </h1>
    </div>
    '''
    return response

@app.route('/predict', methods=['POST', 'GET','OPTIONS'])
def predict():
    if rfc_b:
        try:
            #[('tensed', u'0'), ('Altitude', u'1'), ('dist', u'3'), ('species', u'elephnat'), ('submit', u'')]
            data = request.form
            json_ = {}
            for i,j in data.items():
               if i == "submit": continue
               if i != "Species":
                   json_.setdefault(i, []).append(int(j))
               else:
                   json_.setdefault(i, []).append(j)
            print(json_)
            query = pd.get_dummies(pd.DataFrame(json_))
            query = query.reindex(columns=model_columns, fill_value=0)
            prediction = rfc_b.predict(query)
            print prediction
            if 0 in prediction:
                msg = "The disaster is NOT likely to happen"
            else:
                msg = "The disaster is MORE likely to happen, Please Stay Safe"


            response = '''
            <div style="background-image: url(&quot;https://img-s-msn-com.akamaized.net/tenant/amp/entityid/BBMdr5r.img&quot;);background-color: white;background-size: 100%;height: 100%;width: 100%;" background-image="url(&quot;https://img-s-msn-com.akamaized.net/tenant/amp/entityid/BBMdr5r.img&quot;)">
            <h1 style="
                color: #ccc;
    		background-color: red;
    		box-shadow: 2px;
    		top: 35%;
    		position: fixed;
    		left: 35%;">
        <center>''' + msg +'''</center>
        </h1>
    </div>
    '''

            return response
            response = "<div><center>{}</center></dev>".format(msg)
            return response, 200
            #response.headers.add('Access-Control-Allow-Origin', '*')
            #return response

        except:

            return jsonify({'trace': traceback.format_exc()})
    else:
        print ('Train the model first')
        return ('No model here to use')

if __name__ == '__main__':
    try:
        port = int(sys.argv[1]) # This is for a command-line input
    except:
        port = 2345 # If you don't provide any port the port will be set to 12345

    rfc_b = joblib.load("model.pkl") # Load "model.pkl"
    print ('Model loaded')
    model_columns = joblib.load("model_columns.pkl") # Load "model_columns.pkl"
    print ('Model columns loaded')

    app.run(debug=True, port=port, host="0.0.0.0")
