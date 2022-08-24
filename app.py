from flask import Flask,jsonify,request

app = Flask(__name__)

List = [
    {
        'id':"1",
        'name':"mom",
        'number':"9967013736"
    },
    {
        'id':"2",
        'name':"dad",
        'number':"9967013734"
    }
]

@app.route('/contacts')
def getdata():
    return jsonify({
        'data':List
    })
    
@app.route('/add_contact',methods = ['POST'])
def adddata():
    if not request.json:
        return jsonify({
            "status":"error",
            "message":"Please provide the contact"
        },400)
        
    contact = {
        "id":List[-1]['id']+1,
        "name":request.json('name'),
        "number":request.json.get("number","")
    }
    List.append(contact)
    return jsonify({
        "status":"succes",
        "message":"contact has been added succesfully"
    })
    
if (__name__ == '__main__'):
    app.run(debug = True)
    
    
