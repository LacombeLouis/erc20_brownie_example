from brownie import BocconiToken
from scripts.helpful_scripts import get_account
from web3 import Web3

initial_supply = Web3.toWei(10, "ether")


def main():
    account = get_account()
    our_token = BocconiToken.deploy(initial_supply, {"from": account})
    # print(our_token.balanceOf(account))

    print(our_token.balanceOf(account))
    print(our_token.balanceOf(get_account(index=1)))

    our_token.increaseAllowance(get_account(index=1), 20)
    print(our_token.balanceOf(account))
    print(our_token.balanceOf(get_account(index=1)))

    our_token.transferFrom(get_account(index=1), account, 1)
    print(our_token.balanceOf(account))
    print(our_token.balanceOf(get_account(index=1)))
