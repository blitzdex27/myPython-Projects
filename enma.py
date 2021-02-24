import json
import random
import datetime as dt
import os
""" 
Date created: February 19, 2021

This is a file encryption project I designed myself.
This is a very simple encryption.
Use encrypt(filename, favorite_num) method to encrypt.
Use decrypt(encrypted_file) method to decrypt.
Each method will create a separate file.

"""

def encrypt(filename, favorite_num = 8):

    fullfilename = filename
    splitfilename = filename.split('.')
    filename = splitfilename[0]
    file_ext = splitfilename[1]

    byteread = favorite_num
    # Generates a random key
    key = key_gen()
    try:    
        with open('crypt.json', 'r') as f:
            reader = json.load(f)

            # Change key until the code is unique
            while key in reader.keys() == True:
                key = key_gen()

            # Store the JSON content
            fcryptinfo = reader

    # Handles error if there is crypt.json is not existing or has no content
    except Exception:
        fcryptinfo = {}

    # Run this code whatever happens
    finally:   
        # Convert the generated key into byte and store
        bytekey = key.encode('utf-8')

        # Reads the binary content of the file
        with open(fullfilename, 'rb') as f:

            # Store the binary content into reader variable and limit into 'byteread' bytes
            reader = f.read(byteread)

            # define empty list of unencrypted binary content
            unenc_list = []

            # Store the binary content per specified 'byteread' bytes until no more bytes left
            while reader != b'':

                # Add the read binary content per sepecified bytes into the unenc_list
                unenc_list.append(reader)
                # Read again the the binary content per specified bytes to move the pointer location
                reader = f.read(byteread)
                # Store the length of the last binary content for decoding purposes
                lastbytegroup = len(unenc_list[-1])

            # Define an empty list for reversed unencrypted list
            rev_list = []
            # Get and store the length of the unencrypted list
            y = len(unenc_list)

            # Reverse the unencrypted list. This will be a 1-layer encryption.
            for items in unenc_list:
                # Add the content of unenc_list to the rev_list starting from the end
                rev_list.append(unenc_list[y-1])
                # Decrements the value of y to reverse the list
                y -= 1

                # If the list has reached the 1st binary content of the unencrypted list, break the loop
                if y == 0:
                    break

            # Insert the bytekey at the 0 index
            rev_list.insert(0, bytekey)

        # Define an empty binary object
        unenc = b''
        # Concatenate the binary contents of the list
        for items in rev_list:
            unenc = unenc + items

        # Write the concatenated binary contents into a file
        enc_output_file = filename + '_enc.' + file_ext
        with open(enc_output_file, 'wb') as unenc_file:
            unenc_file.write(unenc)

        # Update the encryptment info file for decoding
        with open('crypt.json', 'w') as f:
            # save
            fcryptinfo.update({key: {'filename' : filename, 'file_ext' : file_ext, 'lastbytegroup' : lastbytegroup, 'byteread' : byteread, 'date_encrypted' : str(dt.date.today())}})
            json.dump(fcryptinfo, f, ensure_ascii = False, sort_keys = True, indent = 2)

        # Making sure the key is stored
        with open('crypt.json') as f:
            cryptdata = json.load(f)
            is_key_stored = key in cryptdata.keys()

        # Let the user know that

        if is_key_stored == True:
            print('Encrypting done!')
            print(key)
        else:
            print('There is some kind of error')


def key_gen():
    char_end = range(49,91)
    char_list = []

    for i in char_end:
        char_list.append(chr(i))

    char_end2 = range(94, 123)

    char_list2 = []
    for i in char_end2:
        char_list.append(chr(i))

    key = ''
    for i in range(1,20):
        key += random.choice(char_list)

    return key


def decrypt( encrypted_file):
    # cryptedfilekey = cryptedfilekey
    encrypted_file = encrypted_file
    # Read the embedded encryptment key for decoding
    with open(encrypted_file, 'rb') as f:
        dkey = f.read(19)
        dkey = dkey.decode('utf-8')

    # Extract the true file name from crypt.json
    # Extract the lastbytegroup and byteread, which are the key parts on decoding process
    with open('crypt.json') as f:
        cryptinfo = json.load(f)
        dfilename = cryptinfo[dkey]['filename']
        dfile_ext = cryptinfo[dkey]['file_ext']
        lastbytegroup = cryptinfo[dkey]['lastbytegroup']
        dbyteread = cryptinfo[dkey]['byteread']

    with open(encrypted_file, 'rb') as cf:
        # Move the pointer after the encryption key
        cf.read(19)

        # Initializes the first byte group content into the list
        bytegroup = cf.read(lastbytegroup)
        undec_list = [bytegroup]

        # Re-read the binary content, but this time using byteread
        bytegroup = cf.read(dbyteread)

        # Add the remaining binary content into the undecrypted list
        while bytegroup != b'':
            undec_list.append(bytegroup)
            bytegroup = cf.read(dbyteread)

        # Define the decrypted list
        dec_list = []
        # Get the length of the undecrypted list
        y = len(undec_list)

        # Reverses the undecrypted list to pass the 1st layer of encryption
        for items in undec_list:
            # Start from the last content of the undecrypted list
            dec_list.append(undec_list[y-1])
            # Decrement's y to proceed reversely
            y -= 1

            # if y = 0, break the loop
            if y == 0:
                break

        # Define decrypted file variable        
        dec_file = b''

        # Concatenate the decrypted list contents
        for items in dec_list:
            dec_file = dec_file + items

    # Write the decrypted content into a file
    output_file = dfilename + '_decrypted' + '.' + dfile_ext
    with open(output_file, 'wb') as df:
        df.write(dec_file)

    bytelength = len(dec_file)
    print('Done decrypting')


def decrypt_all(self):
    dir_list = os.listdir('.')
    #print(dir_list)

    # list all files in folder and subfolder
    files_in_current_folder = []
    for path, subdirs, files in os.walk('.'):
        for name in files:
             files_in_current_folder.append(name)

    #print(files_in_current_folder)

    # import encryption keys
    with open('crypt.json') as f:
        cryptdata = json.load(f)

    #print(cryptdata)
    # list all decryptable files
    # Initialize decryptable list of files
    decriptable_files = []
    #print(cryptdata.keys())
    for filee in files_in_current_folder:
        try:
            with open(filee, 'rb') as f:
                dbkey = f.read(19)
                dkey = dbkey.decode('utf-8')

                if dkey in cryptdata.keys():
                    decriptable_files.append(filee)

        except Exception:
            continue

    x = 0
    for file in decriptable_files:
        decrypt(file)
        x += 1

    print(f"Done! {x} file(s) decrypted.")



