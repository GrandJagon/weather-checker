#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 14:17:00 2020

@author: lucas
"""

import requests as rq 


def extract_info(json):
    info = {'ip' : 0, 'city' : 0, 'region' : 0, 'country' : 0, 'loc' :0}
    for jkey in json:
        for ikey in info:
            if jkey == ikey:
                info[ikey] = json[jkey]
                
    return info
    

def get_local_info():
    url = "https://ipinfo.io/json"
    json = rq.get(url).json()
    
    info = extract_info(json)
    
    return info
    
    


def get_external_info(ip):
    url = "https://ipinfo.io/" + str(ip) + "/json"
    
    json = rq.get(url).json()
    
    if 'error' in json:
        print("Invalid IP, the local one will be used")
        
        return get_local_info()
    
    info = extract_info(json)
    
    return info


    
    


                





    
    
    
    
    
    
    
    
        
    
