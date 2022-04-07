from dataclasses import dataclass
from parsita import *


@dataclass(frozen=True)
class LiteralPacket:
    packet: str

def join(*args):
    return ''.join(*args)

def bin_to_dec(digits):
    digitstring = ''.join(digits)
    return int(digitstring, 2)

def select_operator_type(remainder: str):
    pass


class PacketParser(TextParsers):
    digit = reg(r'[01]')

    version = digit & digit & digit > bin_to_dec
    ptype = digit & digit & digit > bin_to_dec

    literal_chunk = lit('1') & digit & digit & digit & digit > join
    literal_end = lit('0') & digit & digit & digit & digit > join
    literal = rep(literal_chunk) & literal_end

    literal_header = version & lit('100')
    operator_header = version & ptype

    literal_packet = literal_header & literal > LiteralPacket

    lengthtype_0 = reg(r'[01]{15}')
    lengthtype_1 = reg(r'[01]{11}')
    operator_packet = operator_header >= select_operator_type
    packet = (literal_packet | operator_packet) << rep(lit('0'))

tests = ["110100101111111000101000",
         # "00111000000000000110111101000101001010010001001000000000",
         # "11101110000000001101010000001100100000100011000001100000",
         ]

for test in tests:
    packet = PacketParser.packet
    result = packet.parse(test)
    pass
