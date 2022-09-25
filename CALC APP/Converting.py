### MY MAIN FUNCTIONS ###

def fr_bi_to_de(x):
    return(int(str(x),2))
def fr_de_to_bi(x):
    return bin(x).replace("0b","")
def fr_de_to_oc(x):
    return(oct(x)).replace("0o","")
def fr_oc_to_de(x):
    return(int(str(x),8))    
def fr_de_to_hx(x):
    return(hex(x)).replace("0x","")

print("This from binary to decimal :",fr_bi_to_de(101))
print("This from decimal to binary :",fr_de_to_bi(101))
print("This from decimal to octal :",fr_de_to_oc(101))
print("This from octal to decimal :",fr_oc_to_de(101))
print("This from decimal to hexa :",fr_de_to_hx(101)) 

##################1
def fr_bi_to_oc(x):
    x_1=fr_bi_to_de(x)
    x_2=fr_de_to_oc(x_1)
    return(x_2)
print("This from binary to octal :",fr_bi_to_oc(101))
##################2
def fr_oc_to_bi(x):
    x_1=fr_oc_to_de(x)
    x_2=fr_de_to_bi(x_1)
    return(x_2)
print("This from octal to binary :",fr_oc_to_bi(101))
##################3
def fr_bi_to_hx(x):
    x_1=fr_bi_to_de(x)
    x_2=fr_de_to_hx(x_1)
    return(x_2)    
print("This from binary to hexa :",fr_bi_to_hx(101))
##################4
def fr_oc_to_hx(x):
    x_1=fr_oc_to_de(x)
    x_2=fr_de_to_hx(x_1)
    return(x_2)
print("This from octal to hexa :",fr_oc_to_hx(101))
##################5
def fr_hx_to_bi(x):
    return(bin(int(str(x),16))).replace("0b","")
print("This from hexa to binary :",fr_hx_to_bi(101))
##################6
def fr_hx_to_de(x):
    return(int(str(x),16))
print("This from hexa to decimal :",fr_hx_to_de(101))
##################7
def fr_hx_to_oc(x):
    return(oct(int(str(x),16))).replace("0o","")
print("This from hexa to octal :",fr_hx_to_oc(101))