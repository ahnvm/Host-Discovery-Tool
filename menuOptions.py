import sys
import os
import discoverer
import colorama
from datetime import datetime

colorama.init(autoreset=True)

osname = os.name

def clear():
    if osname == "nt":
        os.system("cls")
    else:
        os.system("clear")

def set_ip() -> str:
    while True:
        try:
            ip = input(f"{colorama.Fore.CYAN}Enter IP Pattern (like 127.0.0): {colorama.Style.RESET_ALL}")
            ip_list = ip.split(".")
            ip_list = [int(i) for i in ip_list]
            if len(ip_list) == 3:
                if ip_list[0] < 0 or ip_list[0] > 255 or ip_list[1] < 0 or ip_list[1] > 255 or ip_list[2] < 0 or ip_list[2] > 255:
                    clear()
                    print(f"{colorama.Fore.RED}[Input Error] Invalid IP{colorama.Style.RESET_ALL}")
                else:
                    return ip
            else:
                clear()
                print(f"{colorama.Fore.RED}[Input Error] Invalid IP{colorama.Style.RESET_ALL}")
        except ValueError:
            clear()
            print(f"{colorama.Fore.RED}[Input Error] Invalid IP{colorama.Style.RESET_ALL}")
            continue
        except KeyboardInterrupt:
            print(f"\n{colorama.Fore.YELLOW}Exiting...{colorama.Style.RESET_ALL}")
            sys.exit(0)
        except EOFError:
            print(f"\n{colorama.Fore.YELLOW}Exiting...{colorama.Style.RESET_ALL}")
            sys.exit(0)

def set_ip_range() -> list:
    while True:
        try:
            ipRange = input(f"{colorama.Fore.CYAN}Enter IP Range (like 15 27): {colorama.Style.RESET_ALL}")
            ipRange_list = ipRange.split(" ")
            if len(ipRange_list) == 2:
                try:
                    ipRange_list = [int(i) for i in ipRange_list]
                    if ipRange_list[0] < 0 or ipRange_list[0] > 255 or ipRange_list[1] < 0 or ipRange_list[1] > 255:
                        clear()
                        print(f"{colorama.Fore.RED}[Input Error] Invalid IP Range{colorama.Style.RESET_ALL}")
                    elif ipRange_list[0] >= ipRange_list[1]:
                        clear()
                        print(f"{colorama.Fore.RED}[Input Error] Invalid IP Range{colorama.Style.RESET_ALL}")
                    else:
                        return ipRange_list
                except ValueError:
                    clear()
                    print(f"{colorama.Fore.RED}[Input Error] Invalid IP Range{colorama.Style.RESET_ALL}")
            else:
                clear()
                print(f"{colorama.Fore.RED}[Input Error] You must enter 2 IP addresses{colorama.Style.RESET_ALL}")
        except ValueError:
            clear()
            print(f"{colorama.Fore.RED}[Input Error] Invalid IP Range{colorama.Style.RESET_ALL}")
            continue
        except KeyboardInterrupt:
            clear()
            print(f"\n{colorama.Fore.YELLOW}Exiting...{colorama.Style.RESET_ALL}")
            sys.exit(0)
        except EOFError:
            clear()
            print(f"\n{colorama.Fore.YELLOW}Exiting...{colorama.Style.RESET_ALL}")
            sys.exit(0)

def save_results(outlist):
    if not outlist:
        print(f"{colorama.Fore.RED}No results to save{colorama.Style.RESET_ALL}")
        return

    try:
        sorted_iplist = sorted(outlist, key=lambda x: int(x[0].split(".")[3]))
    except ValueError as e:
        print(f"{colorama.Fore.RED}Error sorting IPs: {e}{colorama.Style.RESET_ALL}")
        return

    with open("results.txt", "w") as f:
        for ip, status, timestamp in sorted_iplist:
            formatted_time = datetime.fromtimestamp(timestamp).strftime("[%Y-%m-%d/%H:%M]")
            f.write(f"{formatted_time} {ip} is {status}\n")

    print(f"{colorama.Fore.YELLOW}Results saved to results.txt{colorama.Style.RESET_ALL}")
def pingOption(ip, ip_range, args) -> list:
    return discoverer.scan_network(ip, ip_range, args)
