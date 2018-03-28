sudo arptables -A INPUT --source-mac 8c:e2:da:f1:b6:f6 -j DROP
sudo arptables -A INPUT --source-mac 8c:e2:da:f1:b6:f5 -j DROP
sudo ip -s neighbour flush all

#reset = sudo arptables --flush
#real mac = 90:ef:68:7b:4f:e6
