def create_account():
    from eth_account import Account
    account = Account.create()
    return account

new_account = create_account()
print(f"New account address: {new_account.address}")