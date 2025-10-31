from auth import AzureClient
from azure.mgmt.storage.models import StorageAccountCreateParameters, Sku

class StorageManager:
    def __init__(self, subscription_id):
        self.azure_client = AzureClient(subscription_id)
        self.storage_client = self.azure_client.get_storage_client()
    
    def create_storage_account(self, rg_name, storage_name, location="eastus"):
        """Create a storage account"""
        print(f"Creating storage account: {storage_name}")
        
        storage_params = StorageAccountCreateParameters(
            sku=Sku(name="Standard_LRS"),
            kind="StorageV2",
            location=location,
            tags={"Environment": "Development"}
        )
        
        storage_operation = self.storage_client.storage_accounts.begin_create(
            rg_name,
            storage_name,
            storage_params
        )
        
        storage_account = storage_operation.result()
        print(f"Storage account {storage_account.name} created successfully")
        return storage_account
    
    def list_storage_accounts(self, rg_name):
        """List storage accounts in a resource group"""
        print(f"Storage accounts in {rg_name}:")
        for account in self.storage_client.storage_accounts.list_by_resource_group(rg_name):
            print(f"  - {account.name}")
