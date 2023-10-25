# Security-Tools-in-Python
Several simple projects done in Python for network monitoring for Cybersecurity and high availability. All the modules needed are in their folder with the script.

<em>UPDATED, ADDED PASSWORD GENERATOR</em>

𝗕𝗔𝗡𝗗𝗪𝗜𝗗𝗧𝗛
<br>This script, made with the psutil library, obtains your bandwidth on the network interface you specify.

<u>References</u>
<br>https://pypi.org/project/psutil/

𝗖𝗥𝗬𝗣𝗧𝗢𝗚𝗥𝗔𝗣𝗛𝗬
<br>This script generates a private key with the RSA encryption algorithm of 2048, then what it does is to convert the private key to a PEM format file, we write the key to the generated file. Then we generate the public key from the private key. 
Finally we pass the public key to an SSH file and write it to a file.

<u>References</u>
<br>https://pypi.org/project/cryptography/

𝗙𝗜𝗥𝗘𝗪𝗔𝗟𝗟 𝗥𝗨𝗟𝗘
<br>This script is very customizable, as we can adjust it for our own needs, in this case I have made a rule to block ping, another rule to block RDP protocol, and the last rule allows TCP traffic from one subnet to another over port 80, in this case, the good thing about this is that you can change it to suit your needs.

<u>References</u>
<br>https://pypi.org/project/python-iptables/

𝗛𝗔𝗦𝗛 𝗖𝗔𝗟𝗖𝗨𝗟𝗔𝗧𝗢𝗥
<br>

<u>References</u>
<br>https://pypi.org/project/hashlib/

𝗣𝗔𝗦𝗦𝗪𝗢𝗥𝗗 𝗚𝗘𝗡𝗘𝗥𝗔𝗧𝗢𝗥
<br>This password generation script, the first thing I have done is to create a function that creates the password with all the ASCII characters and digits with the string library, then create a JSON file, add an exception, and then call the function created and pass it as parameter 12 to make it as secure as possible, and finally the generated passwords will be dumped to the JSON file previously created.

References</u>
<br>https://pypi.org/project/python-secrets/
<br>https://docs.python.org/3/library/json.html
<br>https://docs.python.org/es/3/library/string.html

𝗣𝗢𝗥𝗧 𝗦𝗖𝗔𝗡𝗡𝗘𝗥
<br>The port scanner, I have created a function to scan all ports from 1 to 65535 and check if it is open and then close the connection. Out of the function we indicate the IP to which we want to scan and the ports. Finally we call the function, with the three parameters. 

<u>References</u>
<br>https://docs.python.org/es/3/library/socket.html

𝗧𝗥𝗔𝗙𝗙𝗜𝗖 𝗔𝗡𝗔𝗟𝗬𝗭𝗘𝗥
<br>This script is very short but powerful because it uses one of the best cybersecurity libraries such as scapy. I define a function, in this function it will verify if the packets are TCP and we indicate the TCP traffic and it indicates the size in bytes. With sniff we start capturing packets through the interface that we indicate, in this case eth0.

<u>References</u>
<br>https://scapy.net/

𝗪𝗘𝗕 𝗔𝗣𝗣 𝗦𝗖𝗔𝗡𝗡𝗘𝗥
<br>This script to scan and analyze a web page we need the famous BeautifulSoup library. We indicate the URL that we want to scan, we collect the GET that we have answered the web that we indicate and we get the HTML and parse it using the library, and in this case, we get all the links on the page and finally iterate it with a for loop to show us all. 

<u>References</u>
<br>https://pypi.org/project/requests/
<br>https://pypi.org/project/beautifulsoup4/


