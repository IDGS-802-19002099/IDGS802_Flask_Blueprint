
from flask import Blueprint

dir=Blueprint('dir',__name__)

@dir.route("/getDir",methods=["GET"])
def getdir():
    return {'key':'Directivos'}
