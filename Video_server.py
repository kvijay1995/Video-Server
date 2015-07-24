import netifaces as ni
import time
import socket
import cv2

# Create a socket connection and listen
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST = ni.ifaddresses('wlp3s0')[2][0]['addr']
PORT = 3333
s.bind((HOST, PORT))
s.listen(1)

camera = cv2.VideoCapture(0)

# Listen for connection and send image size
client, address = s.accept()
print "A client has connected from {}".format(address)

try:
    # start loop here
    while True:
        f, img = camera.read()
        f, jpeg = cv2.imencode('.jpg',  img)

        # send image size in bytes to client
        client.sendall(str(jpeg.nbytes) + "\n")

        # send image in byte packets to client
        client.sendall(jpeg.tostring())

except KeyboardInterrupt:
    s.close()
    client.close()
    camera.release()
    print "\nServer requested to die"
