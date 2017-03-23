from errbot import BotPlugin, botcmd
import subprocess
import sys

class GetSnap(BotPlugin):
	"""Errbot plugin to fetch current sprint details"""
	@botcmd
	def getsnap(self, msg, args):
		get_snap_cmd = 'imagesnap ~/$(date +%y%m%d%H%M%S).png'
		get_snap, err = subprocess.Popen(get_snap_cmd, shell=True, stdout=subprocess.PIPE).communicate()
		file_line = get_snap.splitlines()[-1]

		return(file_line)
