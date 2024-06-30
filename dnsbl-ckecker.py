import dns.resolver
import argparse
import ipaddress
from colorama import Fore, Style, init

# Initialize colorama
init()

def check_blacklist(ip):
    dnsbl_providers = [
        'zen.spamhaus.org',
	    'pbl.spamhaus.org',
	    'sbl.spamhaus.org'
        'bl.spamcop.net',
        'dnsbl.sorbs.net',
        'b.barracudacentral.org',
        'dnsbl-1.uceprotect.net',
        'dnsbl-2.uceprotect.net',
        'dnsbl-3.uceprotect.net',
	    'cbl.abuseat.org'
    ]
    
    reversed_ip = '.'.join(reversed(ip.split('.')))
    
    for provider in dnsbl_providers:
        query = f"{reversed_ip}.{provider}"
        try:
            answers = dns.resolver.resolve(query, 'A')
            for rdata in answers:
                print(f"{ip} is {Fore.RED}listed{Style.RESET_ALL} in {provider}: {rdata}")
        except dns.resolver.NXDOMAIN:
            print(f"{ip} is {Fore.GREEN}not listed{Style.RESET_ALL} in {provider}")
        except dns.resolver.Timeout:
            print(f"{ip} {Fore.YELLOW}timeout{Style.RESET_ALL} while querying {provider}")
        except dns.resolver.NoNameservers:
            print(f"No name servers found for {provider}")
        except dns.resolver.NoAnswer:
            print(f"{ip} is {Fore.GREEN}not listed{Style.RESET_ALL} in {provider}")

def main():
    parser = argparse.ArgumentParser(description='Check a range of IP addresses against DNSBL providers.')
    parser.add_argument('subnet', type=str, help='The subnet range in CIDR notation, e.g., xxx.xxx.xxx.0/24')
    args = parser.parse_args()

    try:
        network = ipaddress.ip_network(args.subnet, strict=False)
    except ValueError:
        print("Invalid subnet format. Please use the correct CIDR notation, e.g., xxx.xxx.xxx.0/24")
        return

    for ip in network.hosts():
        check_blacklist(str(ip))

if __name__ == '__main__':
    main()

