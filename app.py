import json
from web3 import Web3

infura_url = "https://mainnet.infura.io/v3/16e2559e46ba4b85b66742b5377104ed"
web3 = Web3(Web3.HTTPProvider(infura_url))

# status of connection
# print(web3.isConnected())

# Get block number info
# print(web3.eth.blockNumber)

abi = json.loads('[]')
address = '0xfdde0a92bfef2d95695d32400a0a8f55e530dc67'

# contract = web3.eth.contract(address=address, abi=abi).call()

# total_supply = web3.functions.totalSupply().call()

# print(web3.fromWei(total_supply, 'ether'))
# print(web3.functions.name().call())
# print(web3.functions.symbol().call())
# print(contract.functions.balanceOf('0xfdde0a92bfef2d95695d32400a0a8f55e530dc67').call())
