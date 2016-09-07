from cli import *

vlan_names = ['web','db','web2','db2','voice','video','srvs','test','prod','qa']
for vlan in range(10,20):
    cli('config t ; ' + 'vlan ' + str(vlan) + ' ; ' + 'name ' + vlan_names[vlan - 10] + ' ; ')

