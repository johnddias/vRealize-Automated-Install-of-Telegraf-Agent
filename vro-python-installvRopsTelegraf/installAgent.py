import requests
import json

def installAgent(context, inputs):
    if "verify" not in inputs.keys():
        inputs["verify"] = True
    print(inputs["verify"])
    headers = {'Content-type':'application/json','Accept':'application/json','Authorization':'vRealizeOpsToken '+ inputs["token"]}
    payload = {
        "resourceCredentials" : [ {
            "resourceId" : inputs["resourceId"],
            "username" : inputs["user"],
            "password" : inputs["passwd"],
            "addRuntimeUser" : True
            } ]
        }
    r = requests.request('POST','https://'+inputs["vropsHost"]+'/suite-api/api/applications/agents', data=json.dumps(payload), headers=headers, verify=inputs["verify"])
    res = {'code':r.status_code, 'text':json.loads(r.text)}
    return(res)
