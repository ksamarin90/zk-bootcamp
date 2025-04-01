from ecpy.curves import Curve
from ecpy.keys import ECPublicKey, ECPrivateKey
from sha3 import keccak_256
import secrets

# generated via ethers.Wallet.createRandom()
private_key = 0x66417992200062b8d493d5258506b2216975f7d2420b16c15bb6cadd4d8f7dc5

curve = Curve.get_curve('secp256k1')

# we use generator (point) of secp256k1 curve and multiply it by private key (scalar) to get a public key point
public_key_point = private_key * curve.generator

# compressed hex encoded public key has 33 bytes
# if y coordinate is even we prefix x with 0x02, otherwise with 0x03
prefix = b'\x02' if public_key_point.y % 2 == 0 else b'\x03'
public_key_compressed_bytes = prefix + public_key_point.x.to_bytes(32, byteorder='big')
public_key = '0x' + public_key_compressed_bytes.hex()

print("Public key: " + public_key)

# to calculate ethereum address we need to hash with keccak256 the sum of x and y coordinates (uncompressed 64 bytes)
# of public key point and take 20 less significant bytes
public_key_bytes = public_key_point.x.to_bytes(32, byteorder='big') + public_key_point.y.to_bytes(32, byteorder='big')
address = '0x' + keccak_256(public_key_bytes).digest()[-20:].hex()

print("Eth address: " + address)

# this is the message private key will sign
message = 'Rareskills zk course rocks'

# we generate h by hashing the message
# h = keccak_256(message.encode())
h = int.from_bytes(keccak_256(message.encode()).digest(), byteorder='big')


# then we pick random scalar k
k = secrets.randbits(256)

# and compute R = k * G
R = k * curve.generator
# from which we only take x value
r = R.x

print(r)

# we compute s
s = (h + r * private_key) * pow(k, -1, curve.order) % curve.order

print(s)

# and send to verifier (public_key, r, s, h)

# verifier computes R'
R_check = (h * curve.generator + r * public_key_point) * pow(s, -1, curve.order)

# and verifies that x value matches r
assert(r == R_check.x)