import json
from flask import Flask, jsonify, request

app=Flask(__name__)


@app.route('/', methods=['GET'])
def query_records():
   name = request.args.get('name')
   print(name)
   with open('files/data.txt', 'r') as f:
      data = f.read()
      records = json.loads(data)
      for record in records:
         if record['name'] == name:
            return jsonify(record)
      return jsonify({'error': 'data not found'})

@app.route('/', methods=['PUT'])
def create_record():
   record = json.loads(request.data)
   with open('files/data.txt', 'r') as f:
      data = f.read()
   if not data:
      records = [record]
   else:
      records = json.loads(data)
      records.append(record)
   with open('files/data.txt', 'w') as f:
      f.write(json.dumps(records, indent=2))
   return jsonify(record)

@app.route('/', methods=['POST'])
def update_record():
   record = json.loads(request.data)
   new_records = []
   with open('files/data.txt', 'r') as f:
      data = f.read()
      records = json.loads(data)
   for r in records:
      if r['name'] == record['name']:
         r['email'] = record['email']
      new_records.append(r)
   with open('files/data.txt', 'w') as f:
      f.write(json.dumps(new_records, indent=2))
   return jsonify(record)

@app.route('/', methods=['DELETE'])
def delete_record():
   record = json.loads(request.data)
   new_records = []
   with open('files/data.txt', 'r') as f:
      data = f.read()
      records = json.loads(data)
      for r in records:
         if r['name'] == record['name']:
            continue
         new_records.append(r)
   with open('files/data.txt', 'w') as f:
      f.write(json.dumps(new_records, indent=2))
   return jsonify(record)

app.run(debug=True)