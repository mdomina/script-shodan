import shodan, ipaddress, time
from .logger import logger

def checkey(data, key):
    if key in data.keys():
        return data[key]
    return 'None'

def api_shodan(apikey, host):
    api = shodan.Shodan(apikey)
    time.sleep(1)
    try:
        # Search specific host in Shodan
        results = api.host(host)

        # check data result
        ip = checkey(data=results, key='ip_str')
        org = checkey(data=results, key='org')
        country = checkey(data=results, key='country_name')
        vulns = checkey(data=results, key='vulns')
        os = checkey(data=results, key='os')
        ports = checkey(data=results, key='ports')
        last_update = checkey(data=results, key='last_update')[:10]

        print("[+] General:")
        print("IP: {}".format(ip))
        print("Organization: {}".format(org))
        print("Country: {}".format(country))
        print("Vulns: {}".format(vulns))
        print("OS: {}".format(os))
        print("Open Ports: {}".format(ports))
        print("Last Update: {}".format(last_update))
        print()
        print("[-] Open Ports:")
        # Print port detail
        for item in results['data']:
            # check exists key
            product = checkey(data=item, key='product')
            port  = checkey(data=item, key='port')
            print("Port: {}".format(port))
            print("Demon: {}".format(product))
        print()
        print("***********************")
        print()
    except shodan.APIError as e:
            logger.error(e)

def split_network(ip):
    result = []
    net = ipaddress.ip_network(ip)
    for x in net.hosts():
        result.append(str(x))   
    return result

if __name__=='__main__':
    x = split_network("8.8.8.0/24")
    print(x)
