from xml.dom.minidom import parseString
import sys
 
def main():
    target = sys.argv[0]
    number = int(sys.argv[-1])
     
    xml = open(target, 'r').read()
    doc = parseString(xml)
    for host in doc.getElementsByTagName('host'):
        ip = host.getAttribute('ip')
        parts = ip.split('.')
        parts[-1] = str(int(parts[-1]) + number)
        host.setAttribute('ip', '.'.join(parts))
         
        mac = host.getAttribute('mac')
        parts = mac.split(':')
        parts[-1] = str(int(parts[-1]) + number)
        host.setAttribute('mac', ':'.join(parts))
     
    f = open(target, 'w')
    f.write(doc.toxml())
    f.close()
 
if __name__ == '__main__':
    main()
