
import json
from auth import *


api_version = "2017-12-01"
resource_group = "test1234"
location = "westus2"


print(generate_headers())


def start_vms(vms=[]):
    request_headers = generate_headers()
    for vm_name in vms:
        print("starting: ", vm_name)
        url = "https://management.azure.com/subscriptions/%s/resourceGroups/%s/providers/Microsoft.Compute/virtualMachines/%s/start?api-version=%s" % (subscription, resource_group, vm_name, api_version)
        r = requests.post(url, headers=request_headers)
        print(r)


def get_vms():
    request_headers = generate_headers()
    url = "https://management.azure.com/subscriptions/%s/resourceGroups/%s/providers/Microsoft.Compute/virtualMachines?api-version=%s" % (subscription, resource_group, api_version)
    r = requests.get(url, headers=request_headers)
    r = json.loads(r.content)['value']
    vms = {}
    for vm in range(len(r)):
        name = r[vm]['name']
        network_url = 'https://management.azure.com' + r[vm]['properties']['networkProfile']['networkInterfaces'][0]['id'] + '/ipConfigurations?api-version=2018-04-01'
        ip = requests.get(network_url, headers=request_headers)
        network_url = json.loads(ip.content)
        vms[name] = network_url['value'][0]['properties']['privateIPAddress']
    return vms


def get_vm_ips():
    request_headers = generate_headers()
    url = "https://management.azure.com/subscriptions/%s/resourceGroups/%s/providers/Microsoft.Compute/virtualMachines?api-version=%s" % (subscription, resource_group, api_version)
    r = requests.get(url, headers=request_headers)
    r = json.loads(r.content)['value']
    all_vms = []
    for vm in range(len(r)):
        name = r[vm]['name']
        network_url = 'https://management.azure.com' + r[vm]['properties']['networkProfile']['networkInterfaces'][0]['id'] + '/ipConfigurations?api-version=2018-04-01'
        ip = requests.get(network_url, headers=request_headers)
        network_url = json.loads(ip.content)
        ip = network_url['value'][0]['properties']['privateIPAddress']
        machine = {"vm": {"name": name, "ip": ip}}
        all_vms.append(machine)
    return all_vms


def list_operations():
    request_headers = generate_headers()
    url = "https://management.azure.com/providers/Microsoft.Network/operations?api-version=" + api_version
    r = requests.get(url, headers=request_headers)
    x = json.loads(r.content.decode("utf-8"))
    return json.dumps(x, indent=4)


#print(list_operations())


def list_availsets1(x):
    request_headers = generate_headers()
    url = "https://management.azure.com/subscriptions/%s/resourceGroups/%s/providers/Microsoft.Compute/availabilitySets?api-version=%s" % (subscription, x, api_version)
    r = requests.get(url, headers=request_headers)
    x = json.loads(r.content.decode("utf-8"))
    return json.dumps(x, indent=4)


# print(list_availsets1(resource_group))


def create_resourcegroups():
    request_headers = generate_headers()
    url = "https://management.azure.com/subscriptions/%s/resourcegroups/%s?api-version=%s" % (subscription, resource_group, api_version)
    payload = '{"id":"/%s/resourceGroups/%s","name":"%s","location":"%s"}' % (subscription, resource_group, resource_group, location)
    r = requests.put(url, headers=request_headers, data=payload)
    return r.content


def del_resourcegroups():
    request_headers = generate_headers()
    url = "https://management.azure.com/subscriptions/%s/resourcegroups/%s?api-version=%s" % (subscription, resource_group, api_version)
    r = requests.delete(url, headers=request_headers)
    x = "I was expecting a 202, however I received: '" + str(r) + "' from the API"
    if r.status_code == 202:
        x = "Resource Group '" + resource_group + "' will be deleted"
    return x


print(create_resourcegroups())

#print(del_resourcegroups())

def test(x):
    jsonData = '{"firstName": "Stephen", "lastName": "Burke", "age": 46}'
    jsonToPython = json.loads(jsonData)
    return jsonToPython[x]


#print(test('lastName'))


# print(list_availsets2())

