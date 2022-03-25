import requests
import json
import urllib3

def getDiscoveredApps(context, inputs):
    vropsHost = "www.mgmt.cloud.vmware.com/vrops-cloud"
    token = inputs["token"]
    if not inputs["cloud"]:
        vropsHost = inputs["vropsHost"]
        token = "vRealizeOpsToken " + inputs["token"]
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    if "verify" not in inputs.keys():
        inputs["verify"] = True
    print(inputs["verify"])
    headers = {'Content-type':'application/json','Accept':'application/json','Authorization':token}
    r = requests.request('GET','https://'+vropsHost+'/suite-api/api/applications/agents/'+inputs["resId"]+'/services', headers=headers, verify=inputs["verify"])
    print(r.status_code)
    print(r.url)
    res = {'code':r.status_code, 'text':json.loads(r.text)}
    return(res)
