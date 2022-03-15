# 5:47:28
from asyncio import exceptions
import pytest
from scripts.helpful_scripts import get_accounts, LOCAL_BLOCKCHAIN_ENVIRONMENTS
from brownie import accounts, network, exceptions
from scripts.deploy import deploy_fund_me

def test_can_fund_and_withdraw():
    account = get_accounts()
    fund_me = deploy_fund_me()
    entrance_fee = fund_me.getEntranceFee() + 100
    tx = fund_me.fund({"from": account, "value": entrance_fee})
    tx.wait(1)
    
    # check that our address and the amount that we founded is adequately recorded
    assert fund_me.addressToAmountFunded(account.address) == entrance_fee

    tx2 = fund_me.withdraw({"from": account})
    tx.wait(1)

    # check that our withdraw function is working
    assert fund_me.addressToAmountFunded(account.address) == 0 

# brownie test


# when we only want to run test on a local chain just to check functionality we use pytest skip functionality to do so

# This test make sure that only the owner of the contract can withdraw NO BODY ELSE 5:51:00
def test_only_owner_can_withdraw():
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip("only for local testing")
    fund_me = deploy_fund_me()
    bad_actor =  accounts.add()    
    
    # this line is tell our test, that if: this revert with this virtual machine error, THATS GOOD!, because nobody exept the owner of the contract can withdraw the money!
    with pytest.raises(exceptions.VirtualMachineError):
          fund_me.withdraw({"from": bad_actor})      




# brownie test -k test_only_owner_can_withdraw
# brownie test -k test_only_owner_can_withdraw --network rinkeby

# WHEN YOURE RUNNIG A TEST AN HAVE AN ERROR, FIND THIS LINE IN THE TERMINAL --> "tests\test_fund_me.py:xx" --> this line will give you a hint of the line in the code that is wrong


# brownie networks add development mainnet-fork-dev cmd=ganache-cli host=http://127.0.0.1 fork=https://eth-mainnet.alchemyapi.io/v2/OLmwpyXbE0fCe4bgIGFokVlxjdQ5RIpR accounts=10 mnemonic=brownie port=7545


