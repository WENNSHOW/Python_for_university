from struct import unpack_from, calcsize


class Types:
    int8 = "b"
    uint8 = "B"
    int16 = "h"
    uint16 = "H"
    int32 = "i"
    uint32 = "I"
    int64 = "q"
    uint64 = "Q"
    float = "f"


class BinaryReader:
    def __init__(self, stream, offset, order="<"):
        self.stream = stream + b" "
        self.offset = offset
        self.order = order

    def jump(self, offset):
        reader = BinaryReader(self.stream, offset, self.order)
        return reader

    def read(self, pattern):
        size = calcsize(pattern)
        data = unpack_from(self.order + pattern, self.stream, self.offset)
        self.offset += size
        return data[0]


def read_a(reader):
    a1 = reader.read(Types.int64)
    a2 = reader.read(Types.int8)
    a3 = reader.read(Types.float)
    a4_offset = reader.read(Types.uint16)
    a4_reader = reader.jump(a4_offset)
    a4 = read_b(a4_reader)
    a5_size = reader.read(Types.uint16)
    a5_offset = reader.read(Types.uint16)
    a5_reader = reader.jump(a5_offset)
    a5 = reader.stream[a5_offset:a5_offset+a5_size].decode('utf-8')
    a6_offset = reader.read(Types.uint16)
    a6_reader = reader.jump(a6_offset)
    a6 = read_d(a6_reader)
    return dict(A1=a1, A2=a2, A3=a3, A4=a4, A5=a5, A6=a6)


def read_b(reader):
    b1_size = reader.read(Types.uint16)
    b1_offset = reader.read(Types.uint32)
    b1_reader = reader.jump(b1_offset)
    b1 = [b1_reader.read(Types.int16) for _ in range(b1_size)]

    b2 = []
    for _ in range(4):
        c1 = b1_reader.read(Types.int8)
        c2 = b1_reader.read(Types.int32)
        b2.append({'C1': c1, 'C2': c2})

    return dict(B1=b1, B2=b2)



def read_d(reader):
    d1 = reader.read(Types.uint32)
    d2 = reader.read(Types.uint64)
    d3 = [reader.read(Types.uint8) for _ in range(2)]
    d4 = reader.read(Types.int16)
    d5 = reader.read(Types.int16)
    d6 = reader.read(Types.int64)
    return dict(D1=d1, D2=d2, D3=d3, D4=d4, D5=d5, D6=d6)


def main(data):
    return read_a(BinaryReader(data, 5))


# Example 1
data1 = (
    b'\xa8HYSEx\xca8\xc4lpc\xe5\x14\xb7\xa3X\xbf:\x00\x04\x00P\x00T\x00\x86`'
    b'8u\x81\xcc\xb6\x0exR\xb3\xac\xf4MA|i\x7f![\x10\x8a\x12\xf21\x10\t\xf9.\xb1'
    b'/\xa8\x06\x00\x1a\x00\x00\x00&\x00\x00\x00+\x00\x00\x000\x00\x00\x00'
    b'5\x00\x00\x00epzb\xee6:\xea\xd2:j\xd9~L\xad\x02\xbc\xb5\xf7s\xb6\xfd\x1c\x01'
    b'\x81\x97\xb6\x19\xf3\x9e'
)
result1 = parse_binary_data(data1)
print("Example 1 Result:", result1)

# Example 2
data2 = (
    b'\xa8HYSEUh\xbc\xe8\nH\xbbNg\x1e\x9f2>6\x00\x03\x00L\x00O\x00\xbd\xfb'
    b'\xea\xff\x0f\x9e\xbf\x08\x93u\xf0\xc8\x81\xff\x99`v\x0f\x04s}\xa2'
    b'\xc7\x14\x1dS\xd6\xe3\x04\x00\x1a\x00\x00\x00"\x00\x00\x00\'\x00\x00\x00'
    b',\x00\x00\x001\x00\x00\x00mwx\xda\x8f_,\xba\xb6\rO\xcd<~\xe2\xad\xe2\x93n4'
    b'\x1b\xd8\xa8\xad\xdf\xc4\x18\x1c:'
)
result2 = parse_binary_data(data2)
print("Example 2 Result:", result2)


