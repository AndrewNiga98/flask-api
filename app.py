from flask import Flask, jsonify

app = Flask(__name__)

person1 = [
    {
        'id' : 0,
        'name' : u'Andrew',
        'surname' : u'Nigaychuk'
        
    },
    {
        'id' : 1,
        'name' : u'Bogdan',
        'surname' : u'Gavrilyuk'
    }
]

@app.route('/api/person', methods=['GET'])

def get_tasks():
    return jsonify({'person': person1})
    
if __name__ == '__main__':
    app.run(debug=True)