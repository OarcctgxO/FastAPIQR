from os import cpu_count


host = '0.0.0.0'
port = 8000

#----------UDP SETTINGS----------
udp_wait_time = 2
broadcast_addr = ('255.255.255.255', port)
udp_request = b"Who's QRcode server?"
udp_response = b"I am the QRcode server."
udp_kill = b"QRcode servers must shutdown."
#--------------------------------

#----------QR SETTINGS----------
correction_levels = { #clear level's name instead of Q, L, etc...
    'minimum': 1,
    'medium': 0,
    'high': 3,
    'maximum': 2
}
correction = correction_levels['minimum']
picture_resolution_ratio = 10 #default=10
border_size = 0 #in qr's pixels, not png pixels

cache_size = 50 #amount of pictures, not bytes
#--------------------------------

workers = cpu_count()