import json

from web3 import HTTPProvider, Web3

w3 = Web3(HTTPProvider("http://127.0.0.1:8545"))

ONE_DAY = 24 * 60 * 60
ONE_YEAR = 365 * ONE_DAY


_json = {}


def load_json(filename: str):
    if filename in _json:
        return _json[filename]

    with open(filename) as f:
        _json[filename] = json.load(f)

    return _json[filename]


def connect_contract(path: str, address: str):
    # load the json data at the json file
    with open("../state/addresses/localhost.json") as f:
        addresses = json.load(f)

    # read the contract data in build/ and create contract objects
    Contract = json.loads(open(path).read())
    return w3.eth.contract(address=address, abi=Contract["abi"])


def connect_all():
    # read addresses from the json file
    with open("../state/addresses/localhost.json") as f:
        addresses = json.load(f)

    # read the contract data in build/ and create contract objects
    return {
        "cash": connect_contract("../artifacts/Cash.sol/Cash.json", addresses["cash"]),
        "treasury": connect_contract(
            "../artifacts/Treasury.sol/Treasury.json", addresses["treasury"]
        ),
        "canvas1": connect_contract(
            "../artifacts/Canvas1.sol/Canvas1.json", addresses["canvas1"]
        ),
    }
