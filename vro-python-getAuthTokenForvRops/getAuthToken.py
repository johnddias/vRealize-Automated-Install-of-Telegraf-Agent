import requests
import json

def getAuthToken(context, inputs):
    if "verify" not in inputs.keys():
        inputs["verify"] = True
    headers = {'Content-type':'application/json','Accept':'application/json'}
    payload = {
    'username':inputs["username"],
    'authSource':inputs["authSource"],
    'password':inputs["password"]
    }
    r = requests.request('POST','https://'+inputs["vropsHost"]+'/suite-api/api/auth/token/acquire', data=json.dumps(payload), headers=headers, verify=inputs["verify"])
    token = json.loads(r.text)
    return(token["token"])
