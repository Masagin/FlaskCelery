from os import path, environ
import json
from flask import Flask, Blueprint, abort, jsonify, request, session
from twisted.python.runtime import seconds
from tasks import add
import tasks

app = Flask(__name__)

@app.route("/test")
def hello_world(x=16, y=16):
    x = int(request.args.get("x", x))
    y = int(request.args.get("y", y))
    res = add.apply_async((x, y))
    context = {"id": res.task_id, "x": x, "y": y}
    result = "add((x){}, (y){})".format(context['x'], context['y'])
    goto = "{}".format(context['id'])
    return jsonify(result= result, goto=goto)

@app.route("/test/result/<task_id>")
def show_result(task_id):
    retval = add.AsyncResult(task_id).get(timeout=1.0)
    return repr(retval)

print app.url_map

if __name__ == "__main__":
    port = int(environ.get("PORT", 5000))
    app.run(host='127.0.0.1', port=port, debug=True)