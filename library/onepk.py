#!/usr/bin/env python

from onep.element.NetworkElement import NetworkApplication, NetworkElement
from onep.element.SessionConfig import SessionConfig
from onep.core.exception import *

class Device():

	def __init__(self,ip,username='cisco',password='cisco'):
	
		self.ip = ip
		self.username = username
		self.password = password

		self.myapp = NetworkApplication.get_instance()
		if not self.myapp.name == 'onePK-Python-Course-app':
			self.myapp.name == 'onePK-Python-Course-app'

		self.session_config = SessionConfig(SessionConfig.SessionTransportMode.TLS)
		self.session_config.ca_certs = "/home/cisco/ca.pem"
		
	def open(self):

		ne = self.myapp.get_network_element(self.ip)
		session_handle = ne.connect(self.username, self.password, self.session_config)

		return ne

