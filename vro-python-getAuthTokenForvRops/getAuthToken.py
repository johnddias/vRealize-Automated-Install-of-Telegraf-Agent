import requests
import json

def getAuthToken(context, inputs):
    if inputs["cloud"]:
        headers = {'Content-type':'application/x-www-form-urlencoded','Accept':'application/json'}
        payload = {
        'refresh_token':inputs["refToken"]
        }
        r = requests.request('POST',"https://console.cloud.vmware.com/csp/gateway/am/api/auth/api-tokens/authorize", data=payload, headers=headers)
        token = json.loads(r.text)
        print(r.text)
        return("CSPToken " + token["access_token"])
    else:
        if "verify" not in inputs.keys():
            inputs["verify"] = True
        headers = {'Content-type':'application/json','Accept':'application/json'}
        payload = {
        'username':inputs["username"],
        'authSource':inputs["authSource"],
        'password':inputs["password"]
        }
        r = requests.request('POST','https://'+inputs["vropsHost"]+'/suite-api/api/auth/token/acquire', data=json.dumps(payload), headers=headers, verify=inputs["verify"])
        print (r.status_code)
        print (r.text)
        token = json.loads(r.text)
        return(token["token"])
