import configparser
from utility import split_network
from utility import api_shodan
import argparse
from argparse import RawTextHelpFormatter

description = """
** Per eseguire il MikeShodanScript **
Acesso a Shoda:
[+] aggiungere l'APIkey di shodan nel file config.ini

Impostare i targets:
[+] aggiungere i targets nel file config.ini e usare l'opzione --target-file
[+] usare l'opzione --target <IP> --api <APIKEY>

[//] ATTENZIONE un metodo esclude l'altro [//]
"""
parser = argparse.ArgumentParser(description=description, formatter_class=RawTextHelpFormatter)
parser.add_argument('--target', help='Single target IP', type=str)
parser.add_argument('--api', help='APIkey Shodan', type=str)
parser.add_argument('--file', help='Legge il target dal file confing.ini', type=str)

# istanzio gli argomenti
args = parser.parse_args()

if args.target:
    api_shodan(args.api, args.target)
elif args.file:
    # file di configurazione
    config = configparser.ConfigParser()
    config.read('config.ini')
    apikey = config['shodan']['apikey']
    target_list = list()
    for section in config.sections():# ciclo tutte le sezioni
        if section == 'shodan':
            continue
        elif section == 'ip':
            for option in config.options(section):# ciclo tutte le opzioni di una singola sezione
                ip = config[section][option]
                target_list.append(ip)
        elif section == 'network':
            for option in config.options(section):
                network = config[section][option]
                ip_list = split_network(network)
                for ip in ip_list:
                    target_list.append(ip)

    for target in target_list:
        api_shodan(apikey, target)

