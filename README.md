- š Hi, Iām @d061987
- š Iām interested in Data Analyst, Python Developing and AWS.
- š± Iām currently learning Python Developing and AWS
- šļø Iām looking to collaborate on ...
- š« How to reach me ...

<!---
d061987/d061987 is a āØ special āØ repository because its `README.md` (this file) appears on your GitHub profile.
You can click the Preview link to take a look at your changes.
--->
import socket
udp_ip = "127.0.0.1"
udp_port = 21000
udp_buffer_size = 1024
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((udp_ip, udp_port))

while True:
    data = sock.recv(udp_buffer_size)
    if not data:
        break
    print(data)
    
    
