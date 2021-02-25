# for 8 digit encryption only
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
# b_codes = ['07418305','07773523','13305743', '14799376', '20037957', '23576469', '31852309', '82876331', '85075022', '92690835']
# enc_codes = encrypt_codes(b_codes)
# print(enc_codes) || Output: ['0475461989310454', '0179727434582334', '1731380353754635', '1141719698337363', '2703073973985171', '2431587463486196', '3611885323320191', '8223817961353214', '8756027658062129', '9422659704873158']
# decrypt_code('0874471489370958') || Output: '07418305'
# batch_decrypt(enc_codes) || Output: ['07418305','07773523','13305743', '14799376', '20037957', '23576469', '31852309', '82876331', '85075022', '92690835']