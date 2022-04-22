# Import the needed credential and management objects from the libraries. 
from    azure.identity      import AzureCliCredential
from    azure.mgmt.resource import ResourceManagementClient
import  os
import  json

# Acquire a credential object using CLI-based authentication.
credential = AzureCliCredential()

# Retrieve subscription ID from environment variable.
subscription_id = os.environ["AZURE_SUBSCRIPTION_ID"]

# Obtain the management object for resources.
resource_client = ResourceManagementClient(credential, subscription_id)

# list all the resource groups in the variable mentioned below
group_list = resource_client.resource_groups.list()

# Retrieve the list of resource groups
rgname      = []
rglocation  = []

# Generating an array of metatadata
for group in list(group_list):
    rgname.append(group.name)
    rglocation.append(group.location)

# Dumping the array within a dictonary variable
map_of_rg ={
    "rgname"        : test-RG,
    "rglocation"    : EastUS
}

# Open a json file and write the dictoanry to a json file
with open('result.json', 'w') as fp:
    json.dump(map_of_rg, fp)