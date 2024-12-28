import sys
import os
import menuOptions
import colorama

colorama.init(autoreset=True)

g_iplist = []
osname = os.name
g_ip = "0.0.0"
g_ipRange_list = [0, 255]

ascii_art = f"""
{colorama.Fore.CYAN}
           _    _ _   ___      ____  __   _______ ____   ____  _       _____ 
     /\   | |  | | \ | \ \    / /  \/  | |__   __/ __ \ / __ \| |     / ____|
    /  \  | |__| |  \| |\ \  / /| \  / |    | | | |  | | |  | | |    | (___  
   / /\ \ |  __  | . ` | \ \/ / | |\/| |    | | | |  | | |  | | |     \___ \ 
  / ____ \| |  | | |\  |  \  /  | |  | |    | | | |__| | |__| | |____ ____) |
 /_/    \_\_|  |_|_| \_|   \/   |_|  |_|    |_|  \____/ \____/|______|_____/ 
                                                                             
                                                {colorama.Fore.YELLOW}by https://github.com/ahnvm
{colorama.Style.RESET_ALL}
"""

def menuChoices(choice):
    global g_iplist
    global g_ipRange_list
    global g_ip 
    if choice == "1":
        g_iplist.clear()
        g_iplist = menuOptions.pingOption(g_ip, g_ipRange_list, [])
    elif choice == "2":
        g_iplist.clear()
        g_iplist = menuOptions.pingOption(g_ip, g_ipRange_list, ["-s"])
    elif choice == "3":
        g_iplist.clear()
        g_iplist = menuOptions.pingOption(g_ip, g_ipRange_list, ["-v"])
    elif choice == "4":
        g_ip = menuOptions.set_ip()
        menuOptions.clear()
    elif choice == "5":
        g_ipRange_list = menuOptions.set_ip_range()
        menuOptions.clear()
    elif choice == "6" and g_iplist:
        menuOptions.discoverer.print_results(g_iplist)
    elif choice == "7" and g_iplist:
        menuOptions.save_results(g_iplist)
    elif choice == "0":
        print(f"{colorama.Fore.YELLOW}Exiting... Goodbye!")
        sys.exit(0)
    else:
        print(f"{colorama.Fore.RED}[Input Error] Invalid option")

def main():
    while True:
        menuOptions.clear()
        print(ascii_art)
        print(f"{colorama.Fore.GREEN}1.{colorama.Style.RESET_ALL} Scan Network")
        print(f"{colorama.Fore.GREEN}2.{colorama.Style.RESET_ALL} Scan Network (Silent)")
        print(f"{colorama.Fore.GREEN}3.{colorama.Style.RESET_ALL} Scan Network (Verbose)")
        print(f"{colorama.Fore.GREEN}4.{colorama.Style.RESET_ALL} Set IP {colorama.Fore.YELLOW}(Current IP: {g_ip}.({g_ipRange_list[0]}-{g_ipRange_list[1]}))")
        print(f"{colorama.Fore.GREEN}5.{colorama.Style.RESET_ALL} Set IP Range {colorama.Fore.YELLOW}(Current Range: {g_ipRange_list})")
        if (g_iplist):
            print(f"{colorama.Fore.GREEN}6.{colorama.Style.RESET_ALL} Show Results")
        if (g_iplist):
            print(f"{colorama.Fore.GREEN}7.{colorama.Style.RESET_ALL} Save Results")
        print(f"{colorama.Fore.RED}0.{colorama.Style.RESET_ALL} Exit")
        try: 
            option = int(input(f"{colorama.Fore.CYAN}Enter option: {colorama.Style.RESET_ALL}"))
        except ValueError:
            print(f"{colorama.Fore.RED}[Input Error] Invalid option. Please enter a number.")
            continue
        except KeyboardInterrupt:
            print(f"\n{colorama.Fore.YELLOW}Exiting... Goodbye!")
            break
        except EOFError:
            print(f"\n{colorama.Fore.YELLOW}Exiting... Goodbye!")
            break
        menuChoices(str(option))

if __name__ == "__main__":
    main()
