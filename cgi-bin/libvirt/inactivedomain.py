from __future__ import print_function
import sys
import libvirt

conn = libvirt.open('qemu:///system')
if conn == None:
    print('Failed to open connection to qemu:///system', file=sys.stderr)
    exit(1)

#domainIDs = conn.listDomainsID()
'''if domainIDs == None:
    priint('Failed to get a list of domain IDs', file=sys.stderr)
'''
domainNames = conn.listDefinedDomains()

#domainIDs = conn.listDomainsID()
#if domainIDs == None:
 #   print('Failed to get a list of domain IDs', file=sys.stderr)
#if len(domainIDs) != 0:
#    for domainID in domainIDs:
#        domain = conn.lookupByID(domainID)
       # domainNames.append(domain.name)
print("Active domain IDs:")

if len(domainNames) == 0:
    print('  None')
else:
    for domainName in domainNames:
        print('  '+domainName)
conn.close()
exit(0)
