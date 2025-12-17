##put and  delete - http verbs
### working with APIs -- json

from flask import Flask, jsonify,request

app = Flask(__name__)

#initial data in my list
items = [
    {"id":1, "name":"Item 1","description":"THis is item 1"}
    {"id":2, "name":"Item 2","description":"THis is item 2"}
]

@app.route('/')
def home():
    return "welcome to the sample to do list app"

##Get : Retrieve all the items
@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items)

##get : retrieve a specific item by id
@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item=next((for item in items if item["id"]==item_id),None)
    if item is None:
        return jsonify({"error":"item not found"})
    return jsonify(item)

##post : create a new task
@app.route('/items'.methods['POST'])
def create_item():
    if not request.json or not 'name' in request.json:





if __name__ == '__main__':
    app.run(debug=True)