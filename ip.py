"""Project:
1.Create GUI subnet calculator.
	-Take IP address input
	-Take subnet mask as input
	-Display IP adresss,subnet mask,Network address,Broadcast address,No.of available IP address,Range

"""
import tkinter as tk
import ipaddress as ip
import os

os.system("banner Subnet Calculator")
win = tk.Tk()
win.title("Subnet Calculator")
win.geometry("600x400")

left_fr = tk.Frame(win)
left_fr.grid(row=0,column=0)

right_fr = tk.Frame(win)
right_fr.grid(row=0,column=2)

#creating variables
ip_addr = tk.StringVar(left_fr)
sub_mask = tk.StringVar(left_fr)
network_addr = tk.StringVar(left_fr)
net4 = tk.StringVar(left_fr)
ip_data = tk.StringVar(left_fr)
net_data = tk.StringVar(left_fr)
total_data = tk.StringVar(left_fr)
range_data = tk.StringVar(left_fr)
sub_data = tk.StringVar(left_fr)
def display():
	net4 = ip.ip_network(f'{ip_addr.get()}/{sub_mask.get()}', strict=False)
	network_addr = ip.ip_interface(f'{ip_addr.get()}/{sub_mask.get()}')
	ip_data.set(ip.ip_address(f'{ip_addr.get()}'))#ipaddress
	sub_data.set(net4.netmask)#subnet address
	net_data.set(network_addr.network)#network address
	total_data.set(net4.num_addresses)#total host
	range_data.set(f'{net4[1]} - {net4[-1] }')#range of hosts
	
tk.Label(left_fr,text = "IP Address").grid(row=0,column=0)
ip_addr = tk.Entry(left_fr,textvariable=ip_addr)
ip_addr.grid(row=0,column=1)

tk.Label(left_fr,text = "Subnet Mask").grid(row=1,column=0)
sub_mask = tk.Entry(left_fr,textvariable=sub_mask)
sub_mask.grid(row=1,column=1)

tk.Button(left_fr,text="Display",command = display).grid(row=2,column=1)

tk.Label(left_fr,text = "IP Address	:").grid(row=3,column=0)
ip_box = tk.Label(left_fr,textvariable=ip_data)
ip_box.grid(row=3,column=1)

tk.Label(left_fr,text = "Subnet Mask	:").grid(row=4,column=0)
sub_box = tk.Label(left_fr,textvariable=sub_data)
sub_box.grid(row=4,column=1)

tk.Label(left_fr,text = "Network Address	:").grid(row=5,column=0)
net_box = tk.Label(left_fr,textvariable=net_data)
net_box.grid(row=5,column=1)

tk.Label(left_fr,text = "Total Host	:").grid(row=6,column=0)
total_box = tk.Label(left_fr,textvariable=total_data)
total_box.grid(row=6,column=1)


tk.Label(left_fr,text = "Range Host	:").grid(row=8,column=0)
range_box = tk.Label(left_fr,textvariable=range_data)
range_box.grid(row=8,column=1)


win.mainloop()
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
