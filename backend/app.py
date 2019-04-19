from flask import Flask,redirect,jsonify,json,render_template,Response
app=Flask(__name__)

@app.errorhandler(404)
def error(e):
    return render_template('404.html'),404

@app.route('/api/pokemon/<int:id>')
def id(id):
    if(id>0 and id<152):
        json_data=open('pokemon_data.json')
        data=json.load(json_data)
        pokemon=data[id-1]
        return jsonify(pokemon)
    else:
        return('<h1>404 Page Not Found</h1>')
if __name__ == '__main__':
    app.run(host='localhost',port=8006,debug=True)
