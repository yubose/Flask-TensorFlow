from flask import Flask, request
from flask_restful import Api
import cift
import subprocess
import ciftCache

app = Flask(__name__)
api = Api(app)

@app.route('/classify-image', methods=['POST'])
def classifyImage():
    data = request.get_json()
    imgUrl = data['image_url']
    #ci = cift.Cift('MobileNet.h5', 'gum_label_1000.json', 224)
    #return ci.classify(imgUrl)
    ca = ciftCache.cache(3600)
    rtnV = ca.get(imgUrl)
    if rtnV is None:
        rtnV = subprocess.check_output(['./cift.py', imgUrl])
        ca.set(imgUrl, rtnV)
    return rtnV

@app.route('/report', methods=['GET'])
def report():
    ca = ciftCache.cache()
    return ca.report()

@app.route('/usercheck', methods=['GET'])
def usercheck():
    secret = request.args.get('secret')
    ca = ciftCache.cache()
    name = ca.authcheck(secret)
    if name is None:
        return "User Not Found", 404
    else:
        return "Hi " + name, 200

if __name__ == '__main__':
    #print ci.classify('https://s3.amazonaws.com/gumgum-interviews/ml-engineer/cat.jpg')
    app.run(host='0.0.0.0', port=8080, debug=True)
