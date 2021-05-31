import subprocess
import json

def rpc(cmd):
    PREFIX = "omnicore-cli"
    command = f"{PREFIX} {cmd}"
    
    res = subprocess.run(command, shell = True, capture_output=True)
    
    print('\n',res.args)
    # if(res.stderr): return { "error": json.dumps(res.stderr) }
    if res.stderr: print('ERROR:',res.stderr)
    return (res.stdout).decode('utf-8').strip()

def gettransaction(id):
    return rpc(f'gettransaction "{id}"')

def getreceivedbyaddress(address):
    return rpc(f'getreceivedbyaddress "{address}"')

def validateaddress(address):
    return rpc(f'validateaddress "{address}"')

def getunconfirmedbalance():
    return rpc(f'getunconfirmedbalance')

def omni_getbalance(address, property_id):
    return rpc(f'omni_getbalance {address} {property_id}')

def omni_getwalletaddressbalances(include_watchonly):
    return rpc(f'omni_getwalletaddressbalances {include_watchonly}')

def omni_listtransactions(address, count=100, skip=0, startblock=0, endblock=0):
    return rpc(f'omni_listtransactions {address}')

def omni_createpayload_simplesend(propertyid, amount):
    return rpc(f'omni_createpayload_simplesend {propertyid} "{amount}"')

def omni_createrawtx_input(raw_hex, txid_funding, vout_funding):
    return rpc(f'omni_createrawtx_input "{raw_hex}" "{txid_funding}" {vout_funding}')

def omni_createrawtx_opreturn(raw_hex, omni_payload):
    return rpc(f'omni_createrawtx_opreturn "{raw_hex}" "{omni_payload}" ')

def omni_createrawtx_reference(raw_hex, to_address):
    return rpc(f'omni_createrawtx_reference "{raw_hex}" "{to_address}"')

def omni_createrawtx_change(raw_hex, input_array, change_address, miner_fee):
    return rpc(f'omni_createrawtx_change "{raw_hex}" \'{json.dumps(input_array)}\' "{change_address}" {miner_fee}')

def omni_decodetransaction(raw_hex):
    return rpc(f'omni_decodetransaction "{raw_hex}"')

def decoderawtransaction(raw_hex):
    return rpc(f'decoderawtransaction "{raw_hex}"')

def signrawtransactionwithkey(raw_hex, pk_array, txid, vout, script_pub_key, redeem_script):
    obj = [{
        "txid": txid,
        "vout": vout,
        "scriptPubKey":script_pub_key,
        "redeemScript":redeem_script
    }]
    return rpc(f'signrawtransactionwithkey \'{raw_hex}\' \'{pk_array}\' \'{json.dumps(obj)}\'')

def sendrawtransaction(signed_hex, max_fee=0.001):
    return rpc(f'sendrawtransaction "{signed_hex}" {max_fee}')
