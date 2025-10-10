def bin2dec(binary:str)->int:
    n=len(binary)-1
    power=2**n
    decimal=0
    for i in range(n,-1,-1):
        decimal+=int(binary[n-i])*power
        power//=2
    return decimal

def dec2bin2(decimal:int)->str:
    if decimal==0:
        return '0'
    binary=''
    while decimal>0:
        r=decimal%2
        binary=str(r)+binary
        decimal//=2
    return binary

def dec2bin(decimal:int)->str:
    potega=128
    bin=''
    while decimal>0:
        bin+=str(decimal//potega)
        decimal%=potega
        potega//=2
    return bin

def u22decimal(binary:str)->int:
    n=len(binary)
    if binary[0]=='0':
        return int(binary,2)
    else:
        inverted=''
        for i in range(n):
            if binary[i]=='0':
                inverted+='1'
            else:
                inverted+='0'

        abs_value=int(inverted,2)+1

        return -abs_value

def dec2other(decimal:int,base:int)->str:
    if decimal==0:
        return '0'
    other=''
    digits=['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    while decimal>0:
        r=decimal%base
        other=digits[r]+other
        decimal//=base
    return other