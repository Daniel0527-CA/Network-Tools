import re
def verify_ip(source_ip):
    ip_str1 = ''
    temp = ''
    return_str = ''
    pattern = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')
    ip_str1 = pattern.search(source_ip,0)
    if ip_str1 == None:
        return return_str
    temp = ip_str1.group(0)   
    return_str = temp.split('.')
    return return_str

def input_para(para):
  while True:
        i = 0
        ip_str = ''
        ini_str = ''
        ip_list = []
        pass_verify = True
        ip_int = 0
        ip_str = input(para)
        ini_str = verify_ip(ip_str)
        if ini_str != '':
          while i < 4:
            try: 
               ip_int = int(ini_str[i])
            except ValueError:
               pass_verify = False 
               print("Oops! Please input a number between 0 and 255. Try again...")
               break
            if (ip_int >= 0) and (ip_int <= 255):
                i += 1
                ip_list.append(ip_int)
            else:
                pass_verify = False
                print("Oops! IP verification failed! Please input a number between 0 and 255. Try again...")
                break
          if (pass_verify == True):  
             break
        else:
            print("Input error! Try again!")
        cont_pro = ''   
        cont_pro = input("Continue -- Y/y Exit -- Other key:")
        if(cont_pro == 'Y') or (cont_pro == 'y'):
            continue
        else:
            break
  return ip_list

def copylist(source,count):
#Transforming a list into a 8 bit long binary list
      j = 2
      dest = []
      tmp = 0
      k = 0
      p = 8 - (count - 2)
      if count < 10:
      #Padding the leading 0 bits
          while k < p:
            dest.append('0')
            k += 1
      while j < count:
        dest.append(source[j])
        j += 1
      return dest

def get_1_bits(dest):
#Recording the location of 1 bit and returning the amount of 1 bits
     global loc
     total_len = len(dest)
     i = 0
     j = 0
     while i < total_len:
       if dest[i] == '1':
          loc.append(i)
          j += 1
       i += 1
     return j

def gen_ini_list(ini_list,li_len):
#Initializing a list for permutation 
     i = 0
     while i < li_len:
         ini_list.append('0')
         i += 1
     return ini_list

def fun(A, P, Index, n):
#Generating permutations
     global dest_list
     if Index == n:
        dest_list.append(list(P))
     else:
        i = 0
        for i in range(2):
          P[Index] = A[i]
          fun(A, P, Index + 1, n)

def convert_bin_to_decimal(result):
#Converting binary to decimal
     bin_len = len(result)
     i = 0
     sum_1 = 0
     tmp = 0
     m = 0
     while i < bin_len:
           tmp = int(pow(2,bin_len - i - 1))
           if(result[i] == '1'):
                m = 1
           else:
                m = 0       
           sum_1 += m * tmp
           i += 1
     return sum_1

def discover(ip_part,loc,dest_list):
#Returning the matching IP in decimal format
    tmp_l = []
    i = 0
    k = 0
    m = 0
    c_bin = []
    dst_str = ''
    tmp_2 = []
    while i < len(dest_list):
        j = 0
        tmp_l = dest_list[i]
        tmp_2 = list(ip_part)
        while j < len(loc):
        #Replacing the original value of 1 bit with new one in the list of dest_list
            k = loc[j]      
            tmp_2[k] = tmp_l[j]
            j += 1
        i += 1
        m = convert_bin_to_decimal(tmp_2)
        c_bin.append(m)
    return c_bin
 
def compact_num(source,num):
#Conslidating the sequential numbers into a range
      i = 1
      start = 0
      end = 0
      final_lst = []
      tmp = ''
      start = 0
      end = 0
      while i < num:
            if source[i] == source[i - 1] + 1:
                  end = i
                  if i == num - 1:
                      tmp = str(source[start]) + '-' + str(source[end])
                      final_lst.append(tmp)
                      break
            elif start < end:
                 tmp = str(source[start]) + '-' + str(source[end])
                 final_lst.append(tmp)
                 start = i
                 end = i
            else:
                 start = i
                 end = i
                 final_lst.append(source[i - 1])
                 if i == num - 1:
                    final_lst.append(source[i])
                    break
            i += 1
      return final_lst
          
#main function()
while True:
  para_ip = 'Please input an ip address in the format e.g. 10.0.0.1:'
  s_ip = []
  s_ip = input_para(para_ip)
  if s_ip == []:
    print("IP address input error!")
    break
  s_mask = []
  para_mask = 'Please input an wildcard mask in the format e.g. 0.0.2.3:'
  s_mask = input_para(para_mask)
  if s_mask == []:
    print("Mask input error!")
    break
  ip_mask = 0
  first_int = 0
  part_1 = 0
  while ip_mask < 4:
      first_int = s_mask[ip_mask]
      part_1 = s_ip[ip_mask]
      #convert IP address from integer to binary string format
      ip_par = format(part_1,'08b')
      loc = []
      result = []
      perm_len = 0
      source = bin(first_int)
      #Get a binary list
      result = copylist(source,len(source))
      #Record the location of 1 bit in the list loc[]
      perm_len = get_1_bits(result)
      ini_list = []
      dest_list = []
      A = ['0','1']
      Index = 0
      bin_dec = []
      sorted_dst = []
      trans_dec = []
      i = 0
      con_num = 0
      tem_n = 0
      fin_index = ip_mask + 1
      if perm_len > 0:
          ini_list = gen_ini_list(ini_list,perm_len)
          fun(A, ini_list, Index, perm_len)
          if dest_list != []:
             bin_dec = discover(ip_par,loc,dest_list)
             sorted_dst = compact_num(sorted(bin_dec),len(bin_dec))
             print('The matching address part', + fin_index,'is:', sorted_dst)
      else:
          print('The matching address part',+ fin_index,'is:',part_1)
      ip_mask += 1
  cont_pro = ''   
  cont_pro = input("Continue -- Y/y Exit -- Other key:")
  if(cont_pro == 'Y') or (cont_pro == 'y'):
          continue
  else:
          break
  


