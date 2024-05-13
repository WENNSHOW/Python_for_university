def main(hex_string):
    data = int(hex_string, 16)

    mask_h1 = 0b11
    mask_h2 = 0b11111
    mask_h3 = 0b1111
    mask_h5 = 0b1111111111
    mask_h6 = 0b111111111111111111

    h1 = data & mask_h1
    h2 = (data >> 2) & mask_h2
    h3 = (data >> 7) & mask_h3
    h5 = (data >> 20) & mask_h5
    h6 = (data >> 30) & mask_h6

    return [('H1', h1), ('H2', h2), ('H3', h3), ('H5', h5), ('H6', h6)]


print(main('0x180c97c28c'))  # [('H1', 0), ('H2', 3), ('H3', 5), ('H5', 201), ('H6', 96)]
print(main('0x7111e90477'))  # [('H1', 3), ('H2', 29), ('H3', 8), ('H5', 286), ('H6', 452)]
print(main('0x1f9f6b8560'))  # [('H1', 0), ('H2', 24), ('H3', 10), ('H5', 502), ('H6', 126)]
print(main('0x2131a372fd'))  # [('H1', 1), ('H2', 31), ('H3', 5), ('H5', 794), ('H6', 132)]