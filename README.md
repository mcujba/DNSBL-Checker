# DNSBL Checker

This repository contains a Python script designed to check a range of IP addresses against multiple DNS-based blackhole lists (DNSBLs). DNSBLs are used to identify and block IP addresses involved in sending spam and other malicious activities. This script helps network administrators and email server managers ensure their IP addresses are not listed on these blacklists, which can affect email deliverability and network reputation.

## Features

- **IP Range Scanning**: Checks a specified range of IP addresses within a given subnet against multiple DNSBL providers.
- **Customizable DNSBL Providers**: Easily modify the list of DNSBL providers to include or exclude specific lists.
- **Colored Output**: Provides color-coded results for better readability:
  - **Green**: IP not listed
  - **Red**: IP listed
  - **Yellow**: Query timeout
- **Error Handling**: Gracefully handles DNS resolution errors, timeouts, and other exceptions.
- **Command-Line Arguments**: Accepts subnet range as a command-line argument in CIDR notation.

## Prerequisites

- Python 3.x
- `dnspython` library
- `colorama` library

Install the required libraries using pip:

```bash
pip install dnspython colorama
```

## Usage

Clone the repository and navigate to the directory:

```bash

git clone https://github.com/yourusername/dnsbl-checker.git
cd dnsbl-checker
```

Run the script with the desired subnet:

```bash

python3 blacklist-check.py 185.226.106.0/24
```

This command will check all IP addresses in the range 185.226.106.1 to 185.226.106.255 against the specified DNSBL providers and display the results with appropriate color codes.

## Customizing DNSBL Providers

To customize the list of DNSBL providers, edit the dnsbl_providers list in the script:

```python

dnsbl_providers = [
    'zen.spamhaus.org',
    'bl.spamcop.net',
    'b.barracudacentral.org',
    'cbl.abuseat.org',
    'pbl.spamhaus.org',
    'sbl.spamhaus.org'
]
```

Add or remove DNSBL providers as needed.

### Example Output

```bash 

185.226.106.1 is not listed in zen.spamhaus.org
185.226.106.1 is listed in bl.spamcop.net: 127.0.0.2
185.226.106.1 timeout while querying b.barracudacentral.org
...
```
