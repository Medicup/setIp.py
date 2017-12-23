#!/usr/bin/python3
import os
import sys
import time

netpath = "/etc/network/interfaces"
cwd = os.getcwd()
timestr = time.strftime("%Y%m%d-%H%M%S")
net1 = 'ens160'
net2 = 'ens192'
add = 'address'
mask = 'netmask'
gate = 'gateway'
dns = 'dns-nameservers'

print ('cp %s %s-%s' % (netpath, netpath, timestr))
def ipBackup():
  os.system('cp %s %s-%s' % (netpath, netpath, timestr))
  os.system('rm %s' % (netpath))

def createInterface():
  net1_ip = input('Enter %s ip address: ' % (net1))
  net1_mask = input('Enter %s netmask: ' % (net1))
  net1_gate = input('Enter %s gateway: ' % (net1))
  net1_dns = input('Enter %s : ' % (dns))
  net2_ip = input('Enter %s ip address: ' % (net2))
  net2_mask = input('Enter %s netmask: ' % (net2))

  # create a new file
  f = open(netpath, 'w')
  f.write('source /etc/network/interfaces.d/* \n\n')
  f.write('# the loopback network interface \n')
  f.write('auto lo \n')
  f.write('iface lo inet loopback \n\n ')
  f.write('# the primary network interface %s \n' % (net1))
  f.write('auto %s \n' % (net1))
  f.write('iface %s inet static \n' % (net1))
  f.write('\t %s %s \n' % (add, net1_ip))
  f.write('\t %s %s \n' % (mask, net1_mask))
  f.write('\t %s %s \n' % (gate, net1_gate))
  f.write('\t %s %s \n\n' % (dns, net1_dns))
  f.write('# the secondary network interface %s \n' % (net2))
  f.write('auto %s \n' % (net2))
  f.write('iface %s inet static \n' % (net2))
  f.write('\t %s %s \n' % (add, net2_ip))
  f.write('\t %s %s \n' % (mask, net2_mask))
  f.close()

ipBackup()
createInterface()

