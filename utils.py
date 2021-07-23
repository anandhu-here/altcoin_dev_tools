import hashlib
import codecs
import ecdsa

def isHex(value):
    try:
        int(value, 16)
        return True
    except ValueError:
        return False
    except:
        raise

def sha256_(value):
	try:
		return hashlib.sha256(value).digest()
	except TypeError:
		if(isHex(value)):
			return hashlib.sha256(bytes.fromhex(value)).digest()
		else:
			return hashlib.sha256(value.encode('utf-8')).digest()
	except:
		raise




def ToPublicKey(privKey):
    # Error Checking
    if not isHex(privKey):
        raise TypeError('Private Key argument must be valid hex')
    if len(privKey) != 64:
        raise ValueError('Private Key argument must be 32 bytes')

    privateKeyBytes = codecs.decode(privKey, 'hex')
    key = ecdsa.SigningKey.from_string(privateKeyBytes, curve=ecdsa.SECP256k1).verifying_key
    keyBytes = key.to_string()
    keyHex = codecs.encode(keyBytes, 'hex')
    return (bytearray(b'04') + keyHex).decode('utf-8')

def ToCompressedKey(pubKey):
    # Error Checking
    if not isHex(pubKey):
        raise TypeError('Public Key argument must be valid hex')
    if len(pubKey) != 130:
        raise ValueError('Public Key argument must be 65 bytes')
    
    x = pubKey[2:66]
    lastByte = x[-2:]
    lastInt = int(lastByte, 16)
    isOdd = lastInt % 2 != 0

    if isOdd:
        compressedKey = '03' + x
    else:
        compressedKey = '02' + x
    return compressedKey