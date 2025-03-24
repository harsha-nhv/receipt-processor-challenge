from flask import Flask, request, jsonify
from models.ReceiptModel import ReceiptModel
from receipt import Receipt
from pydantic import ValidationError


app = Flask(__name__)
idToReceiptMap = dict()
counter = 0

@app.route("/")
def main():
    return "<p>Hello, Welcome to Receipt Processor Challenge!</p>"

@app.route("/receipts/<id>/points", methods = ['GET'])
def getPoints(id):
    if id in idToReceiptMap:
        return {"points": idToReceiptMap[id].getPoints()}
    
    return jsonify({"message": "No receipt found for that ID."}), 400


@app.route("/receipts/process", methods = ['POST'])
def processReceipts():
    global counter
    try : 
        receiptObject = ReceiptModel.parse_raw(request.data)

        receipt = Receipt(receiptObject)
        id = 'receipt-' + str(counter)
        counter += 1
        idToReceiptMap[id] = receipt

        return {"id" : id}, 200
    except ValidationError as e:
        return jsonify({"message": "The receipt is invalid."}), 400
    
    except Exception as e:
        return jsonify({"message": "Internal processing error"}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)