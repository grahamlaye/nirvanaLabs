import httpx, asyncio
import nvSecrets
from pprint import pprint as pp

class NirvanaLabs:
    def __init__(self):
        self.client = httpx.AsyncClient()
        mySecrets = nvSecrets.Provider().getCredentials()
        self.apiKey, self.nodeName = mySecrets['apiKey'], mySecrets['nodeName']
        self.url = f'https://avax.nirvanalabs.xyz/{self.nodeName}/ext/bc/C/rpc?apikey={self.apiKey}'
        self.headers = {
            'accept': 'application/json', 'content-type': 'application/json'
        }
        self.payload = {
            'jsonrpc': '2.0', 'method': None, 'params': None, 'id': 1
        }

    async def requestTemplate(self, httpMethod, paramMethod, params=None):
        self.payload['method'] = paramMethod
        if params:
            self.payload['params'] = params
        try:
            response = await self.client.request(
            httpMethod,
            url=self.url,
            headers=self.headers,
            json=self.payload,
            timeout=10
            )
            response.raise_for_status()
            return paramMethod, response.json()
        except httpx.HTTPError as e:
            print(f'There was an HTTP error in the API response: {e}')
            return None

    async def getNetVersion(self):
        return await self.requestTemplate(httpMethod='POST', paramMethod='net_version')
    
    async def getBlockNumber(self):
        return await self.requestTemplate(httpMethod='POST', paramMethod='eth_blockNumber')
    
    async def getLatestBlockTxNumber(self):
        return await self.requestTemplate(httpMethod='POST', paramMethod='eth_getBlockTransactionCountByNumber', params=['latest'])
    
    async def gasPrice(self):
        return await self.requestTemplate(httpMethod='POST', paramMethod='eth_gasPrice')
    
    async def maxPriorityPerGas(self):
        return await self.requestTemplate(httpMethod='POST', paramMethod='eth_maxPriorityFeePerGas')
    
    async def getUncles(self):
        return await self.requestTemplate(httpMethod='POST', paramMethod='eth_getUncleCountByBlockNumber', params=['latest'])
    
    async def runAll(self):
        coroutines = [
            self.getNetVersion(),
            self.getBlockNumber(),
            #self.getLatestBlockTxNumber(),
            self.gasPrice(),
            self.maxPriorityPerGas(),
            self.getUncles()
            ]
        results = await asyncio.gather(*coroutines)
        for param_method, response in results:
            print(f'Client ID: {id(self.client)} | {param_method} | {response}')
        return results
    
if __name__ == '__main__':
    asyncio.run(NirvanaLabs().runAll())
