import requests
import json
import logging

def getBootstrapStatus(context, inputs):
    if "verify" not in inputs.keys():
        inputs["verify"] = True
    headers = {'Content-type':'application/json','Accept':'application/json','Authorization':'vRealizeOpsToken '+ inputs["token"]}
    r = requests.request('GET','https://'+inputs["vropsHost"]+'/suite-api/api/applications/agents/'+inputs["taskId"]+'/status', headers=headers, verify=inputs["verify"])
    if (r.status_code == 200):
        taskStatus = json.loads(r.text)
        return(taskStatus["bootstrapObjectStatuses"][0]["stage"])
    return("Error retrieving bootstap status: " + str(r.status_code))
