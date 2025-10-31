from auth import AzureClient
import sys

class ResourceManager:
    def __init__(self, subscription_id):
        self.azure_client = AzureClient(subscription_id)
        self.resource_client = self.azure_client.get_resource_client()
    
    def create_resource_group(self, rg_name, location="eastus"):
        """Create a resource group"""
        print(f"Creating resource group: {rg_name}")
        rg_result = self.resource_client.resource_groups.create_or_update(
            rg_name,
            {"location": location, "tags": {"Environment": "Development"}}
        )
        print(f"Resource group {rg_result.name} created successfully")
        return rg_result
    
    def list_resource_groups(self):
        """List all resource groups"""
        print("Listing all resource groups:")
        for rg in self.resource_client.resource_groups.list():
            print(f"  - {rg.name} ({rg.location})")
    
    def delete_resource_group(self, rg_name):
        """Delete a resource group"""
        print(f"Deleting resource group: {rg_name}")
        delete_operation = self.resource_client.resource_groups.begin_delete(rg_name)
        print("Delete operation initiated. Waiting for completion...")
        delete_operation.wait()
        print(f"Resource group {rg_name} deleted successfully")

if __name__ == "__main__":
    # Get subscription ID
    SUBSCRIPTION_ID = "YOUR_SUBSCRIPTION_ID"  # Replace with your subscription ID
    
    rm = ResourceManager(SUBSCRIPTION_ID)
    
    # Example usage
    rm.create_resource_group("automated-rg-demo", "eastus")
    rm.list_resource_groups()
