import aiohttp
import asyncio
import random
from datetime import datetime
from colorama import init, Fore, Style

# Initialize Colorama for terminal colors
init(autoreset=True)

# Set window title
print(f"\033]0;Quantum Stressor X1 - Nightmare Overdrive\007", end="", flush=True)

# Startup message
print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT + """
If you don't have a clue how to use a script or any servers, head to 
https://nightmare-stresser.co and we will give you a FREE shared booter 
login for Nightmare Stresser, 100% free! Just make a ticket and mention 
you want the free booter shared account login.
""")

# ASCII Art (Futuristic, cinematic)
ASCII_ART = f"{Fore.LIGHTCYAN_EX}{Style.BRIGHT}\n" \
            f"  ╔════════════════════════════════════════════╗\n" \
            f"  ║         Quantum Stressor X1                ║\n" \
            f"  ║     Nightmare Overdrive - Classified       ║\n" \
            f"  ║  Developed by:   nightmare-stresser.co     ║\n" \
            f"  ║  Quantum-Powered Network Stress Suite      ║\n" \
            f"  ╚════════════════════════════════════════════╝\n"

# Simulated API response
async def simulate_api_call(url: str) -> str:
    print(Fore.YELLOW + f"Sending request to {url}...")
    await asyncio.sleep(1)  # Simulate network delay
    print(Fore.GREEN + "Response: Attack sent successfully!")
    return "sent"

# API interaction for sending attacks
async def send_attack(api_key: str, method: str, host: str, port: int, time: float, concurrents: int = 1):
    url = f"https://api.nightmare-stresser.com/?key={api_key}&method={method}&host={host}&port={port}&time={time}&concurrents={concurrents}"
    return await simulate_api_call(url)

# API interaction for stopping attacks
async def stop_attack(api_key: str, host: str, port: int, time: float, concurrents: int = 1):
    url = f"https://api.nightmare-stresser.com/?key={api_key}&method=STOP&host={host}&port={port}&time={time}&concurrents={concurrents}"
    return await simulate_api_call(url)

# API interaction for stopping all attacks
async def stop_all_attacks(api_key: str):
    url = f"https://api.nightmare-stresser.com/?key={api_key}&method=STOPALL"
    return await simulate_api_call(url)

# Validation Function
def validate_input(prompt: str, min_val: float, max_val: float, input_type=float) -> float:
    while True:
        try:
            value = input_type(input(Fore.LIGHTCYAN_EX + prompt))
            if min_val <= value <= max_val:
                return value
            print(Fore.RED + f"Value must be between {min_val} and {max_val}!")
        except ValueError:
            print(Fore.RED + "Invalid input! Numbers only.")

# Credits Function
def show_credits():
    print(Fore.LIGHTCYAN_EX + "\n" + "═"*50)
    print(Fore.LIGHTCYAN_EX + "        Quantum Stressor X1 Credits")
    print(Fore.LIGHTCYAN_EX + "═"*50)
    print(Fore.LIGHTCYAN_EX + "Developed by: https://nightmare-stresser.co")
    print(Fore.LIGHTCYAN_EX + "Purpose: Simulated quantum network stress testing")
    print(Fore.LIGHTCYAN_EX + "Features: Layer 4 & 7 Quantum Attacks via Nightmare API")
    print(Fore.LIGHTCYAN_EX + "Legal Note: Fictional tool for cinematic use only")
    print(Fore.LIGHTCYAN_EX + "═"*50 + "\n")

# Main Menu
async def main():
    api_key = input(Fore.LIGHTCYAN_EX + "Enter Nightmare Stresser API Key: ")
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(ASCII_ART)
    print(Fore.LIGHTCYAN_EX + f"API Key Authenticated: {api_key[:4]}****")
    print(Fore.LIGHTCYAN_EX + f"System Time: {current_time}\n")

    layer4_methods = [
        "DNS", "ACK", "GAME-FIVEM", "GAME-SOURCE", "UDP-MIX", "MINECRAFT",
        "TCP-AMP", "TCP-GEO-BYPASS", "UDP-BYPASS", "TCP-SYN", "DNS-R",
        "TCP-RAND", "TCP-OVH", "REVERSE-REFLECTION", "SYN-ACK",
        "TCP-BYPASSv1", "TCP-BYPASSv2", "UDP-GEO-BYPASS"
    ]
    layer7_methods = [
        "AUTO-BYPASS", "BYPASSv2", "SOCKET-SPAM", "HTTP-SPAMMER",
        "AUTO-BYPASSv2", "TOR"
    ]

    while True:
        print(Fore.LIGHTCYAN_EX + "Quantum Modules:")
        print("  1. Layer 4 Attacks")
        print("  2. Layer 7 Attacks")
        print("  3. Stop Attack")
        print("  4. Stop All Attacks")
        print("  5. Credits")
        print("  0. Exit Quantum Matrix")
        category = input(Fore.LIGHTCYAN_EX + "Select module (0-5): ").strip()

        if category == "0":
            print(Fore.RED + "Shutting down Quantum Matrix...")
            break
        elif category == "1":
            print(Fore.LIGHTCYAN_EX + "\nLayer 4 Attacks:")
            for i, method in enumerate(layer4_methods, 1):
                print(f"  {i}. {method}")
            method_idx = input(Fore.LIGHTCYAN_EX + "Select attack (1-18): ").strip()
            if method_idx.isdigit() and 1 <= int(method_idx) <= len(layer4_methods):
                method = layer4_methods[int(method_idx) - 1]
                host = input(Fore.LIGHTCYAN_EX + "Enter target IP: ")
                port = validate_input("Enter port (1-65535): ", 1, 65535)
                time = validate_input("Enter duration (seconds): ", 1, 3600)
                concurrents = validate_input("Enter concurrents (1-100): ", 1, 100, int)
                await send_attack(api_key, method, host, port, time, concurrents)
            else:
                print(Fore.RED + "Invalid attack!")
        elif category == "2":
            print(Fore.LIGHTCYAN_EX + "\nLayer7 Attacks:")
            for i, method in enumerate(layer7_methods, 1):
                print(f"  {i}. {method}")
            method_idx = input(Fore.LIGHTCYAN_EX + "Select attack (1-6): ").strip()
            if method_idx.isdigit() and 1 <= int(method_idx) <= len(layer7_methods):
                method = layer7_methods[int(method_idx) - 1]
                host = input(Fore.LIGHTCYAN_EX + "Enter target IP or domain: ")
                port = 80 if method in ["HTTP-SPAMMER", "AUTO-BYPASS", "AUTO-BYPASSv2", "TOR"] else validate_input("Enter port (1-65535): ", 1, 65535)
                time = validate_input("Enter duration (seconds): ", 1, 3600)
                concurrents = validate_input("Enter concurrents (1-100): ", 1, 100, int)
                await send_attack(api_key, method, host, port, time, concurrents)
            else:
                print(Fore.RED + "Invalid attack!")
        elif category == "3":
            host = input(Fore.LIGHTCYAN_EX + "Enter target IP: ")
            port = validate_input("Enter port (1-65535): ", 1, 65535)
            time = validate_input("Enter duration (seconds): ", 1, 3600)
            concurrents = validate_input("Enter concurrents (1-100): ", 1, 100, int)
            await stop_attack(api_key, host, port, time, concurrents)
        elif category == "4":
            await stop_all_attacks(api_key)
        elif category == "5":
            show_credits()
        else:
            print(Fore.RED + "Invalid module!")

if __name__ == "__main__":
    asyncio.run(main())
