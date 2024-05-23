import sys

def ipv4_parser(hex):
    version = hex[0]

    header_length = int(hex[1],16)*4 # we multiply by 4 because we want the header length in bytes (a header goes from 20 bytes to 60 bytes)
    
    total_length = int(hex[4:8], 16) #length is usually said in decimal notation

    identification = hex[8:12] #stay in hexa

    time_to_live = int(hex[16:18], 16) 

    protocol = int(hex[18:20], 16) #only 3 cases
    if protocol == 17:
        protocol = "UDP"
    elif protocol ==1:
        protocol = "ICMP"
    else:
        protocol = "TCP"
    
    ipsrc = str(int(hex[24:26], 16)) + "." + str(int(hex[26:28], 16)) + "." + str(int(hex[28:30], 16))+ "." + str(int(hex[30:32], 16))
    ipdst = str(int(hex[32:34], 16)) + "." + str(int(hex[34:36], 16)) + "." + str(int(hex[36:38], 16))+ "." + str(int(hex[38:40], 16))
    
    return(f" version: {version}\n header length (bytes): {header_length}\n total length: {total_length}\n identification: 0x{identification}\n time to live: {time_to_live}\n protocol: {protocol}\n source IP: {ipsrc}\n destination IP: {ipdst}")

def main():
    file = sys.argv[1]
    i=0
    with open(file, 'r') as _file:
        for line in _file:
            i+=1
            hex = line.strip()
            result = ipv4_parser(hex)
            print(f"\n---------packet n°{i}-------------\n{result}\n")

if __name__ == "__main__":
    main()
