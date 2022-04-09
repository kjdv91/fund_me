from brownie import FundMe, MockV3Aggregator, network, config
from scripts.helpfulScripts import get_account, deploy_mocks


def deployFundMe():
    account = get_account()
    if network.show_active() != "development":
        price_feed_address = config["networks"][network.show_active()][
            "eth_usd_price_feed"
        ]
    else:
        deploy_mocks()
        price_feed_address = MockV3Aggregator[-1].address

    fundMe = FundMe.deploy(
        price_feed_address,
        {"from": account},
        publish_source=config["networks"][network.show_active()].get["verify"],
    )
    print(f"Contract deployed to {fundMe.address}")


def main():
    deployFundMe()
