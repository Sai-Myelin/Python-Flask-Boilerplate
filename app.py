from pytube import YouTube
from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

@app.route('/stock_search')
def load_stock_data():
    name = request.args.get('ticker', type=str)
    url = (str(name))
    output_string = str(YouTube("https://www.youtube.com/watch?v=ornZr5VB4U0&feature=youtu.be&list=PLZvMd5DC4ZW4g1nHZVi9g7PzMxacSqAvm").streams[0].url)
    output_string = "<iframe width = '512px' height = '301px' src = '" + output_string + "'></iframe>"
    return jsonify(ticker = str(output_string))

@app.route('/home')
def edit():
    data = [1,1,1,
            0,0,0,
            -1,-1,-1]
    return render_template('index.html', boardData = data)

if __name__ == '__main__':
    app.run(port=5555)
