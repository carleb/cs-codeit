# import logging
# import json

# from flask import request, jsonify

# from codeitsuisse import app

# logger = logging.getLogger(__name__)


# def stonks1(input):
#     return str(input)


# @app.route('/stonks ', methods=['POST'])
# def stonks():
#     data = request.get_json()
#     logging.info("data sent for evaluation {}".format(data))
#     # inputValue = data.get("input")
#     result = stonks1(data)
#     logging.info("My result :{}".format(result))
#     return json.dumps(result)
