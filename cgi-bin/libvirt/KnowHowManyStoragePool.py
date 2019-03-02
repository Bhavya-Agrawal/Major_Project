from __future__ import print_function
import sys
import libvirt
conn=libvirt.open()
'''
def createStoragePool(conn):        
        xmlDesc = """                             #to create our own storage
        <pool type='dir'>
          <name>guest_images_storage_pool</name>
          <uuid>8c79f996-cb2a-d24d-9822-ac7547ab2d01</uuid>
          <capacity unit='bytes'>4306780815</capacity>
          <allocation unit='bytes'>237457858</allocation>
          <available unit='bytes'>4069322956</available>
          <source>
          </source>
          <target>
            <path>/usr</path>
            <permissions>
              <mode>0755</mode>
              <owner>-1</owner>
              <group>-1</group>
            </permissions>
          </target>
        </pool>"""


        pool = conn.storagePoolDefineXML(xmlDesc, 0)

        #set storage pool autostart     
        pool.setAutostart(1)
        return pool

'''
pools = conn.listAllStoragePools(0)

for pool in pools:              

    #check if pool is active
    if pool.isActive() == 0:
        #activate pool               #know about how many storage pool
        pool.create()

    stgvols = pool.listVolumes()
    print('Storage pool: '+pool.name())
    for stgvol in stgvols :
        print('  Storage vol: '+stgvol)

