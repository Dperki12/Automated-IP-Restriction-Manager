import_file = "allow_list.txt"
remove_list = ["192.168.97.225", "192.168.158.170", "192.168.201.40", "192.168.58.57"]

print(import_file)

print(remove_list)

import_file = "allow_list.txt"
remove_list = ["192.168.97.225", "192.168.158.170", "192.168.201.40", "192.168.58.57"]

with open(import_file, "r") as file:
import_file = "allow_list.txt"
remove_list = ["192.168.97.225", "192.168.158.170", "192.168.201.40", "192.168.58.57"]

with open(import_file, "r") as file:
  ip_addresses = file.read()

print(ip_addresses)

import_file = "allow_list.txt"
remove_list = ["192.168.97.225", "192.168.158.170", "192.168.201.40", "192.168.58.57"]

with open(import_file, "r") as file:
  ip_addresses = file.read()
ip_addresses = ip_addresses.split()

print(ip_addresses)

import_file = "allow_list.txt"
remove_list = ["192.168.97.225", "192.168.158.170", "192.168.201.40", "192.168.58.57"]

with open(import_file, "r") as file:
  ip_addresses = file.read()
ip_addresses = ip_addresses.split()

for element in ip_addresses:

    print(element)

import_file = "allow_list.txt"
remove_list = ["192.168.97.225", "192.168.158.170", "192.168.201.40", "192.168.58.57"]

with open(import_file, "r") as file:
  ip_addresses = file.read()
ip_addresses = ip_addresses.split()

#Remove process

for element in ip_addresses:
    if element in remove_list:
        ip_addresses.remove(element) 

print(ip_addresses)


import_file = "allow_list.txt"
remove_list = ["192.168.97.225", "192.168.158.170", "192.168.201.40", "192.168.58.57"]

with open(import_file, "r") as file:
  ip_addresses = file.read()
ip_addresses = ip_addresses.split()

for element in ip_addresses: 
    if element in remove_list:
        ip_addresses.remove(element)

ip_addresses = " ".join(ip_addresses)    


with open(import_file, "w") as file:
  file.write(ip_addresses)


import_file = "allow_list.txt"
remove_list = ["192.168.97.225", "192.168.158.170", "192.168.201.40", "192.168.58.57"]

with open(import_file, "r") as file:
  ip_addresses = file.read()
ip_addresses = ip_addresses.split()

for element in ip_addresses: 
    if element in remove_list:
        ip_addresses.remove(element)
ip_addresses = " ".join(ip_addresses)       

with open(import_file, "w") as file:
  file.write(ip_addresses)

with open(import_file, "r") as file:
    text = file.read()

print(text)


def update_file(import_file, remove_list):

    with open(import_file, "r") as file:
        ip_addresses = file.read()
    ip_addresses = ip_addresses.split()

    for element in ip_addresses:
        if element in remove_list:
            ip_addresses.remove(element)

    ip_addresses = " ".join(ip_addresses)       


    with open(import_file, "w") as file:
        file.write(ip_addresses)


def update_file(import_file, remove_list):

  with open(import_file, "r") as file:
      ip_addresses = file.read()
  ip_addresses = ip_addresses.split()

  for element in ip_addresses:
    if element in remove_list:
      ip_addresses.remove(element)
  ip_addresses = " ".join(ip_addresses)       

  with open(import_file, "w") as file:
    file.write(ip_addresses)

update_file(import_file, ["192.168.25.60", "192.168.140.81", "192.168.203.198"])

with open("allow_list.txt", "r") as file:
  text = file.read()

print(text)


