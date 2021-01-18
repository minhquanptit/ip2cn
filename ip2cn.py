import ipaddress
import csv

#Network = input("Nhap mang can tra: ")
  
with open('result.csv', 'w', newline='') as file:
    fieldnames = ['IP', 'CN', 'Count']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    with open ('ip.csv', newline = '') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            IP = (row['src'])
            count = (row['_count'])
            with open ('db.csv','r',newline = '') as csvfile:
                reader1 = csv.DictReader(csvfile)
                for row in reader1:
                    Network = row['data']
                    if ipaddress.ip_address(IP) in ipaddress.ip_network(Network):
                        writer.writerow({'IP': IP, 'CN':row['cn'], 'Count': count})
