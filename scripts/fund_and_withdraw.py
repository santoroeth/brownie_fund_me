from brownie import FundMe
from scripts.helpful_scripts import get_accounts

#5:42:40

def fund():
    fund_me = FundMe[-1]
    account = get_accounts()
    entrance_fee = fund_me.getEntranceFee()
    
    print(entrance_fee)
    print(f"current entry fee is {entrance_fee}")
    print("funding...")
 
    fund_me.fund({"from": account, "value": entrance_fee})


def withdraw():
    fund_me = FundMe[-1]
    account = get_accounts()
    fund_me.withdraw({"from": account})

    
def main():
    fund()
    withdraw()


#! Se corre en la terminal asi para la test net: "brownie run scripts/fund_and_withdraw.py --network [nombre]" 