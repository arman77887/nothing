import time
import sys
import colorama
from colorama import Fore, Style

# Initialize colorama
colorama.init()

def print_lyrics():
    lyrics = [
        f"{Fore.CYAN}Haathon ko sambhale mere haathon meni{Style.RESET_ALL}",
        f"{Fore.YELLOW}kaise haathon ko sambhale mere haathon meni{Style.RESET_ALL}",
        f"{Fore.GREEN}jab tak neend na aaya, inn lakeeron meni{Style.RESET_ALL}",
        f"{Fore.MAGENTA}Baateni hon..........{Style.RESET_ALL}",
        f"{Fore.RED}Haayee........{Style.RESET_ALL}"
    ]
    
    delays = [1.0, 0.1, 1.22, 0.9, 0.8]
    
    print(f"{Fore.BLUE}Arz kya hai?...........\n{Style.RESET_ALL}")
    time.sleep(1.4)
    
    for i, line in enumerate(lyrics):
        for char in line:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.03)  # Slightly faster typing
        print()
        time.sleep(delays[i])

def main():
    print(f"{Fore.WHITE}{'='*50}{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}🎵 Lyrics Display System 🎵{Style.RESET_ALL}")
    print(f"{Fore.WHITE}{'='*50}{Style.RESET_ALL}\n")
    
    print_lyrics()
    
    print(f"\n{Fore.GREEN}✅ Song completed!{Style.RESET_ALL}")

if __name__ == "__main__":
    main()
