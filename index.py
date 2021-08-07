import subprocess
import re
from pyfiglet import Figlet

f = Figlet(font='slant')
print(f.renderText('Security testing software v1.2'))

print("""##################[ MENU ]###################
[~] Change MAC address    - Enter 1
[~] Scan Network          - Enter 2
[~] Spoof ARP data        - Enter 3
[~] Sniff data flow       - Enter 4
[~] MITM Detector         - Enter 5
[~] Vul Scanner           - Enter 6
[~] To use command mode   - type "command"
[~] To close software     - type "exit"
""")


def mac():
    print("""DEMO commands:- \npython3 macchanger.py -i eth0 -m 08:00:27:5c:65:25 \npython3 macchanger.py --help
                     or    \nuse input mode given below (NOTE: Use commands only if input mode not working)
                             """)
    print("<input mode>")
    a1 = input("Enter interface       :")
    a2 = input("Enter new MAC address :")

    if is_valid_macaddr(a2) and a1.lower() in ["eth0", "eth1", "eth2", "wlan0", "wlan1", "wlan2", "wlx00c0ca98e507", "enp0s3"]:
        subprocess.call(["python3", "macchanger.py", "-i", a1, "-m", a2])
    else:
        print("Please type valid INTERFACE and MAC address")

def is_valid_macaddr(value):
    allowed = re.compile(r"""
                         (
                             ^([0-9A-F]{2}[-]){5}([0-9A-F]{2})$
                            |^([0-9A-F]{2}[:]){5}([0-9A-F]{2})$
                         )
                         """,
                         re.VERBOSE | re.IGNORECASE)

    if allowed.match(value) is None:
        return False
    else:
        return True


def network():
    print("""DEMO commands:- \npython3 network_scanner.py -r 192.168.10.0/24 \npython3 network_scanner.py --help
                     or    \nuse input mode given below (NOTE: Use commands only if input mode not working)
                                """)
    print("<input mode>")
    a1 = input("Enter ip Address/ipRange :")
    subprocess.call(["python3", "network_scanner.py", "-r", a1])


def arp():
    print("""DEMO commands:- \npython3 arp_spoof.py -t 192.168.10.19 -s 192.168.10.1 \npython3 arp_spoof.py --help
                     or    \nuse input mode given below (NOTE: Use commands only if input mode not working)
                                   """)
    print("<input mode>")
    a1 = input("Enter target ip address   :")
    a2 = input("Enter spoofing ip address :")
    subprocess.call(["python3", "arp_spoof.py", "-t", a1, "-s", a2])


def s1(a1, a2):
    # lock.acquire()
    x = subprocess.call(["python3", "arp_spoof.py", "-t", a1, "-s", a2])
    # lock.release()
    return x


def s2(a3):
    # lock.acquire()
    subprocess.check_call(["python3", "packet_sniffer.py", "-i", a3])
    # lock.release()


def sniff():
    print("""DEMO commands:- To use the sniffer you need to run two commands simultaneously separated by ';' 
    \npython3 arp_spoof.py -t 192.168.10.19 -s 192.168.10.1 ; python3 packet_sniffer.py -i eth0 \npython3 arp_spoof.py --help ; python3 packet_sniffer.py
                         or    \nuse input mode given below (NOTE: Use commands only if input mode not working)
                                       """)
    print("<input mode>")

    a3 = input("Enter interface :")
    subprocess.call(["python3", "packet_sniffer.py", "-i", a3])



def mitm():
    print("""DEMO commands:- \npython3 mitm_detector.py
                         or    \nuse input mode given below (NOTE: Use commands only if input mode not working)
                                       """)
    print("<input mode>")
    subprocess.call(["python3", "mitm_detector.py"])


try:
    while True:
        a = input("\nmain >>>")
        if a.lower() == "exit":
            break
        elif a == "1":
            mac()
        elif a == "2":
            network()
        elif a == "3":
            try:
                arp()
            except KeyboardInterrupt as e:
                continue
        elif a == "4":
            try:
                sniff()
            except KeyboardInterrupt as e:
                continue
        elif a == "5":
            try:
                mitm()
            except KeyboardInterrupt as e:
                continue
        elif a.lower() == "command":
            print("<command mode>")
            print("\n[###] WARNING: You are using command mode, this may harm your system!")
            try:
                while True:
                    command = input("\n### >")
                    if command.lower() == "exit":
                        print("\nclosing command mode...\n<command mode> CLOSED")
                        break
                    subprocess.call(command, shell=True)
            except KeyboardInterrupt as e:
                print("\n<command mode> FORCE CLOSED")
            except Exception as e:
                print(e)
                print("\n<command mode> CLOSED")
        else:
            print("To use system commands, start command mode.\ntype 'command'")
except KeyboardInterrupt as e:
    print("\nFORCE QUIT")
except Exception as e:
    print(e)
