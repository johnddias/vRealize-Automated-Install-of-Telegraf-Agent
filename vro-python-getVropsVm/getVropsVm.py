import requests
import json

def getVropsVm(context, inputs):
    if "verify" not in inputs.keys():
        inputs["verify"] = True
    print(inputs["verify"])
    headers = {'Content-type':'application/json','Accept':'application/json','Authorization':'vRealizeOpsToken '+ inputs["token"]}
    r = requests.request('POST','https://'+inputs["vropsHost"]+'/suite-api/api/resources/'+inputs[resId], headers=headers, verify=inputs["verify"])
    res = {'code':r.status_code, 'text':json.loads(r.text)}
    return(res)
