from flask import Flask,jsonify,render_template,Response
import json,requests

app=Flask(__name__)                                                 # Initializing Flask

@app.route('/api/pokemon/<int:id>')                                 
def id(id):
    if(id>0 and id<152):
        json_data=open('pokemon_data.json')                        # Opening Pokemon Data JSON File
        data=json.load(json_data)                                  # Loading Pokemon Data
        pokemon=data[id-1]                                         # Stroing required details into a variable
        return jsonify(pokemon)                                    # Displaying required JSON data
    else:
        return('<h1>404 Page Not Found</h1>')
@app.errorhandler(404)                                              # Handling 404 Error
def page_not_found(e):
    return render_template('404.html'),404

if __name__ == '__main__':
    app.run(host='localhost',port=8006,debug=True)
