import libvirt

conn=libvirt.open("qemu:///system")
 
for id in conn.listDomainsID():
   dom = conn.lookupByID(id)
   infos = dom.info()
   print 'ID = %d' % id
   print 'Name =  %s' % dom.name()
   print 'State = %d' % infos[0]
   print 'Max Memory = %d' % infos[1]
   print 'Number of virt CPUs = %d' % infos[3]
   print 'CPU Time (in ns) = %d' % infos[2]
   print ' '
#conn=libvirt.open("qemu:///system")
names = conn.listDefinedDomains()
print names
'''
clist = dir(conn)
for item in clist:
    print item
filts = conn.listNWFilters()
for item in filts:
            print item
'''
