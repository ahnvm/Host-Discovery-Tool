from scapy.all import *
from scapy.layers.inet import IP, ICMP
from concurrent.futures import ThreadPoolExecutor
import logging
import os
import colorama
from typing import List
from datetime import datetime
import time

colorama.init()

iplist = []

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

def ping(addr, args=None):
    global iplist
    ip_packet = IP()
    icmp_packet = ICMP()

    ping_packet = ip_packet / icmp_packet
    ping_packet.dst = addr

    silent = False
    verbose = False

    if args:
        for item in args:
            if item == "-s":
                silent = True
            elif item == "-v":
                verbose = True

    if silent:
        logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
    elif verbose:
        logging.getLogger("scapy.runtime").setLevel(logging.INFO)
    else:
        logging.getLogger("scapy.runtime").setLevel(logging.WARNING)

    response = sr1(ping_packet, timeout=1, verbose=verbose)

    if response:
        iplist.append((addr, "up", time.time()))
    else:
        iplist.append((addr, "down", time.time()))

    if not silent:
        logging.info(f"{colorama.Fore.CYAN}Finished sending 1 packet to IP {addr}{colorama.Style.RESET_ALL}")
        logging.info(f"{colorama.Fore.CYAN}Received 1 packet from IP {addr}, got {1 if response else 0} answers, remaining {1 if not response else 0} packets{colorama.Style.RESET_ALL}")

def scan_network(ip, ip_range, args) -> List:
    with ThreadPoolExecutor(max_workers=32) as executor:
        ip_range = [f"{ip}.{i}" for i in range(ip_range[0], ip_range[1]+1)]
        executor.map(lambda addr: ping(addr, args), ip_range)
    return iplist

def print_results(outlist):
    if not outlist:
        print(f"{colorama.Fore.RED}No results to display{colorama.Style.RESET_ALL}")
        return

    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

    try:
        sorted_iplist = sorted(outlist, key=lambda x: int(x[0].split(".")[3]))
    except ValueError as e:
        print(f"{colorama.Fore.RED}Error sorting IPs: {e}{colorama.Style.RESET_ALL}")
        return

    for ip, status, timestamp in sorted_iplist:
        formatted_time = datetime.fromtimestamp(timestamp).strftime("[%Y-%m-%d/%H:%M]")
        if status == "up":
            print(f"{colorama.Fore.YELLOW}{formatted_time} {colorama.Fore.GREEN}{ip} is {status}{colorama.Style.RESET_ALL}")
        else:
            print(f"{colorama.Fore.YELLOW}{formatted_time} {colorama.Fore.RED}{ip} is {status}{colorama.Style.RESET_ALL}")
    
    print(f"{colorama.Fore.YELLOW}Total IPs scanned: {len(sorted_iplist)}{colorama.Style.RESET_ALL}")
    print(f"{colorama.Fore.YELLOW}Total IPs up: {len([x for x in sorted_iplist if x[1] == 'up'])}{colorama.Style.RESET_ALL}")
    print(f"{colorama.Fore.YELLOW}Total IPs down: {len([x for x in sorted_iplist if x[1] == 'down'])}{colorama.Style.RESET_ALL}")
    print(f"{colorama.Fore.YELLOW}Press enter to continue...{colorama.Style.RESET_ALL}")
    try:
        input()
    except KeyboardInterrupt:
        print(f"{colorama.Fore.YELLOW}Exiting...{colorama.Style.RESET_ALL}")
        sys.exit(0)
    except EOFError:
        print(f"{colorama.Fore.YELLOW}Exiting...{colorama.Style.RESET_ALL}")
        sys.exit(0)    
