from web3 import Web3

infura_url = "https://mainnet.infura.io/v3/16e2559e46ba4b85b66742b5377104ed"

web3 = Web3(Web3.HTTPProvider(infura_url))

# status of connection
print(web3.isConnected())

# Get block number info
print(web3.eth.blockNumber)

# balance = web3.getBalace("")