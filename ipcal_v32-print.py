import ipaddress
#Main function()
while True:
  while True:
    try:
       net = input("Please enter an IPv4/IPv6 host address or network address: ")
       ipaddress.ip_interface(net)
       break;
    except ValueError:
       print("Oops!  That was no valid IPv4 or IPv6 address.  Try again...")
  while True:
     try:
       mask = input("Please enter a regular network mask in any following format like /8 /16 /0.0.0.255 /64 /120: ")
       netaddr = ipaddress.ip_interface(net + mask)
       break;
     except ValueError:
       print("Oops! Invalid mask. Try again...")
  m_net = ipaddress.ip_network(netaddr.network)
   #Input the maximum IP address that would be created
  while True:
     try:
       max_add = input("Please enter the maximum IP address that would be created (Optional- if leaving it blank, the default value is maximum IPv4 or IPv6 address) \n")
       if max_add == "":
          if m_net.version == 4:
             max_add = "255.255.255.255"
          elif m_net.version == 6:
             max_add = "FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF"
       ipaddress.ip_interface(max_add)
       if ipaddress.ip_address(net) < ipaddress.ip_address(max_add):
          break;
       else:
           print("Oops! Please make sure the maximum IP address is greater than the start IP address. Try again...")
     except ValueError:
        print("Oops!  That was no valid IPv4 or IPv6 address. Try again...")

#Calculate the maximum subnets should be allowed to create
  cal_m1 = int(ipaddress.ip_address(max_add)) - int(ipaddress.ip_address(net)) + 1
  max_nets = cal_m1 // m_net.num_addresses
  if cal_m1 % m_net.num_addresses != 0:
        max_nets += 1
  print ("Maxium subnets that can be allocated are: ", max_nets)   
# rep = 1
  while True:
      try:
         rep_str = input("How many subnets do you want to create: the default value is 1\n")
         if rep_str == "":
           rep = 1
           break
         rep = int(rep_str)
         if rep <= max_nets:
             break;
         else:
            print("Oops! Please ensure the amount of subnets is less than the maximum allowed subnets shown above. Try again...")   
      except ValueError:
            print("Oops!  That was not an integer. Try again...")
  j = 1
  max_ip = ipaddress.ip_address(max_add)
  prefix_str = "/" + str(m_net.prefixlen)
  while j <= rep:
        print ('--------------------------------------------------------------------\n')
        print('Subnet index:',j)
        print ('Network address:',m_net[0])
        print ('Prefix length: ',prefix_str)
        print ('Subnet Mask:',m_net.netmask)
        if m_net.version == 4:
           print ('IPv4 Host/Reverse Mask:',ipaddress.ip_network(m_net).hostmask)
           print ('The first host address:', m_net[1])
        m_last = m_net[-1]
        if m_net.version == 6:
           print ('The first host address:', m_net[1])
           if max_ip in m_net:
             print('The last available host IP: ', max_ip)
           else:
             print ('The last host address:', m_last)
        else:
           if max_ip in m_net:
              print('The last available host IP: ', max_ip)
           else:
              print ('The last host address:', m_last - 1)
              print ('The broadcast address:', m_last)
        netaddr = str(m_last + 1) + mask
        m_net = ipaddress.ip_network(netaddr)
        j += 1
  cont_pro = ''
  cont_pro = input("Continue -- Y/y Exit -- Other key:")
  if (cont_pro == 'Y') or (cont_pro == 'y'):
      continue
  else:
      break
   
