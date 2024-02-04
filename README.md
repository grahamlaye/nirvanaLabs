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
cd <<repo dir>>
```

- OPTIONAL: Create python3 virtual environment
```bash
python3 -m venv qredoApiSDK
```

- OPTIONAL: Activate the new venv
```bash
source qredoApiSDK/bin/activate
```

- Install dependencies from requirements.txt
```bash
pip3 install -r requirements.txt
```

- Test with your apiKey, apiSecret & workspaceID ** IMPORTANT: Please do not hard code your credentials for production usage [Best Practices](https://developers.qredo.com/developer-guides/qredo-api/security-best-practices). **
```bash
vi getToken.py
```
```bash
# Edit apiKey, apiSecret and workspaceID values for your environment.
def main():
    apiKey = 'yourApiKeyGoesHere'
    apiSecret = 'yourApiSecretGoesHere'
    workspaceID = 'yourWorkspaceIDGoesHere'
```

- Run the getToken.py script. This should print a token that can be used to authenticate your API calls to the Qredo Network.
```bash
python3 getToken.py
```

-  Once successful restore the getToken.py file to its original state. Now, use the example.py file to perform two GET REST API calls to the Qredo network. The script is preconfigured to retrieve workspace attributes and list existing API keys via asynchronous requests. ** IMPORTANT: Please do not hard code your credentials for production usage [Best Practices](https://developers.qredo.com/developer-guides/qredo-api/security-best-practices). **
```bash
vi example.py
```
```bash

# Change apiKey, apiSecret and workspaceID to your own environment arguments below.
async def main():
    apiKey = 'apiKeyGoesHere'
    apiSecret = 'apiSecretGoesHere'
    workspaceID = 'workspaceIDGoesHere'
```

- Run the example.py script. This will pretty print the afforementioned GET responses.
```bash
python3 example.py
```

- Observe that you can make simple additions to the example.py script to initiate API calls with and without a JSON body.

Example 1: No JSON body

```bash
    async def newApiCallNoJson(self):
        return await self.skeletonRequest \
            (url=f'endpoint/example', method='GET')
```

Example 2: With a JSON body

```bash
    async def newApiCallWithJson(self):
        return await self.skeletonRequest \
            (url=f'endpoint/example', method='POST', body=pathToJson)
```

### You can now make API calls to the Qredo network with the correct x-token authentication headers.
