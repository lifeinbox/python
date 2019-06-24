#not end!

from pysnmp.hlapi import *

result = getCmd(SnmpEngine(),
            CommunityData(community_name, mpModel=0),
            UdpTransportTarget((str("10.31.1.1"), 161)),
            ContextData(),
            ObjectType(ObjectIdentity(...)))

result2 = nextCmd(..., lexicographicMode=False)

snmp_object = ObjectIdentity('SNMP-v2-MIB', 'sysDescr', 0)
snmp_object = ObjectIdentity('1.3.6.1.2.1.2.2.1.2')