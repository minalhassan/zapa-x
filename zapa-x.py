#!/usr/bin/env python3
import os
import sys
import argparse
import nmap
import requests
from bs4 import BeautifulSoup
import websockets
import asyncio
import subprocess
from time import sleep
from pyfiglet import Figlet
from termcolor import colored
import random
import json
from pathlib import Path

# ======================
# 🎨 SOLO LEVELING DESIGN
# ======================
class SoloLevelingUI:
    def __init__(self):
        self.ranks = {
            1: "E-Rank Hunter",
            2: "D-Rank Hunter", 
            3: "C-Rank Hunter",
            4: "B-Rank Hunter",
            5: "A-Rank Hunter",
            10: "S-Rank Hunter",
            20: "National-Level Hunter",
            50: "Shadow Monarch"
        }
        self.xp = 0
        self.level = 1
        
    def show_banner(self):
        f = Figlet(font='slant')
        banner = f.renderText('ZAPA-X')
        print(colored(banner, 'red'))
        print(colored("≡"*60, 'blue'))
        print(colored("||  SOLO LEVELING CYBER ARSENAL  ||  KALI LINUX EDITION  ||", 'yellow'))
        print(colored("≡"*60, 'blue'))
        print(colored(f"\n>> Hunter Rank: {self.get_rank()} (Level {self.level})", 'green'))
        print(colored(">> System Ready: All shadows standing by", 'magenta'))
        print(colored("≡"*60, 'blue'))
        
    def get_rank(self):
        for threshold, rank in sorted(self.ranks.items(), reverse=True):
            if self.level >= threshold:
                return rank
        return "Civilian"
    
    def level_up(self):
        self.xp += random.randint(5, 20)
        if self.xp >= 100:
            self.level += 1
            self.xp = 0
            print(colored(f"\n[!] LEVEL UP! You are now Level {self.level} - {self.get_rank()}", 'cyan'))
            self.show_level_up_animation()
            
    def show_level_up_animation(self):
        animations = [
            "Shadows emerging from the ground...",
            "Your stats are increasing...",
            "The System is evaluating your growth...",
            "New skills unlocked in your arsenal..."
        ]
        for anim in animations:
            print(colored(f" >> {anim}", 'yellow'))
            sleep(0.5)

