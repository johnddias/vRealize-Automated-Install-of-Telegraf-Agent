import requests
import json

def installAgent(context, inputs):
    vropsHost = "www.mgmt.cloud.vmware.com/vrops-cloud"
    token = inputs["token"]
    if not inputs["cloud"]:
        vropsHost = inputs["vropsHost"]
        token = "vRealizeOpsToken " + inputs["token"]
    if "verify" not in inputs.keys():
        inputs["verify"] = True
    print(inputs["verify"])
    headers = {'Content-type':'application/json','Accept':'application/json','Authorization':token}
    payload = {
        "resourceCredentials" : [ {
            "resourceId" : inputs["resourceId"],
            "username" : inputs["user"],
            "password" : inputs["passwd"],
            "addRuntimeUser" : True
            } ]
        }
    r = requests.request('POST','https://'+vropsHost+'/suite-api/api/applications/agents', data=json.dumps(payload), headers=headers, verify=inputs["verify"])
    res = {'code':r.status_code, 'text':json.loads(r.text)}
    return(res)
