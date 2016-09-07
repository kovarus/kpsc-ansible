#!/usr/bin/env python


from onepk import Device
from addroute import addRoute

from onep.interfaces.InterfaceStatus import InterfaceStatus
from onep.interfaces.InterfaceFilter import InterfaceFilter
from onep.interfaces.InterfaceConfig import InterfaceConfig
from onep.interfaces import NetworkInterface
import time

def getInterfaceStatus(device,interface):

	lp = device.get_interface_by_name(interface).get_status().lineproto

	if lp == 3:
		oper = 'up'
	else:
		oper = 'down'

	return oper

def main():
	
	r1_session = Device(ip='10.10.10.110')
	
	r1 = r1_session.open()

	oper = getInterfaceStatus(r1,'GigabitEthernet0/0')
	
	route = dict(dest_prefix='111.111.10.0',dest_prefix_mask=24,next_hop='10.1.1.120', \
		out_intf='GigabitEthernet0/2', admin_distance=34)

	if oper == 'down':
		status = addRoute(r1,route)
	else:
		status = 'Interface is up.  Dynamic Route not configured'


	if status == 'Route Installed':
			print '\n' + status
			print 'Check the routing table if you want to see it'
			print "Use 'show ip route " + route['dest_prefix'] + "'"
			print 'Look for the (a) route'
			time.sleep(30)
			print '\nRoute Removed'
	else:
		print status	

	r1.disconnect()

if __name__ == "__main__":
	main()




