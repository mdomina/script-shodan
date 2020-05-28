import shodan, ipaddress
def checkey(data, key):
    if key in data.keys():
        return data[key]
    return 'None'

def api(apikey, host):
    api = shodan.Shodan(apikey)

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
        last_update = checkey(data=results, key='last_update')

        print("[+] General:")

        # Print general info
        print("""
        IP: {}
        Organization: {}
        Country: {}
        Vulns: {}
        OS: {}
        Open Ports: {}
        Last Update: {}
        """.format(
                ip,
                org, 
                country, 
                vulns,
                os,
                ports,
                last_update
                )
            )
        print("[-] Details:")
        # Print port detail
        for item in results['data']:
            # check exists key
            product = checkey(data=item, key='product')
            port  = checkey(data=item, key='port')

            print("""
        Port: {}
        Demon: {}""".format(
                        port, 
                        product
                        )
                )
    except shodan.APIError as e:
            print('Error: {}'.format(e))

def net(ip):
    result = []
    # se è un range es: 8.8.8.8-50
    if '-' in ip:
        # divido il range [8.8.8.8, 50]
        ip_range = ip.split('-')
        # divido il primo il otteti
        octets = ip_range[0].split('.')
        for i in range( int(octets[3]), int(ip_range[1])+1 ):
            new_ip = octets[0] + '.' + octets[1] + '.' + octets[2] + '.' + str(i)
            result.append(new_ip)
    # se è un network es 8.8.8.0/24
    elif '/' in ip:
        net = ipaddress.ip_network(ip)
        for x in net.hosts():
            result.append(x)
    else:
        result.append(ip)
    
    return result
