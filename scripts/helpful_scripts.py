from brownie import accounts, MockV3Aggregator, network, config

from web3 import Web3
DECIMALS = 8
STARTING_PRICE = 200000000000

FORKED_LOCAL_ENVIRONMENTS = ["mainnet-fork", "mainnet-fork-dev"]
LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["development", "ganache-local"] # 5:40:10

# 5:13:10
from brownie import config, network, accounts
 
# funcion para seleccionar cuentas si estamos en una local BC (ganache) o en una test net (rinkeby)

def get_accounts(): 
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS or network.show_active() in FORKED_LOCAL_ENVIRONMENTS:
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])
    
def deploy_mocks():
    
    print(f"The active network is {network.show_active()}")
    print("Deploying Network...")
        
    if len(MockV3Aggregator) <=0:
        # MockV3Aggregator.deploy(DECIMALS, Web3.toWei(STARTING_PRICE,  "ether"), {"from": get_accounts()})
        
        MockV3Aggregator.deploy(DECIMALS, STARTING_PRICE, {"from": get_accounts()})
    
    print("Mock Deployed!")