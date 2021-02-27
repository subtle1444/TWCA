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
    
    def get_scan_types(self):
        scan_type = str()
        if self.sS != False:
            scan_type += '-sS '
        if self.sV != False:
            scan_type += '-sV '
        if self.sT != False:
            scan_type += '-sT '
        if self.sU != False:
            scan_type += '-sU '
        if self.sX != False:
            scan_type += '-sX '
        return scan_type

if __name__ == '__main__':
    lubina = Scanner(sS=True, sV=True)
    print(lubina.get_scan_types())














