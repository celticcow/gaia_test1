#!/usr/bin/python3 -W ignore::DeprecationWarning

import requests
import json


"""
gaia api test bed

see sk143612

"""
#remove the InsecureRequestWarning messages
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


"""
api_call function 
takes IP of mds / api command name / json payload / session ID as arg
"""
def api_call(ip_addr, command, json_payload, sid):
    url = "https://" + ip_addr + ":" + "/gaia_api/" + command
    if(sid == ""):
        request_headers = {"Content-Type" : "application/json"}
    else:
        request_headers = {"Content-Type": "application/json", "X-chkp-sid" : sid}
    
    r = requests.post(url,data=json.dumps(json_payload), headers=request_headers, verify=False)
    return r.json()

"""
Login function
payload to login to CMA
returns Session ID (SID)
"""
def login(user, password, gateway):
    payload = {"user" : user, "password" : password}
    response = api_call(gateway, "login", payload, "")

    return response["sid"]

def main():
    gw       = "146.18.33.55"
    user     = "admin"
    password = "1qazxsw2"

    sid = login(user, password, gw)

    print(sid)

    show_route_response = api_call(gw, "show-routes-static", {}, sid)

    print(json.dumps(show_route_response))

    show_cluster_state_response = api_call(gw, "show-cluster-state", {}, sid)

    print(json.dumps(show_cluster_state_response))

    show_radius_response = api_call(gw, "show-radius", {}, sid)

    print(json.dumps(show_radius_response))

    show_asset_response = api_call(gw, "show-asset", {}, sid)

    print(json.dumps(show_asset_response))

    print("#############################################################")
    power_supply_len = len(show_asset_response["power-supply"])

    for i in range(power_supply_len):
        print(show_asset_response['power-supply'][i])

    disk_len = len(show_asset_response["disk"])

    for i in range(disk_len):
        print(show_asset_response['disk'][i])

    system_len = len(show_asset_response["system"])

    for i in range(disk_len):
        print(show_asset_response['system'][i])
    
    memory_len = len(show_asset_response["memory"])

    for i in range(disk_len):
        print(show_asset_response['memory'][i])

    print("#############################################################")
    show_diag_json = {"category": "os", "topic": "cpu"}
    show_diag_response = api_call(gw, "show-diagnostics", show_diag_json, sid)

    print(json.dumps(show_diag_response))

    for i in range(show_diag_response['total']):
        print("CPU " + str(i))
        print(show_diag_response['objects'][i]['idle'], end=' ')
        print("idle")
        print(show_diag_response['objects'][i]['io-wait'], end=' ')
        print("io-wait")
        print(show_diag_response['objects'][i]['system'], end=' ')
        print("system")
        print(show_diag_response['objects'][i]['user'], end=' ')
        print("user")



    print("#############################################################")
    logout = api_call(gw, "logout", {}, sid)

    print(json.dumps(logout))
    

if __name__ == "__main__":
    main()
#end of program