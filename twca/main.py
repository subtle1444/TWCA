try:
    import nmap
    import pprint as pp
    import requests
except ModuleNotFoundError as e:
    print(e)

nm = nmap.PortScanner()

class Scanner:
    def __init__(self, sS=False, sV=False, sT=False, sU=False, sX=False, target='127.0.0.1', ports='22-443'):
        self.sS = sS
        self.sV = sV
        self.sT = sT
        self.sU = sU
        self.sX = sX
        self.target = target
        self.ports = ports
    
    def get_scan_type(self):
        args = str()
        if self.sS == True:
            args += '-sS '
        if self.sV == True:
            args += '-sV '
        if self.sT == True:
            args += '-sT '
        if self.sU == True:
            args += '-sU '
        if self.sX == True:
            args += '-sX '
        return args
    
    def scan(self):
        out = nm.scan(hosts=self.target, arguments=self.get_scan_type()+f'-p {self.ports}')
        return out



if __name__ == '__main__':
    lubina = Scanner(sS=True, sV=True)
    print(lubina.scan())