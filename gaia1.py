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
    debug = 0

    payload = {"user" : user, "password" : password}
    response = api_call(gateway, "login", payload, "")

    if(debug == 1):
        print("---------------------------------------")
        print(json.dumps(response))
        print("---------------------------------------")
    return response["sid"]

def main():
    gw       = "146.18.33.55"
    user     = "admin"
    password = "1qazxsw2"

    sid = login(user, password, gw)

    print(sid)

    logout = api_call(gw, "logout", {}, sid)

    print(json.dumps(logout))
    

if __name__ == "__main__":
    main()
#end of program