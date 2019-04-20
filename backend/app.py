from flask import Flask,jsonify,render_template,json

app=Flask(__name__)                                                 # Initializing Flask

@app.route('/api/pokemon/<int:id>')                                 
def id(id):
    if(id>0 and id<152):
        data={}
        data['pokemon']=json.load(open('pokemon_data.json'))                        # Opening and Loading Pokemon Data JSON File
        return jsonify(data[id-1])                                       # Displaying required JSON data
    else:
        return('<h1>404 Page Not Found</h1>')
@app.errorhandler(404)                                              # Handling 404 Error
def page_not_found(e):
    return render_template('404.html'),404

if __name__ == '__main__':
    app.run(host='localhost',port=8006)
