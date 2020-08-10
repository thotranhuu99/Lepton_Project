import socket
import cv2
import time
import subprocess
import os

Bash_script_location = os.path.join(os.getcwd(), "flirpi", "single_read.sh")
img_location = os.path.join(os.getcwd(), "flirpi", "x.png")
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
while True:
    # rc = subprocess.call("/home/tho/Lepton_Project/Test_folder/Test_bash.sh", shell=True)
    rc = subprocess.call(Bash_script_location, shell=True)
    img = cv2.imread(img_location, -1)
    b = bytearray(img)
    sock.sendto(b, ("192.168.100.6", 5002))
    print("Frame sent")
    time.sleep(0.1)

