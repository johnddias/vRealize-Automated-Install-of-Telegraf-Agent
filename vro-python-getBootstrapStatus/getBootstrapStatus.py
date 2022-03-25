import requests
import json
import logging

def getBootstrapStatus(context, inputs):
    vropsHost = inputs["vropsHost"]
    token = "vRealizeOpsToken " + inputs["token"]
    if inputs["cloud"]:
        vropsHost = "www.mgmt.cloud.vmware.com/vrops-cloud"
        token = inputs["token"]
    if "verify" not in inputs.keys():
        inputs["verify"] = True
    headers = {'Content-type':'application/json','Accept':'application/json','Authorization': token}
    r = requests.request('GET','https://'+vropsHost+'/suite-api/api/applications/agents/'+inputs["taskId"]+'/status', headers=headers, verify=inputs["verify"])
    print(r.status_code)
    if (r.status_code == 200):
        taskStatus = json.loads(r.text)
        return(taskStatus["bootstrapObjectStatuses"][0]["stage"])
    return("Error retrieving bootstap status: " + str(r.status_code))
