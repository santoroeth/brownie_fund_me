#--> (5:12:22) Inicio de este script

from brownie import FundMe, MockV3Aggregator, network, config
from eth_account import Account
from scripts.helpful_scripts import deploy_mocks, get_accounts, LOCAL_BLOCKCHAIN_ENVIRONMENTS



def deploy_fund_me():
    # 1. Necesitamos una cuenta 5:12:28
    account = get_accounts()
    
    # 2. Llamr el contrato creando un objeto
    # if we are on a persistent network like rinkeby, use the associates address
    # otherwise, deply mocks!

    # Funcion para seleccionar una cuenta que nos de el feed del precio del ether from "AggregatorV3Interface"
    if network.show_active() not in  LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        price_feed_address = config["networks"][network.show_active()]["eth_usd_price_feed_address"]
    
    # 5:27:36 
    else: 
        deploy_mocks()
        price_feed_address = MockV3Aggregator[-1].address
        


    fund_me=FundMe.deploy(price_feed_address,{"from":account}, publish_source=config["networks"][network.show_active()].get("verify")) 
    
    print(f"contract deployed to {fund_me.address}")
    
     
    # for the test (with this the test can have owr fundMe contract --> 5:48:14)
    return fund_me

    
    #! Se corre en la terminal asi para la test net: "brownie run scripts/deploy.py --network [nombre]"

    #! Se corre en la terminal asi para local chain(ganache) [UI o CLI]: "brownie run scripts/deploy.py"

    #! Para ver las networks disponibles en brownie: "brownie networks list"

    #! Para agregar una nueva networks  en brownie: "brownie+ networks+ add+ [Ethereum] o [Development]+ nombre que le quieras dar+ host=[http address]+ chainid=[networkid] "


def main():

    deploy_fund_me()
