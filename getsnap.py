from errbot import BotPlugin, botcmd
import subprocess
import sys

class GetSnap(BotPlugin):
	"""Errbot plugin to fetch current sprint details"""
	@botcmd
	def getsnap(self, msg, args):
		get_snap_cmd = 'imagesnap ~/snap$(date +%y%m%d%H%M%S).png'
		get_snap, err = subprocess.Popen(get_snap_cmd, shell=True, stdout=subprocess.PIPE).communicate()
		file_line = get_snap.splitlines()[-1]
		filename = file_line.split('/')[-1]
		get_key_name = 'ls ~/.ssh/ | grep -i digital | grep -vi pub'
		key_name, err = subprocess.Popen(get_key_name, shell=True, stdout=subprocess.PIPE).communicate()

		clean_key_name = key_name.replace('\n', '')

		up_snap_cmd = 'scp -i ~/.ssh/'+clean_key_name +' ~/' + filename + ' reverse@'+args[0]':./'
		up_snap = subprocess.Popen(up_snap_cmd, shell=True, stdout=subprocess.PIPE).communicate()

		return("File uploaded.")
		# return(user_dir)
