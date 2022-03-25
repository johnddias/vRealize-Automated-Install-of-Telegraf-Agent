import requests
import json

def getVropsVmPowerState(context, inputs):
    vropsHost = "www.mgmt.cloud.vmware.com/vrops-cloud"
    token = inputs["token"]
    if not inputs["cloud"]:
        vropsHost = inputs["vropsHost"]
        token = "vRealizeOpsToken " + inputs["token"]
    if "verify" not in inputs.keys():
        inputs["verify"] = True
    headers = {'Content-type':'application/json','Accept':'application/json','Authorization':token}
    r = requests.request('GET','https://'+vropsHost+'/suite-api/api/resources/'+inputs["resId"]+'/stats/latest?statKey=sys|poweredOn', headers=headers, verify=inputs["verify"])
    resObj = json.loads(r.text)
    resObj["code"] = r.status_code
    res = json.dumps(resObj)
    print(res)
    return(res)
