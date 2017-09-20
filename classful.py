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


def subnet_a(dept_name,no_of_host,network_id_string):
    bits,mask_val,mask_inti=0,[],'255.'
    while(no_of_host>pow(2,bits)):
        bits+=1
#calculating subnet_mask
    mask_val.extend(one[0:(24-bits)])
    mask_val.extend(zero[0:bits])
    last_mask_val=sum(int(mask_val) * (2 ** i) for i, mask_val in enumerate(mask_val[(len(mask_val)-1):15:-1]))
    second_last_mask_val=sum(int(mask_val) * (2 ** i) for i, mask_val in enumerate(mask_val[15:7:-1]))# These three lines calculate value z,y,x in '255.x.y.z' for class A
    third_last_mask_val=sum(int(mask_val) * (2 ** i) for i, mask_val in enumerate(mask_val[7::-1]))
    mask=mask_inti+str(third_last_mask_val)+'.'+str(second_last_mask_val)+'.'+str(last_mask_val)
    bits=0
#calculating network_id
    network_id=network_id_string.split('.')
    third_end_of_id=int((2**bits+sum(class_a))/65536)
    network_id.append(str(third_end_of_id))
    sec_end_of_id=int((2**bits+sum(class_a)-third_end_of_id*65536)/255)
    network_id.append(str(sec_end_of_id))
    end_of_id=2**bits+sum(class_a)-third_end_of_id*65536-sec_end_of_id*255
    while(end_of_id>pow(2,bits)):
        bits+=1
    end_of_id=2**bits
    network_id.append(str(end_of_id))
    class_a.append(end_of_id+(255*sec_end_of_id)+(65536*third_end_of_id))
    printable_network_id=network_id[0]+'.'+network_id[1]+'.'+network_id[2]+'.'+network_id[3]

#printitng calculated values
    print('\t   ',dept_name,'\t      ',mask,'\t',printable_network_id,'\n')

def main():
    network_id_string=input('Enter the network id\n')                                         # Gets the network id as a string
    depts=[int(i) for i in input('Enter number of hosts in each department seperated with space\n').split()] # Get number of hosts in each department

    alphabets=list(string.ascii_uppercase)                                                    # List of uppercase Alphabets 
    dept_map=dict(zip(alphabets[0:len(depts)],depts))                                         # Dictionary of department name and number of host in them

    network_id=network_id_string.split('.')                                                   # Converts the entered network id into a list seperated by '.'
    print('\tDEPARTMENT\tSUBNET MASK\t SUBNET ID')   

    if(int(network_id[0])>=1 and int(network_id[0])<=127):
        for key,value in dept_map.items():                                                    #passing department name and number of host in that department to calculate subnet_id and mask
            subnet_a(key,value,network_id_string)
        print('This network id follows Class A addressing')

    elif(int(network_id[0])>=128 and int(network_id[0])<=191):                                # All if conditions to check with class of network
        for key,value in dept_map.items():
            subnet_b(key,value,network_id_string)
        print('This network id follows Class B addressing')

    elif(int(network_id[0])>=192 and int(network_id[0])<=223):
        for key,value in dept_map.items():
            subnet_c(key,value, network_id_string)
        print('This network id follows Class C addressing')
main()
