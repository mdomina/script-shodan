import argparse
from api import api, net

parser = argparse.ArgumentParser(description='CTI Shodan')
parser.add_argument('--api', help='Shodan API Key', type=str, required=True)

# gruppo ad esclusione per la gestione del target
targetGroup = parser.add_mutually_exclusive_group()
targetGroup.add_argument('--target', help='Single target host/ip', type=str)
targetGroup.add_argument('--file', help='Read host/ip from file txt', type=str)

# istanzio gli argomenti
args = parser.parse_args()

if args.target:
    api(apikey=args.api, host=args.target)
elif args.file:
    with open(args.file, 'r') as f:
        # leggo ogni riga del file 
        for row in f:
            list_ip = net(row.rstrip())
            for ip in list_ip:
                api(apikey=args.api, host=ip)