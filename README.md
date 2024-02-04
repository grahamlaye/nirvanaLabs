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

