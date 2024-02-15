import httpx, asyncio, time
import nvSecrets
from pprint import pprint as pp
from rich import print
from rich.progress import Progress

class NirvanaLabs:
    def __init__(self):
        self.client = httpx.AsyncClient()
        mySecrets = nvSecrets.Provider().getCredentials()
        self.apiKey, self.nodeName = mySecrets['apiKey'], mySecrets['nodeName']
        #self.url = f'https://avax.nirvanalabs.xyz/{self.nodeName}/ext/bc/C/rpc?apikey={self.apiKey}'
        #self.url = f'https://mantle-sepolia.nirvanalabs.xyz/{self.nodeName}?apikey={self.apiKey}'
        self.url = str(input('enter full URL here: '))
        self.headers = {
            'accept': 'application/json',
            'content-type': 'application/json'
        }
        self.payload = {
            'jsonrpc': '2.0',
            'method': None,
            'params': None,
            'id': 1
        }

    async def requestTemplate(self, httpMethod, paramMethod=None, params=None, progress=None):
        self.payload['method'] = paramMethod
        if params:
            self.payload['params'] = params
        else:
            self.payload['params'] = []
        try:
            task = progress.add_task(f"[cyan]{paramMethod} in progress...", total=1)
            response = await self.client.request(
                httpMethod,
                url=self.url,
                headers=self.headers,
                json=self.payload,
                timeout=10
            )
            response.raise_for_status()
            progress.update(task, completed=1)
            return paramMethod, response.json()
        except httpx.HTTPError as e:
            print(f'There was an HTTP error in the API response: {e}')
            return None

    async def getNetVersion(self, progress):
        return await self.requestTemplate(httpMethod='POST', paramMethod='net_version', progress=progress)

    async def getBlockNumber(self, progress):
        return await self.requestTemplate(httpMethod='POST', paramMethod='eth_blockNumber', progress=progress)
    
    async def getLatestBlockTxNumber(self, progress):
        return await self.requestTemplate \
            (httpMethod='POST', paramMethod='eth_getBlockTransactionCountByNumber', params=['latest'], progress=progress)
    
    async def gasPrice(self, progress):
        return await self.requestTemplate(httpMethod='POST', paramMethod='eth_gasPrice', progress=progress)
    
    async def maxPriorityPerGas(self, progress):
        return await self.requestTemplate(httpMethod='POST', paramMethod='eth_maxPriorityFeePerGas', progress=progress)
    
    async def getUncles(self, progress):
        return await self.requestTemplate \
            (httpMethod='POST', paramMethod='eth_getUncleCountByBlockNumber', params=['latest'], progress=progress)
    
    async def ethSync(self, progress):
        return await self.requestTemplate(httpMethod='POST', paramMethod='eth_syncing', progress=progress)
    
    async def netListening(self, progress):
        return await self.requestTemplate(httpMethod='POST', paramMethod='net_listening', progress=progress)
    
    async def netPeerCount(self, progress):
        return await self.requestTemplate(httpMethod='POST', paramMethod='net_peerCount', progress=progress)
    
    async def ethEstimateGas(self, progress):
        params = [
            {"from": "0x9cE564c7d09f88E7d8233Cdd3A4d7AC42aBFf3aC","to": "0xd46e8dd67c5d32be8058bb8eb970870f07244567","value": "0x9184e72a"}
            ]
        return await self.requestTemplate(httpMethod='POST', paramMethod='eth_estimateGas', params=params)
    
    async def runAll(self):
        with Progress() as progress:
            coroutines = [
                self.getNetVersion(progress),
                self.getBlockNumber(progress),
                self.getLatestBlockTxNumber(progress),
                self.gasPrice(progress),
                self.maxPriorityPerGas(progress),
                self.getUncles(progress),
                self.ethSync(progress),
                self.netListening(progress),
                self.netPeerCount(progress),
                #self.ethEstimateGas(progress)
            ]
            results = await asyncio.gather(*coroutines)
            for param_method, response in results:
                print(f'Client ID: {id(self.client)} | {param_method}: {response}')
            return results

if __name__ == '__main__':
    asyncio.run(NirvanaLabs().runAll())
