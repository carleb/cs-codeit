import logging
import json

from flask import request, jsonify

from codeitsuisse import app

logger = logging.getLogger(__name__)

def optopt1(input):

    count = len(input['options'])

    assign = 100/count

    res = []
    for i in range(count):
        res.append(assign)
        
    return res


@app.route('/optopt', methods=['POST'])
def optopt():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    # inputValue = data.get("input")
    result = optopt1(data)
    logging.info("My result :{}".format(result))
    return json.dumps(result)
