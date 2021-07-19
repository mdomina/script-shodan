import configparser
from utility import split_network
from utility import api_shodan

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