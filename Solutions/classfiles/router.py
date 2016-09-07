#!/usr/bin/env python

import sys

def getRouter(rtr):
   router1 = {'os_version':'3.1.1','hostname':'nyc_router1','model':'nexus 9396', \
   'domain':'cisco.com','mgmt_ip':'10.1.50.11'}
   router2 = dict( os_version='3.2.1', hostname='rtp_router2',model='nexus 9396', \
   	domain='cisco.com', mgmt_ip='10.1.50.12')
   router3 = dict( os_version='3.1.1', hostname='ROUTER3',model='nexus 9504', \
   	domain='lab.cisco.com', mgmt_ip='10.1.50.13')
   
   router_list = [router1,router2,router3]
   for router in router_list:
       if rtr == router['hostname']:
           return router
   return 'No router found.'

if __name__ == "__main__":

    args = sys.argv

    #print args

    result1 = getRouter(args[1])
    
    print 'HOSTNAME:', result1['hostname']

    value = args[2]

    print value.upper() + ': ' + result1[value]
    

