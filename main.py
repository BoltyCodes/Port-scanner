import socket
import subprocess
import sys
from datetime import datetime

# Clear the screen
subprocess.call('clear', shell=True)

# Ask for input
host_toscan = raw_input("Enter a remote host to scan: ")
serverIP  = socket.gethostbyname(host_toscan)

# Print a nice banner with information on which host we are about to scan
print "-" * 60
print "Please wait, scanning remote host", remoteServerIP
print "-" * 60

# Check what time the scan started
t1 = datetime.now()



try:
    for port in range(2,1025):  
        sockets = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        hostfound = sockets.connect_ex((remoteServerIP, port))
        if hostfound == 0:
            print "Port {}: 	 Open".format(port)
        sock.close()

except KeyboardInterrupt:
    print "You exited this code"
    sys.exit()

except socket.gaierror:
    print 'Hostname could not be resolved. Exiting now.'
    sys.exit()

except socket.error:
    print "Couldn't connect to server"
    sys.exit()


# How long it took to find a port
total =  t2 - t1

# Printing the information to screen
print 'Scanning Completed in: ', total
