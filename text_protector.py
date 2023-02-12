import pyzipper

def text_protect(filename, pwdx):
    pwd = bytes(pwdx, 'utf-8')


    with pyzipper.AESZipFile('newtest.zip',
                            'w',
                            compression=pyzipper.ZIP_LZMA,
                            encryption=pyzipper.WZ_AES) as zf:
        zf.setpassword(pwd)
        zf.writestr(filename, "Txt protected!!")

    with pyzipper.AESZipFile('newtest.zip') as zf:
        zf.setpassword(pwd)
        my_secrets = zf.read(filename)