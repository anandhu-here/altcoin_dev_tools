from get_pri_key import *
import argparse
import hashlib
from utils import *


  #  	except TypeError:
		# if(isHex(value)):
		# 	return hashlib.sha256(bytes.fromhex(value)).digest()
  #       else:
  #       	return hashlib.sha256(value.encode('utf-8')).digest()
  #   except:
  #   	raise

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Perform the SHA256 function on input string. Can be hex or ascii.')
    parser.add_argument('value', metavar='value')
    args = parser.parse_args()

    result = sha256_(args.value)
    print(result.hex())

