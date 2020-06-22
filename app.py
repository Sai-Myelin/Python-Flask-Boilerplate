#Only required library is Flask
#Python 3+
from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

#This route is called from JS inside of Index.html on line 30
@app.route('/example_route')
def function1():
    #Get the data from the request
    #The parameter we want is called parameter1
    #See lines 23-38 for more details!
    name = request.args.get('parameter1', type=str)
    url = (str(name))
    return jsonify(parameter1 = str(url))

#This means when you type localhost:5555/home it will hit this route
#5555 is just the port defined at the bottom of the file!
@app.route('/home')
def edit():
    #Data to pass to our templates/index.html file
    data = 6

    #This line means render index.html with params data as name game_data
    #A great behavior that can be very useful.
    return render_template('index.html', game_data = data)

if __name__ == '__main__':
    #The port our Flask app will run on
    app.run(port=5555)
