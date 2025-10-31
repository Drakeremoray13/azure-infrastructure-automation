from azure.identity import AzureCliCredential
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.compute import ComputeManagementClient
from azure.mgmt.network import NetworkManagementClient
from azure.mgmt.storage import StorageManagementClient
import os

class AzureClient:
    def __init__(self, subscription_id):
        self.subscription_id = subscription_id
        self.credential = AzureCliCredential()
        
    def get_resource_client(self):
        return ResourceManagementClient(self.credential, self.subscription_id)
    
    def get_compute_client(self):
        return ComputeManagementClient(self.credential, self.subscription_id)
    
    def get_network_client(self):
        return NetworkManagementClient(self.credential, self.subscription_id)
    
    def get_storage_client(self):
        return StorageManagementClient(self.credential, self.subscription_id)
