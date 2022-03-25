import requests
import json

def getResourceId(context, inputs):
    vropsHost = "www.mgmt.cloud.vmware.com/vrops-cloud"
    token = inputs["token"]
    if not inputs["cloud"]:
        vropsHost = inputs["vropsHost"]
        token = "vRealizeOpsToken " + inputs["token"]
    if "verify" not in inputs.keys():
        inputs["verify"] = True
    headers = {'Content-type':'application/json','Accept':'application/json','Authorization':token}
    payload = {
        'propertyName':'summary|UUID',
        'propertyValue':inputs["vmUUID"]
    }
    r = requests.request('GET','https://'+vropsHost+'/suite-api/api/resources',params=payload, headers=headers, verify=inputs["verify"])
    print (r.text)
    print (r.url)
    resource = json.loads(r.text)
    if not resource["resourceList"]:
        return()
    else:
        return(resource["resourceList"][0]["identifier"])
