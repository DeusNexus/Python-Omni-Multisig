from utils import omni_createpayload_simplesend, omni_createrawtx_input, omni_createrawtx_opreturn, omni_createrawtx_reference, omni_createrawtx_change
from constants import OMNILAYER_ID, OMNIASSET_VALUE_TO_SEND

def createRawTransaction(funding_tx, funding_vout, funding_value, script_pub_key, from_address, to_address, fee):
    payload = omni_createpayload_simplesend(OMNILAYER_ID,OMNIASSET_VALUE_TO_SEND)
    # print('Payload:', payload)

    rawtx_input = omni_createrawtx_input('',funding_tx, funding_vout)
    # print('Input:', rawtx_input)

    rawtx_opreturn = omni_createrawtx_opreturn(rawtx_input, payload)
    # print('OPRETURN:', rawtx_opreturn)

    rawtx_reference = omni_createrawtx_reference(rawtx_opreturn, to_address)
    # print('REFERENCE:', rawtx_reference)

    #This uses a single input, if you need multiple then modify the script
    rawtx_change = omni_createrawtx_change(rawtx_reference, [
        {
            "txid": funding_tx,
            "vout": funding_vout,
            "scriptPubKey": script_pub_key,
            "value": funding_value
        }
    ], from_address, fee)
    
    # print('CHANGE:',rawtx_change)
    return rawtx_change