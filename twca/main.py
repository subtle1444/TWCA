import nmap
import pprint as pp
import requests

nm = nmap.PortScanner()


if __name__ == '__main__':
    output = nm.scan('127.0.0.1', '22-443')
    pp.pprint(output)