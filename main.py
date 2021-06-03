from hashlib import sha256
from tqdm import tqdm
MAX_NONCE = 100000000

def compute_sha_256(text):
    return sha256(text.encode('ascii')).hexdigest()

def mine(block_number, transactions, previous_hash, prefix_zeros):
    final_hash = -1
    final_nonce = -1
    prefix_str = '0' * prefix_zeros
    for nonce in tqdm(range(MAX_NONCE)):
        text = str(block_number) + transactions + previous_hash + str(nonce)
        new_hash = compute_sha_256(text)
        if new_hash.startswith(prefix_str):
            final_hash = new_hash
            final_nonce = nonce
            break
    return final_hash, final_nonce

# Sample bit mining script
if __name__ == '__main__':
    transactions = '''
        Dhaval -> Bhavin -> 20
        Mando -> Cara -> 45
    '''
    difficulty = 20
    fhash, nonce = mine(5, transactions, "00001781d2d57583a5d87c985d999b9b24ce5b280cbdcbff38725f53a91132c4", difficulty)
    print(fhash, nonce)