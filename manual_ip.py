"""
print(ip.ip_address(ip_input))
net4 = ip.ip_network(f'{ip_input}/{sub_mask}', strict=False)
network_addr = ip.ip_interface(f'{ip_input}/{sub_mask}')
print(network_addr.network)
print(net4.netmask)
print(net4.hostmask)
print(net4.num_addresses)
print(net4[1])
print(net4[-1])
#for x in net4.hosts():
#	print(x)
"""

ip = input("Enter the ip address")
submask = input("Enter the submask")
net_bin = []

def cidr_to_netmask(cidr): ## convert 24 to binary subnet mask
	cidr = int(cidr)
	mask = (0xffffffff >> (32 - cidr)) << (32 - cidr)
	return (str( (0xff000000 & mask) >> 24)   + '.' + str( (0x00ff0000 & mask) >> 16)   + '.' + str( (0x0000ff00 & mask) >> 8)    + '.' + str( (0x000000ff & mask)))

def ip_to_binary(ip):
	bin_ip =  '.'.join([bin(int(x)+256)[3:] for x in ip.split('.')])
	return bin_ip

def bin_to_ip(bina):
	bin_ip= '.'.join(str(int(x, 2)) for x in net_bin)
	return bin_ip

def network_address_generation(sub_split,ip_split):
	for i in range(0,len(sub_split)):
		if sub_split[i] == "11111111":
			net_bin.append(ip_split[i])
		else:
			net_bin.append("00000000")
	return net_bin	

def broadcast_address_gen(submask,network):
	flag =0
	for i in range(0,len(submask)):
		for j in range(0,len(submask[i])):
			if j == "1":
				pass
			else:
				flag = 1
				break
		if flag == 1:
			broad.append("")
		else:
			broad.append(network[i])
bin_ip = ip_to_binary(ip)
bin_meta = cidr_to_netmask(submask)
bin_sub = ip_to_binary(bin_meta)

ip_split = bin_ip.split('.')
sub_split = bin_sub.split('.')
net_bin = network_address_generation(sub_split,ip_split)
network_addr = bin_to_ip(net_bin)

print(bin_ip)
print(bin_sub)
print(network_addr)

broadcast_addr = broadcast_address_gen(sub_split,net_bin)



