import base64
import gzip
import warnings
import os
warnings.filterwarnings("ignore", category=DeprecationWarning) 

save = open(f"{os.path.expandvars(r'%LOCALAPPDATA%/GeometryDash')}/CCGameManager.dat", "r").read()

def xor(string: str, key: int) -> str:
    return ("").join(chr(ord(char) ^ key) for char in string)

def decrypt_data(data: str) -> str:
    base64_decoded = base64.urlsafe_b64decode(xor(data, key=11).encode())
    decompressed = gzip.decompress(base64_decoded)
    return decompressed

def getAccountManager():
    decrypted_data = decrypt_data(save).decode(encoding='unicode_escape', errors='ignore')
    accountManager = {}
    accountManager["accountID"] = decrypted_data.split("GJA_003</k><i>")[1].split("</i>")[0]
    accountManager["gjp2"] = decrypted_data.split("GJA_005</k><s>")[1].split("</s>")[0]
    accountManager["userName"] = decrypted_data.split("GJA_001</k><s>")[1].split("</s>")[0]
    return accountManager

# Example: Using the getAccountManager() function.
print(getAccountManager())