import nmap3 #from nmap3 import *
import pprint as pp
import requests

testrange = '127.0.0.1'

nm = nmap3.Nmap()

if __name__ == "__main__":
    pp.pprint(nm.scan_top_ports(testrange))