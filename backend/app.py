from flask import Flask,jsonify,render_template,json
app=Flask(__name__)                                                 # Initializing Flask

@app.errorhandler(404)                                              # Handling 404 Error
def page_not_found(e):
    return render_template('404.html'),404

@app.route('/api/pokemon/<int:id>')                                 
def id(id):
    if(id>0 and id<152):
        poke={}
        data=json.load(open('pokemon_data.json'))                   # Opening and Loading Pokemon Data JSON File
        poke['pokemon']=data[id-1]                                  # Storing all the data in a variable
        return json.dumps(poke)                                     # Displaying required JSON data
    else:
        return render_template('404.html'),404

if __name__ == '__main__':
    app.run(host='localhost',port=8006)
