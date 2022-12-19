import time
Web3
import random

def check_balance(address, number, web3):
    try:
        balance = web3.eth.get_balance(web3.to
        h            params = {
                "network": network
            }
        )
        cprint(f">>> Успешно | {address
    except Exception as error:
        cprint(f">>> Неудачно | {address} | ошибк
if __name__ == "__main__":
    with open("wallets.txt", "r") as f
    netwo