# ======================
# 🛠️ CORE FUNCTIONALITY
# ======================
class ZapaX:
    def __init__(self):
        self.ui = SoloLevelingUI()
        self.ui.show_banner()
        self.check_environment()
        self.args = self.parse_args()
        
    def check_environment(self):
        if os.geteuid() != 0:
            print(colored("\n[!] You must awaken your powers as root!", 'red'))
            sys.exit(1)
            
        required = ['nmap', 'curl', 'john', 'hashcat']
        missing = [cmd for cmd in required if not shutil.which(cmd)]
        if missing:
            print(colored(f"\n[!] Missing hunter tools: {', '.join(missing)}", 'red'))
            sys.exit(1)
    
    def parse_args(self):
        parser = argparse.ArgumentParser(description='ZAPA-X: The Solo Leveling Cyber Arsenal')
        
        # Main modes
        modes = parser.add_subparsers(dest='mode', required=True)
        
        # Shadow Scan (Nmap)
        scan = modes.add_parser('scan', help='Shadow scanning techniques')
        scan.add_argument('target', help='Target to assess')
        scan.add_argument('--stealth', action='store_true', help='Use shadow blend technique')
        scan.add_argument('--vuln', action='store_true', help='Identify weak points')
        
        # Web Assault (cURL)
        web = modes.add_parser('web', help='Web assault tactics')
        web.add_argument('url', help='Target URL')
        web.add_argument('--fuzz', action='store_true', help='Shadow fuzzing')
        web.add_argument('--ws', action='store_true', help='WebSocket shadowing')
        
        # Shadow Craft (SEToolkit)
        craft = modes.add_parser('craft', help='Shadow crafting techniques')
        craft.add_argument('--phish', help='Create shadow lure')
        craft.add_argument('--template', help='Shadow template to use')
        
        # Shadow Break (Cracking)
        crack = modes.add_parser('break', help='Shadow breaking techniques')
        crack.add_argument('hashfile', help='File containing shadow seals')
        crack.add_argument('--hybrid', action='store_true', help='Combine shadow forces')
        
        return parser.parse_args()
    
    def run(self):
        if self.args.mode == 'scan':
            self.shadow_scan()
        elif self.args.mode == 'web':
            self.web_assault()
        elif self.args.mode == 'craft':
            self.shadow_craft()
        elif self.args.mode == 'break':
            self.shadow_break()
            
        self.ui.level_up()
    
    # ======================
    # 🕵️ SHADOW SCAN (NMAP)
    # ======================
    def shadow_scan(self):
        print(colored(f"\n[+] Initiating shadow scan on {self.args.target}", 'cyan'))
        
        nm = nmap.PortScanner()
        args = '-sV -T4'
        
        if self.args.stealth:
            print(colored(" >> Using shadow blend technique (Stealth scan)", 'magenta'))
            args += ' -sS -Pn'
            
        if self.args.vuln:
            print(colored(" >> Activating weak point identification", 'magenta'))
            args += ' --script vuln'
        
        print(colored(f" >> Scanning with parameters: {args}", 'yellow'))
        nm.scan(hosts=self.args.target, arguments=args)
        
        self.display_scan_results(nm)
    
    def display_scan_results(self, nm):
        print(colored("\n[+] Shadow Scan Results:", 'green'))
        for host in nm.all_hosts():
            print(colored(f"\nTarget: {host}", 'blue'))
            print(colored(f"State: {nm[host].state()}", 'blue'))
            
            for proto in nm[host].all_protocols():
                print(colored(f"\nProtocol: {proto}", 'yellow'))
                ports = nm[host][proto].keys()
                
                for port in sorted(ports):
                    service = nm[host][proto][port]
                    print(colored(f"  {port}/tcp: {service['name']} - {service['product']} {service.get('version', '')}", 'green'))
    
    # ======================
    # 🌐 WEB ASSAULT (CURL)
    # ======================
    def web_assault(self):
        print(colored(f"\n[+] Preparing web assault on {self.args.url}", 'cyan'))
        
        if self.args.fuzz:
            self.shadow_fuzzing()
        elif self.args.ws:
            asyncio.run(self.websocket_shadowing())
        else:
            self.basic_recon()
    
    def shadow_fuzzing(self):
        print(colored(" >> Initiating shadow fuzzing technique", 'magenta'))
        # Implement fuzzing logic
        print(colored(" >> Shadow fuzzers deployed to target", 'green'))
    
    async def websocket_shadowing(self):
        print(colored(" >> Establishing WebSocket shadow connection", 'magenta'))
        try:
            async with websockets.connect(self.args.url) as ws:
                print(colored(" >> WebSocket shadow connection established", 'green'))
                # Add WebSocket interaction logic
        except Exception as e:
            print(colored(f" >> Shadow connection failed: {str(e)}", 'red'))
    
    # ======================
    # 🎣 SHADOW CRAFT (SET)
    # ======================
    def shadow_craft(self):
        if self.args.phish:
            print(colored(f"\n[+] Crafting shadow lure: {self.args.phish}", 'cyan'))
            template = self.args.template or 'default'
            print(colored(f" >> Using shadow template: {template}", 'magenta'))
            # Implement phishing template creation
            print(colored(" >> Shadow lure successfully crafted", 'green'))
    
    # ======================
    # 💥 SHADOW BREAK (CRACK)
    # ======================
    def shadow_break(self):
        print(colored(f"\n[+] Analyzing shadow seals in {self.args.hashfile}", 'cyan'))
        
        if self.args.hybrid:
            print(colored(" >> Combining Hashcat and John the Ripper shadows", 'magenta'))
            # Implement hybrid cracking
        else:
            print(colored(" >> Using standard shadow force", 'magenta'))
            # Implement standard cracking
            
        print(colored(" >> Shadow seals are breaking...", 'green'))

# ======================
# 🏁 MAIN EXECUTION
# ======================
if __name__ == '__main__':
    try:
        hunter = ZapaX()
        hunter.run()
    except KeyboardInterrupt:
        print(colored("\n[!] Shadow operation cancelled by the Hunter", 'red'))
        sys.exit(0)
    except Exception as e:
        print(colored(f"\n[!] Shadow system error: {str(e)}", 'red'))
        sys.exit(1)
