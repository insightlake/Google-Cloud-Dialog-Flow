try:
    import urllib
    import json
    import os
    from flask import (Flask,request, make_response)

except Exception as e:

    print("Some modules are missing {}".format(e))


# Flask app should start in global layout
app = Flask(__name__)


# whenever you make request /webhook
# Following calls are made
# webhook ->
# -----------> Process requests
# ---------------------------->get_data()

@app.route('/webhook', methods=['POST'])
def webhook():

    if request.method == "POST":
        req = request.get_json(silent=True, force=True)
        res = processRequest(req)

        res = json.dumps(res, indent=4)
        r = make_response(res)
        r.headers['Content-Type'] = 'application/json'
        return r


def processRequest(req):

    # Get all the Query Parameter
    query_response = req["queryResult"]
    global city
    # print(query_response)
    city=query_response['outputContexts'][0]['parameters']['geo-city.original']
    # geo_city=query_response['parameters']['geo-city']
    text = query_response.get('queryText', None)
    parameters = query_response.get('parameters', None)
    res = get_data()

    return res


def get_data():
    sample_data={'la':'sunny','moscow':'rainy','california':'windy','neveda':'cold','new-york':'mild'}
    speech = "Weather in {} is {}".format(city,sample_data[city])
    # speech="getting data"
    return {
        "fulfillmentText": speech,
    }


port = int(os.getenv('PORT', 5000))
print ("Starting app on port %d" %(port))
app.run(debug=True, port=port, host='0.0.0.0')


