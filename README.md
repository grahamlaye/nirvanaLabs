# Nirvana Labs Avalanche C-Chain Demo

This repository leverages the Nirvana Cloud node services to produce a collection of API calls to a provisioned Avalanche node.


## Pre-Reqs

- You have read and understood the Qredo API Security Best Practices document [here](https://developers.qredo.com/developer-guides/qredo-api/security-best-practices).
- You have a Nirvana Labs account. Open [here](https://nirvanalabs.io/).
- You have entered a payment method [here](https://nirvanalabs.io/cloud).
- You have successfully provisioned an Avalanche Mainnet node [here](https://nirvanalabs.io/dashboard/nodes).
- You have the node name and your API key available.

## Installation and Usage

- Clone the Repo
```bash
git clone https://github.com/grahamlaye/nirvanaLabs.git
```
- Change directory to repo
```bash
cd nirvanaLabs
```

- OPTIONAL: Create python3 virtual environment
```bash
python3 -m venv nirvanaLabs
```

- OPTIONAL: Activate the new venv
```bash
source nirvanaLabs/bin/activate
```

- Install dependencies from requirements.txt
```bash
pip3 install -r requirements.txt
```

- Run the nvLabs.py script. Upon initial launch this script will secure your apiKey and nodeName in your local hosts keyring manager.
```bash
python3 nvLabs.py
```

- You should see an output similar to the following:
```bash
Client ID: 140669013631376 | net_version: {'jsonrpc': '2.0', 'id': 1, 'result': '43114'}
Client ID: 140669013631376 | eth_blockNumber: {'jsonrpc': '2.0', 'id': 1, 'result': '0x2755403'}
Client ID: 140669013631376 | eth_gasPrice: {'jsonrpc': '2.0', 'id': 1, 'result': '0x5d21dba00'}
Client ID: 140669013631376 | eth_maxPriorityFeePerGas: {'jsonrpc': '2.0', 'id': 1, 'result': '0x0'}
Client ID: 140669013631376 | eth_getUncleCountByBlockNumber: {'jsonrpc': '2.0', 'id': 1, 'result': '0x0'}
```
- Observe the client ID used should be the same for each instantiation of the class. This is due to running async calls to the API, resulting in non-blocking execution.

- Re-running the script should not prompt you again for your API Key and Node name. These are now secured on your local Keyring manager.
