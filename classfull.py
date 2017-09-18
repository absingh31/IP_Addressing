import string
zero,one,class_b,class_a,mask_list,end_of_id=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],[],[],[],0

def subnet_c(dept_name, no_of_host,network_id_string):
    global end_of_id
    bits,mask_val,mask_inti,end=0,[],'255.255.255.',['0']
    while(no_of_host>pow(2,bits)):
        bits+=1                                                                               # To calculate number of bits assigned for host

    network_id=network_id_string.split('.')
    network_id.append(str(end_of_id))
    printable_network_id=network_id[0]+'.'+network_id[1]+'.'+network_id[2]+'.'+network_id[3]
    end_of_id=2**bits
# calculating subnet_mask
    mask_val.extend(one[0:(8-bits)])
    mask_val.extend(zero[0:bits])                                                             
    last_mask_val=sum(int(mask_val) * (2 ** i) for i, mask_val in enumerate(mask_val[::-1]))  # calculate value of x in '255.255.255.x'
    mask=mask_inti+str(last_mask_val)                                                         
    mask_list.append(mask)                                                                    # List of subnet mask printed till this statement's execution
# printing subnet_mask and network_id calculated
    print('\t   ',dept_name,'\t      ',mask,'\t',printable_network_id,'\n') 

def subnet_b(dept_name,no_of_host,network_id_string):
    b,bits,mask_val,mask_inti=0,0,[],'255.255.'
    while(no_of_host>pow(2,bits)):
        bits+=1
    mask_val.extend(one[0:(16-bits)])
    mask_val.extend(zero[0:bits])
    bits=0
# Calculating the network_id
    network_id=network_id_string.split('.')
    end_of_id=2**bits+sum(class_b)
    sec_end_of_id=int(end_of_id/255)
    network_id.append(str(sec_end_of_id))
    end_of_id=end_of_id-sec_end_of_id*255
    while(end_of_id>pow(2,bits)):   # end_of_id recalculated here after
        bits+=1
    end_of_id=2**bits
    network_id.append(str(end_of_id))
    class_b.append(end_of_id+(255*sec_end_of_id))
    printable_network_id=network_id[0]+'.'+network_id[1]+'.'+network_id[2]+'.'+network_id[3]
#calculating subnet_mask 
    last_mask_val=sum(int(mask_val) * (2 ** i) for i, mask_val in enumerate(mask_val[(len(mask_val)-1):7:-1]))
    second_last_mask_val=sum(int(mask_val) * (2 ** i) for i, mask_val in enumerate(mask_val[7::-1])) # These two lines calculate value z,y in '255.255.y.z' for class B
    mask=mask_inti+str(second_last_mask_val)+'.'+str(last_mask_val)
#printing subnet_mask and network_id calculated
    print('\t   ',dept_name,'\t      ',mask,'\t',printable_network_id,'\n')

