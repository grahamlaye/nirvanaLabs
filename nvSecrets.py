import keyring

class Provider:
    def __init__(self, keyRingName='nvLab'):
        self.keyRingName = keyRingName
        self.apiKey = keyring.get_password(self.keyRingName, 'apiKey')
        self.nodeName = keyring.get_password(self.keyRingName, 'nodeName')
        
        if not (self.apiKey and self.nodeName):
            self.apiKey = str(input('Enter API Key: '))
            self.nodeName = str(input('Enter Node Name: '))
            keyring.set_password(self.keyRingName, 'apiKey', self.apiKey)
            keyring.set_password(self.keyRingName, 'nodeName', self.nodeName)

    def getCredentials(self):
        return {
            'apiKey': self.apiKey,
            'nodeName': self.nodeName
        }

# Example usage:
if __name__ == '__main__':
    provider_instance = Provider()
    credentials = provider_instance.getCredentials()
    print(credentials)
