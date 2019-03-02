#!/usr/bin/python2
from __future__ import print_function
import sys
import libvirt

filename = '/var/lib/libvirt/images/vv.qcow2'

conn = libvirt.open('qemu:///system')

if conn == None:
    print('Failed to open connection to qemu:///system', file=sys.stderr)
    exit(1)
    print id
'''
if id == conn.restore(filename) < 0:
    print('Unable to restore guest from '+filename, file=sys.stderr)
    exit(1)

dom = conn.lookupByID(id);
if dom == None:
    print('Cannot find guest that was restored', file=sys.stderr)
    exit(1)

print('Guest state restored from '+filename, file=sys.stderr)

conn.close()
exit(0)
'''
