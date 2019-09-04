def gcd(e1, phi1):
    while True:
        temp=e1%phi1
        if temp==0:
            return phi1
        else:
            e1 = phi1
            phi1 = temp

def encodeMsg(msg):
    encoded_msg_list = []
    for i in msg:
        encoded_msg_list.append(str(ord(i)))
    return encoded_msg_list

def decodeMsg(encoded_decrypted_list):
    decoded_msg_list = []
    for i in range(len(encoded_decrypted_list)):
        temp_char = chr((int)(encoded_decrypted_list[i]))
        decoded_msg_list.append(temp_char)
    return decoded_msg_list

def rsaEncrypt(encoded_list, e, n):
    encrypted_list = []
    for i in range(len(encoded_list)):
        char_encrypt_int = (int)((pow((int)(encoded_list[i]), e))%n)
        char_encrypt_str = (str)(char_encrypt_int)
        encrypted_list.append(char_encrypt_str)
    return encrypted_list

def rsaDecrypt(encrypted_list, d ,n):
    decrypted_list = []
    for i in range(len(encrypted_msg_list)):
        char_decrypt_int = (int)((pow((int)(encrypted_msg_list[i]), d))%n)
        char_decrypt_str = (str)(char_decrypt_int)
        decrypted_list.append(char_decrypt_str)
    return decrypted_list


p = 13
q = 17
n = p * q
phi = (p-1) * (q-1)
e = 2
while e < phi:
    if(gcd(e, phi)==1):
        break
    else:
        e = e+1

k=2
#private key
d = (int)((k*phi + 1)/e)

msg = input("Enter our msg : ")

encoded_msg_list = encodeMsg(msg)

encoded_msg_str = ""
encoded_msg_str = encoded_msg_str.join(encoded_msg_list)
print("Encoded msg list  = ", encoded_msg_list)
print("Length = ", len(encoded_msg_list))
print("Encoded msg str  = ", encoded_msg_str)


encrypted_msg_list = rsaEncrypt(encoded_msg_list, e, n)

encrypted_msg_str = ""
encrypted_msg_str = encrypted_msg_str.join(encrypted_msg_list)
print("Encrypted msg list = ", encrypted_msg_list)
print("Length = ", len(encrypted_msg_list))
print("Encrypted msg str = ", encrypted_msg_str)


decrypted_msg_list = rsaDecrypt(encrypted_msg_list, d, n)

decrypted_msg_str = ""
decrypted_msg_str = decrypted_msg_str.join(decrypted_msg_list)
print("Decrypted msg list : ", decrypted_msg_list)
print("Length = ", len(decrypted_msg_list))
print("Decrypted msg str : ", decrypted_msg_str)


decoded_msg_list = decodeMsg(decrypted_msg_list)
print("Length = ", len(decoded_msg_list))
decoded_msg_str = ""
decoded_msg_str = decoded_msg_str.join(decoded_msg_list)

print("Original msg list = ", decoded_msg_list)
print("Original msg str = ", decoded_msg_str)
