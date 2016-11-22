from uuid import getnode as get_my_mac_address

mac_add = get_my_mac_address()

mac_address = ':'.join(("%012X" % mac_add)[i:i+2] for i in range(0, 12, 2))
