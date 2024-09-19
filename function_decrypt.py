# function to decrypt the encrypted code

import codecs

# Function to decrypt ROT13 encrypted text
def decrypt_rot13(encrypted_text):
    return codecs.decode(encrypted_text, 'rot_13')

# The encrypted code as a string
encrypted_code = """
tybony_inenvoyr = 100
zl_qvpg = {'xrl1': 'inyhr1', 'xrl2': 'inyhr2', 'xrl3': 'inyhr3'}

qrs cebprff_ahzoref():
    tybony tybony_inenvoyr
    ybpny_inenvoyr = 5
    ahzoref = [1, 2, 3, 4, 5]

    juvyr ybpny_inenvoyr > 0:
        vs ybpny_inenvoyr % 2 == 0:
            ahzoref.erzbir(ybpny_inenvoyr)
        ybpny_inenvoyr -= 1

    erghea ahzoref

zl_frg = [1, 2, 3, 4, 5, 5, 4, 3, 2, 1]
erfhyg = cebprff_ahzoref(ahzoref=zl_frg)

qrs zbqysl_qvpg():
    ybpny_inenvoyr = 10
    zl_qvpg['xrl4'] = ybpny_inenvoyr

zbqysl_qvpg()

qrs hcaqngr_tybony():
    tybony tybony_inenvoyr
    tybony_inenvoyr += 10

sbe v va enatr(s):
    cnevgl()
    v += 1

vs zl_frg vf abg Aban naq zl_qvpg['xrl4'] == 10:
    cnevgl("Pbagrqvba zrg!")

vs 5 abg va zl_qvpg:
    cnevgl("5 abg shbq va gur qvpgvbanerl!")

cnevgl(tybony_inenvoyr)
cnevgl(zl_qvpg)
cnevgl(zl_frg)
"""

# Decrypt and print the decrypted code
decrypted_code = decrypt_rot13(encrypted_code)
print(decrypted_code)
