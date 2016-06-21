def to_bases(n):
    if n < 2 ** 4:
        template = '{0:2d} 0x{0:X} 0o{0:03o} 0b{0:04b}'
    elif n < 2 ** 8:
        template = '{0:3d} 0x{0:02X} 0o{0:03o} 0b{0:08b}'
    elif n < 2 ** 16:
        template = '{0:5d} 0x{0:04X} 0o{0:06o} 0b{0:016b}'
    elif n < 2 ** 32:
        template = '{0:10d} 0x{0:08X} 0o{0:012o} 0b{0:032b}'
    elif n < 2 ** 64:
        template = '{0:20d} 0x{0:016X} 0o{0:024o} 0b{0:064b}'
    else:
        template = '{0:d} 0x{0:X} 0o{0:o} 0b{0:b}'
    return template.format(n)