import socket
host = "Thinky.local"
port = 4444

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))


try:
	s.send("hellochat")
except:
	print("Server Down!")
	raise SystemExit
	

sendloop = True
while sendloop:
	message = raw_input("What you want? ")
	if message == "history":
		print("This is the History")
		s.send(message)

		ouputa = s.recv(10000)
		print ouputa

	if message == "exit":
		print("Bye!")
		s.close
		raise SystemExit

	else:
		# add newline
		message = message + "\n"
		s.send(message)
			