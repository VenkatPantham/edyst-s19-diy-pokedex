from flask import Flask,redirect,jsonify,json
import requests
app=Flask(__name__)

@app.route('/api/pokemon/<id>')
def id(id):
    if int(id) < 808:
        data=requests.get('https://pokeapi.co/api/v2/pokemon-form/'+id).json()
        num=data['id']
        name=data['name']
        sprite=data['sprites']
        return jsonify({'id':num,'name':name,'sprite':sprite})
    else:
        return ('Pokemon not found,Sorry We have only 807 types of Pokemons!')

if __name__ == '__main__':
    app.run(host='localhost',port=8006,debug=True)
