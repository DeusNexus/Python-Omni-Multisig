import json
from utils import decoderawtransaction, signrawtransactionwithkey

def signRawTransaction(unsigned_raw_tx_hex, private_keys, redeem_script):
    print('\n\nSIGNING.....!')

    decode_raw_tx = json.loads(decoderawtransaction(unsigned_raw_tx_hex))
    # print(decode_raw_tx)

    txid = decode_raw_tx['txid']
    vout = decode_raw_tx['vin'][0]['vout']
    script_pub_key = decode_raw_tx['vout'][0]['scriptPubKey']['hex']

    uncomplete_raw_tx = signrawtransactionwithkey(unsigned_raw_tx_hex, private_keys, txid, vout, script_pub_key, redeem_script)
    
    if(json.loads(uncomplete_raw_tx)['complete']): 
        print('\n[READY] COMPLETELY_SIGNED_RAW_TX_HEX: ', json.loads(uncomplete_raw_tx))
    else:
        print("\n[UNCOMPlETE] UNCOMPLETE_RAW_TX_HEX: ",json.loads(uncomplete_raw_tx))
    
    return json.loads(uncomplete_raw_tx)