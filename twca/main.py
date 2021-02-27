import nmap
import pprint as pp
import requests

nm = nmap.PortScanner()


class Scanner:
    def __init__(self, sS=False, sV=False, sT=False, sU=False, sX=False, target='127.0.0.1', ports='--p 22-443'):
        self.sS = sS
        self.sV = sV
        self.sT = sT
        self.sU = sU
        self.sX = sX
        self.target = target
        self.ports = ports
    

if __name__ == '__main__':
    lubina = Scanner(sS=True, sV=True)
    print(lubina.start_scan())














