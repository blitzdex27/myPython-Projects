# 8-digit code simple encryptor
# Date created: Feb 26, 2021, 2 hours
# use encrypt_codes(code_list) method to encrypt a list of 8 digit codes
# use decrypt_code(encrypted_code) method to decrypt the code
# use batch_decrypt(encrypted_codes) method to batch decrypt
import csv
import random
def encrypt_codes(code_list):
    """
    for 8 digit backup codes only
    """
    enc_codes = []
    
    for codes in b_codes:
        ec = ''
        for digit in codes:
            ec += digit

            ec += (lambda snum: chr(snum))(random.randint(49, 57))

        enc_codes.append(ec)
    
    with open('encrpyted_codes.csv', 'w', encoding = 'utf-8') as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow('Encrypted codes')
        csv_writer.writerow(enc_codes)
    
    
    
    return enc_codes

def decrypt_code(encrypted_code):
    """
    Decrypts the code
    """
    decrypted_code = ''
    for i, c in enumerate(encrypted_code):
        if i % 2 == 0:
            decrypted_code += c
        else:
            pass

    return decrypted_code

def batch_decrypt(encrypted_codes):
    """
    Decrypts a batch of codes
    """
    decrypted_codes = []
    for code in encrypted_codes:
        
        decrypted_code = ''
        for i, c in enumerate(code):
            if i % 2 == 0:
                decrypted_code += c
            else:
                pass
            
        decrypted_codes.append(decrypted_code)
    
    return decrypted_codes

# sample
b_codes = ['07410475','07770475','13300475', '14790475', '20030475', '23570475', '31850475', '82870475', '85070475', '92690475']
enc_codes = encrypt_codes(b_codes)
print(enc_codes) #|| Output: ['0877451703417759', '0672757103447553', '1831360108477958', '1442749209487559', '2704043809477251', '2139557101437554', '3316865503477154', '8927897209497657', '8752057904467452', '9828679409487956']
decrypt_code('0874471489370958') #|| Output: '07410475'
decrypted_codes = batch_decrypt(enc_codes) #|| Output: ['07410475', '07770475', '13300475', '14790475', '20030475', '23570475', '31850475', '82870475', '85070475', '92690475']
print(decrypted_codes)