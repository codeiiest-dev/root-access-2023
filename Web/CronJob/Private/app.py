from flask import Flask,request,jsonify

app = Flask(__name__)

@app.route('/', methods = ['POST'])
def getData():
    print(request.form.get("flag"))
    data = {"message" : "Message recieved",}
    return jsonify(data)

if __name__ == '__main__':
    app.run(host="localhost", port=8000,debug="True")