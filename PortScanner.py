import socket
import threading
import sys
import timeit

class scanner():
    def __init__(self):
        self.threadCollector = []
        self.OpenPorts = []
        self.HOST = "localhost"

    def ScanPort (self,host, port):
        with socket.socket() as sock:
            try: 
                sock.connect((host, port))
                self.OpenPorts.append(port)
            except Exception as e:
                #print (f'{port} not accessable')
                pass

    def ScanPorts (self, range_a, range_b):
        for i in range(range_a, range_b):
            t1  = threading.Thread(target=self.ScanPort, args=(self.HOST, i))
            self.threadCollector.append(t1)
        
        #start threads
        for i in self.threadCollector: 
            i.start()

        #join to main thread
        for i in self.threadCollector: 
            i.join()

        self.OpenPorts.sort()


def main():
    scan = scanner()
    s = timeit.default_timer()
    scan.ScanPorts(int(sys.argv[1]), int(sys.argv[2]))
    e = timeit.default_timer()
    print (f"{round(e - s, 4)} Secs")
    print(len(scan.OpenPorts))
    print(scan.OpenPorts)


main()
