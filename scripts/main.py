import argparse
from resource_manager import ResourceManager
from storage_manager import StorageManager
import os

SUBSCRIPTION_ID = os.getenv("AZURE_SUBSCRIPTION_ID", "YOUR_SUBSCRIPTION_ID")

def main():
    parser = argparse.ArgumentParser(description="Azure Infrastructure Automation Tool")
    parser.add_argument("--action", choices=["create", "list", "delete"], required=True)
    parser.add_argument("--resource", choices=["rg", "storage"], required=True)
    parser.add_argument("--name", help="Resource name")
    parser.add_argument("--location", default="eastus", help="Azure region")
    
    args = parser.parse_args()
    
    if args.resource == "rg":
        rm = ResourceManager(SUBSCRIPTION_ID)
        
        if args.action == "create":
            rm.create_resource_group(args.name, args.location)
        elif args.action == "list":
            rm.list_resource_groups()
        elif args.action == "delete":
            rm.delete_resource_group(args.name)
    
    elif args.resource == "storage":
        sm = StorageManager(SUBSCRIPTION_ID)
        
        if args.action == "create":
            # Storage needs a resource group name
            rg_name = input("Enter resource group name: ")
            sm.create_storage_account(rg_name, args.name, args.location)
        elif args.action == "list":
            rg_name = input("Enter resource group name: ")
            sm.list_storage_accounts(rg_name)

if __name__ == "__main__":
    main()
