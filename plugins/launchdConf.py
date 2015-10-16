__author__ = 'patrick w'

'''
launchd.conf

    the /etc/launchd.conf file contains commands that are that are executed at boot by launchctl

    this plugin (very basically) parses this file, extacting all such commands
'''

import os

#project imports
import utils
import command

#plugin framework import
from yapsy.IPlugin import IPlugin

#path to launchd.conf
LAUNCHD_CONF_FILE = '/etc/launchd.conf'

#for output, item name
LAUNCHD_CONF_NAME = 'Launchd Configuration File'

#for output, description of items
LAUNCHD_CONF_DESCRIPTION = 'Commands that are executed by LaunchCtl'

#plugin class
class scan(IPlugin):

	#init results dictionary
	# ->item name, description, and items list
	def initResults(self, name, description):

		#results dictionary
		return {'name': name, 'description': description, 'items': []}

	#invoked by core
	def scan(self):

		#commands
		commands = []

		#dbg msg
		utils.logMessage(utils.MODE_INFO, 'running scan')

		#init results dictionary
		results = self.initResults(LAUNCHD_CONF_NAME, LAUNCHD_CONF_DESCRIPTION)

		#get all commands in launchd.conf
		# ->note, commands in functions will be ignored...
		commands = utils.parseBashFile(LAUNCHD_CONF_FILE)

		#iterate over all commands
		# ->instantiate command obj and save into results
		for extractedCommand in commands:

			#TODO: could prolly do some more advanced processing (e.g. look for bsexec, etc)

			#instantiate and save
			results['items'].append(command.Command(extractedCommand))

		return results






