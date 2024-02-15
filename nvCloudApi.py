import nvSecrets
import httpx, asyncio

class NvCloudApi:
    def __init__(self):
        self.apiKey = nvSecrets.cloudApiKey
        self.client = httpx.AsyncClient()
        self.baseurl = 'https://api.nirvanacloud.xyz/api'
        self.headers = {
            'accept': 'application/json',
            'content-type': 'application/json',
            'Authorization': f'Bearer {self.apiKey}'
            }
        
    async def requestTemplate(self, service, httpMethod, payload=None):
        apiurl = f'{self.baseurl}/{service}'
        try:
            if payload:
                response = await self.client.request(
                httpMethod,
                url=apiurl,
                headers=self.headers,
                json=payload,
                timeout=15
                )
                print(response.status_code)
            else:
                response = await self.client.request(
                httpMethod,
                url=apiurl,
                headers=self.headers,
                timeout=15
                )
            response.raise_for_status()
            return response.json()
        except httpx.HTTPStatusError as e:
            print(f'There was an HTTP error in the API response: {e}')
            return None
        
    async def getVpcs(self):
        return await self.requestTemplate(httpMethod='GET', service='vpcs?region=london')
    
    async def getVpcDetails(self, vpcID):
        return await self.requestTemplate(httpMethod='GET', service=f'vpcs/{vpcID}')
    
    async def createVpc(self, regionName, vpcName, subnetName):
        payload = {
            'region': regionName,
            'name': vpcName,
            'subnet_name': subnetName
        }
        response = await self.client.request(
            'POST',
            url=f'{self.baseurl}/vpcs',
            headers=self.headers,
            json=payload
        )
        print(response)

    async def viewAllVms(self, regionName):
        return await self.requestTemplate(httpMethod='GET', service=f'vms?region={regionName}')


if __name__ == '__main__':
    from pprint import pprint as pp
    #pp(asyncio.run(NvCloudApi().getVpcs()))
    #pp(asyncio.run(NvCloudApi().getVpcDetails(vpcID=195)))
    pp(asyncio.run(NvCloudApi().viewAllVms(regionName='london')))