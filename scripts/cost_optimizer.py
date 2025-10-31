from auth import AzureClient

class CostOptimizer:
    def __init__(self, subscription_id):
        self.azure_client = AzureClient(subscription_id)
        self.resource_client = self.azure_client.get_resource_client()
    
    def find_unused_resources(self):
        """Identify potentially unused resources"""
        print("Scanning for unused resources...")
        unused = []
        
        # List all resource groups
        for rg in self.resource_client.resource_groups.list():
            resources = list(self.resource_client.resources.list_by_resource_group(rg.name))
            
            if len(resources) == 0:
                unused.append({
                    "type": "Empty Resource Group",
                    "name": rg.name,
                    "recommendation": "Consider deleting if not needed"
                })
        
        return unused
    
    def generate_cost_report(self):
        """Generate cost optimization recommendations"""
        print("\n=== Cost Optimization Report ===")
        unused = self.find_unused_resources()
        
        if unused:
            print(f"\nFound {len(unused)} optimization opportunities:")
            for item in unused:
                print(f"  - {item['type']}: {item['name']}")
                print(f"    Recommendation: {item['recommendation']}")
        else:
            print("No obvious optimization opportunities found.")