'''
import struct


def unpack(fmt, data, offset):
    size = struct.calcsize(fmt)
    return struct.unpack(fmt, data[offset:offset+size]), offset + size


def parse_uint16(data, offset):
    return unpack('<H', data, offset)


def parse_int8(data, offset):
    return unpack('<b', data, offset)


def parse_int16(data, offset):
    return unpack('<h', data, offset)


def parse_uint32(data, offset):
    return unpack('<I', data, offset)


def parse_int32(data, offset):
    return unpack('<i', data, offset)


def parse_int64(data, offset):
    return unpack('<q', data, offset)


def parse_uint64(data, offset):
    return unpack('<Q', data, offset)


def parse_float(data, offset):
    return unpack('<f', data, offset)


def parse_char_array(data, offset, size):
    fmt = '<' + str(size) + 's'
    chars, offset = unpack(fmt, data, offset)
    return chars.decode('utf-8'), offset


def parse_uint32_array(data, offset, size):
    array = []
    for _ in range(size):
        elem, offset = parse_uint32(data, offset)
        array.append(elem)
    return array, offset


def parse_int16_array(data, offset, size):
    array = []
    for _ in range(size):
        elem, offset = parse_int16(data, offset)
        array.append(elem)
    return array, offset


def parse_uint32_int16_array(data, offset):
    size, offset = parse_uint16(data, offset)
    addr, offset = parse_uint32(data, offset)
    array, offset = parse_int16_array(data, addr, size)
    return array, offset


def parse_uint32_int32_array(data, offset, size):
    array = []
    for _ in range(size):
        addr, offset = parse_uint32(data, offset)
        elem, offset = parse_int32(data, addr)
        array.append(elem)
    return array, offset


def parse_uint64_uint8_array(data, offset):
    uint64_val, offset = parse_uint64(data, offset)
    uint8_array, offset = parse_uint32_int16_array(data, offset)
    return uint64_val, uint8_array, offset


def parse_uint32_uint64_uint8_int16_int16_int64(data, offset):
    uint32_val, offset = parse_uint32(data, offset)
    uint64_val, offset = parse_uint64(data, offset)
    uint8_array, offset = parse_char_array(data, offset, 2)
    int16_val1, offset = parse_int16(data, offset)
    int16_val2, offset = parse_int16(data, offset)
    int64_val, offset = parse_int64(data, offset)
    return uint32_val, uint64_val, uint8_array, int16_val1, int16_val2, int64_val, offset


def parse_c_structure(data, offset):
    int8_val, offset = parse_int8(data, offset)
    int32_val, offset = parse_int32(data, offset)
    return {'C1': int8_val, 'C2': int32_val}, offset


def parse_b_structure(data, offset):
    size, offset = parse_uint16(data, offset)
    addr, offset = parse_uint32(data, offset)
    int16_array, offset = parse_int16_array(data, addr, size)
    uint32_array, offset = parse_uint32_int32_array(data, offset, 4)
    return {'B1': int16_array, 'B2': uint32_array}, offset


def parse_d_structure(data, offset):
    uint32_val, uint64_val, uint8_array, int16_val1, int16_val2, int64_val, offset = \
        parse_uint32_uint64_uint8_int16_int16_int64(data, offset)
    return {'D1': uint32_val, 'D2': uint64_val, 'D3': uint8_array, 'D4': int16_val1, 'D5': int16_val2, 'D6': int64_val}, offset


def parse_a_structure(data, offset):
    int64_val, offset = parse_int64(data, offset)
    int8_val, offset = parse_int8(data, offset)
    float_val, offset = parse_float(data, offset)
    b_structure_addr, offset = parse_uint16(data, offset)
    char_array_size, char_array_addr, offset = parse_uint16_uint16(data, offset)
    d_structure_addr, offset = parse_uint16(data, offset)
    char_array, offset = parse_char_array(data, char_array_addr, char_array_size)
    b_structure, offset = parse_b_structure(data, b_structure_addr)
    d_structure, offset = parse_d_structure(data, d_structure_addr)
    return {'A1': int64_val, 'A2': int8_val, 'A3': float_val, 'A4': b_structure, 'A5': char_array, 'A6': d_structure}, offset


def parse_uint16_uint16(data, offset):
    uint16_val1, offset = parse_uint16(data, offset)
    uint16_val2, offset = parse_uint16(data, offset)
    return uint16_val1, uint16_val2, offset


def main(data):
    offset = 5  # Starting offset after the signature
    return parse_a_structure(data, offset)


example_data_1 = (
    b'\xa8HYSEx\xca8\xc4lpc\xe5\x14\xb7\xa3X\xbf:\x00\x04\x00P\x00T\x00\x86`'
    b'8u\x81\xcc\xb6\x0exR\xb3\xac\xf4MA|i\x7f![\x10\x8a\x12\xf21\x10\t\xf9.\xb1'
    b'/\xa8\x06\x00\x1a\x00\x00\x00&\x00\x00\x00+\x00\x00\x000\x00\x00\x00'
    b'5\x00\x00\x00epzb\xee6:\xea\xd2:j\xd9~L\xad\x02\xbc\xb5\xf7s\xb6\xfd\x1c\x01'
    b'\x81\x97\xb6\x19\xf3\x9e'
)
example_data_2 = (
    b'\xa8HYSEUh\xbc\xe8\nH\xbbNg\x1e\x9f2>6\x00\x03\x00L\x00O\x00\xbd\xfb'
    b'\xea\xff\x0f\x9e\xbf\x08\x93u\xf0\xc8\x81\xff\x99`v\x0f\x04s}\xa2'
    b'\xc7\x14\x1dS\xd6\xe3\x04\x00\x1a\x00\x00\x00"\x00\x00\x00\'\x00\x00\x00'
    b',\x00\x00\x001\x00\x00\x00mwx\xda\x8f_,\xba\xb6\rO\xcd<~\xe2\xad\xe2\x93n4'
    b'\x1b\xd8\xa8\xad\xdf\xc4\x18\x1c:'
)

result_1 = main(example_data_1)
result_2 = main(example_data_2)

print("Результат разбора примера 1:", result_1)
print("Результат разбора примера 2:", result_2)
'''