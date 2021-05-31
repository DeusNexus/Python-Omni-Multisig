from createrawtx import createRawTransaction
from sign import signRawTransaction
from utils import sendrawtransaction
from constants import FUNDING_TX, FUNDING_VOUT, FUNDING_VALUE, REDEEM_SCRIPT, SCRIPT_PUB_KEY, FROM_ADDRESS, TO_ADDRESS, FEE, PK1, PK2, PK3, PK4, PK5
import time

# ONLY SET TO 'True' IF YOU ARE WILLING TO BROADCAST A REAL TRANSACTION!
ENABLE_BROADCAST = False

unsigned_raw_tx_hex = createRawTransaction(FUNDING_TX, FUNDING_VOUT, FUNDING_VALUE, SCRIPT_PUB_KEY, FROM_ADDRESS, TO_ADDRESS, FEE)
print('\nunsigned_raw_tx_hex:', unsigned_raw_tx_hex)

def checkComplete(data):
    if(data['complete']):
        print('\n### COMPLETED ### - Ready to broadcast!')
        time.sleep(5)
        
        t = 10
        while(t > 0):
            print(f'\n[!] Broadcasting transaction in {t} seconds!')
            time.sleep(1)
            t-=1
        
        txid = 'TEST_NO_REAL_BROADCAST'

        if ENABLE_BROADCAST:
            txid = sendrawtransaction(data['hex'])

        return txid
    else:
        print('\n### UNCOMPLETE ### - Require more signatures before broadcast!')
        return data['hex']

#BASED ON A 3-of-5 multisig address
sig1 = checkComplete(signRawTransaction(unsigned_raw_tx_hex, PK5, REDEEM_SCRIPT))
print('\nSIGNATURE1:',sig1)

sig2 = checkComplete(signRawTransaction(sig1, PK4, REDEEM_SCRIPT))
print('\nSIGNATURE2: ',sig2)

sig3 = checkComplete(signRawTransaction(sig2, PK3, REDEEM_SCRIPT))
print('\nTXID: ',sig3)