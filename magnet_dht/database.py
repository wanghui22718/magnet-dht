#!/usr/bin/env python
# coding=utf-8
from ctypes import sizeof
import random
import time

class RedisClient:
    def __init__(self, ):
        self.all = 0
        self.ttimes = {}

    def add_magnet(self, magnet):
        # print(magnet)
        
        if magnet in self.ttimes:
            self.ttimes[magnet] += 1
        else:
            self.ttimes[magnet] = 1

        self.all += 1
        if self.all %1000 ==0:
            with open('/root/workspace/magnet-dht/dhtlist.txt', 'a') as f:
                f.write(f'got {self.all//1000}k links ...\n')
                f.flush()
            if self.all % 100000 == 0 :
                show_times = []
                for k, v in self.ttimes.items():
                    if v > 16:
                        show_times.append((k, v))

                std_times = sorted(show_times, key=lambda x:x[1], reverse=True)
                with open('/root/workspace/magnet-dht/dhtlist.txt', 'a') as f:
                    for x in std_times:
                        f.write(f'magnet:?xt=urn:btih:{x[0]}\n{x[1]}\n')
                    f.write(f'total filter : {len(std_times)} links \n')
                    f.write(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
                    f.flush()

                
                self.ttimes.clear()

    

        

    def get_magnets(self, count=128):
        pass

if __name__ == "__main__":
    c = RedisClient()
    for i in range(1,100001):
        c.add_magnet(str(random.randrange(1,64)))
    # print(c.ttimes)
