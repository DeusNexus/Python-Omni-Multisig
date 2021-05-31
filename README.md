# Python-Omni-Multisig

Create a 3-of-5 multisig address to test the code or edit to code to suit your n-of-k requirement.

# Requirements

Omnicore client (probably needs to be fully synchronized, but for signing you can use a non-synced omnicore)

# Instructions

Rename `constants.example.py` to `constants.py` and fill out your details which will be used by the scripts.

Then run python `main.py`, this will create the transaction using createRawTransaction function and return an unsigned raw hex that needs to be signed by the private keys of the multisig address that wants to move (omnilayer) funds.

The `main.py` script will also use the private keys provided in the `constants.py` file to emulate the signing process. Once the n-of-k keys is reached the object will return 'complete' status indicating required amount of keys have signed and transaction is now ready to be broadcasted.

By default `ENABLE_BROADCAST` is set to `False` and no real transaction will be broadcasted, if you want to test it out check if everything is correct before proceeding, it will then broadcast the multisig transaction to the bitcoin network!