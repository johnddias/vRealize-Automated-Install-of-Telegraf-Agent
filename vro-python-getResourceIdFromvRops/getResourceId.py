import requests
import json

def getResourceId(context, inputs):
    if "verify" not in inputs.keys():
        inputs["verify"] = True
    headers = {'Content-type':'application/json','Accept':'application/json','Authorization':'vRealizeOpsToken '+ inputs["token"]}
    payload = {
        'propertyName':'summary|UUID',
        'propertyValue':inputs["vmUUID"]
    }
    r = requests.request('GET','https://'+inputs["vropsHost"]+'/suite-api/api/resources',params=payload, headers=headers, verify=inputs["verify"])
    print (r.text)
    resource = json.loads(r.text)
    if not resource["resourceList"]:
        return()
    else:
        return(resource["resourceList"][0]["identifier"])
