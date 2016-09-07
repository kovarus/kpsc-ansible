#!/usr/bin/env python

from onep.element.NetworkElement import NetworkApplication, NetworkElement
from onep.element.SessionConfig import SessionConfig
from onep.routing.AppRouteTable import AppRouteTable
from onep.routing.L3UnicastRouteOperation import L3UnicastRouteOperation
from onep.routing.RouteOperation import RouteOperation
from onep.routing.L3UnicastRIBFilter import L3UnicastRIBFilter
from onep.routing.L3UnicastScope import L3UnicastScope
from onep.routing.L3UnicastRouteRange import L3UnicastRouteRange
from onep.interfaces.NetworkPrefix import NetworkPrefix
from onep.routing.L3UnicastRoute import L3UnicastRoute
from onep.routing.RouteRange import *
from onep.routing.RoutingClass import *
from onep.routing.L3UnicastNextHop import L3UnicastNextHop


from onepk import Device
import time
import sys

def addRoute(device,route):
	
	next_hop = route['next_hop']
	out_intf = route['out_intf']
	dest_prefix = route['dest_prefix']
	dest_prefix_mask = route['dest_prefix_mask']
	admin_distance = route['admin_distance']

	try:
		routing = Routing.get_instance(device)
		approutetable = routing.app_route_table
		aL3UnicastScope = L3UnicastScope("",L3UnicastScope.AFIType.IPV4 ,L3UnicastScope.SAFIType.UNICAST, "")
		destNetwork = NetworkPrefix(dest_prefix, dest_prefix_mask)
		eth_interface = device.get_interface_by_name(out_intf)

		route_scope = L3UnicastScope("", L3UnicastScope.AFIType.IPV4 , L3UnicastScope.SAFIType.UNICAST, "")

		aL3UnicastNextHop = L3UnicastNextHop(eth_interface,next_hop,route_scope)
		aL3UnicastNextHopList = list()  
		aL3UnicastNextHopList.append(aL3UnicastNextHop)

		aRoute = L3UnicastRoute(destNetwork, aL3UnicastNextHopList)
		aRoute.admin_distance = admin_distance

		routeOperation = L3UnicastRouteOperation(RouteOperation.RouteOperationType.ADD, aRoute)    
		routeOperationList = list()
		routeOperationList.append(routeOperation)
		approutetable.update_routes(aL3UnicastScope, routeOperationList)

		return 'Route Installed'
	
	except:
		print 'Error'
		return 'Error: Route Not Installed'

def main():
	

	dev = Device(ip='10.1.1.110')

	args = sys.argv
	
	route = {}

	route['dest_prefix'] = args[1]
	route['dest_prefix_mask'] = int(args[2])
	route['next_hop'] = args[3]
	route['out_intf'] = args[4]
	route['admin_distance'] = int(args[5])

	status = addRoute(dev,route)

	if status == 'Route Installed':
		print status
		print "Check the routing table if you want to see it: 'show ip route " + route['dest_prefix'] + "'"
		time.sleep(10)
		dev.disconnect()
		print 'Route Removed'
	else:
		print status	


if __name__ == "__main__":

	main()