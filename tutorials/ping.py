import subprocess

def ping_server(myhost,mycount):
	try:
		
		response = subprocess.run(
			["ping","-c",str(mycount),myhost],
			stdout=subprocess.PIPE,
			stderr=subprocess.PIPE,
			text=True
			)
		if response.returncode==0:
			return f"Successful: \n{response.stdout}"

		else:
			return f"Unsuccessful: \n{response.stderr}"	

	except Exception as e:
		return f"Excecption {str(e)}"
	finally:
		pass


myhost	=	"www.google.com"
mycount =	4

print(ping_server(myhost,mycount))