L = 32
N = 624
M = 397
UM = 2**31
LM = UM - 1

def unBitshiftRightXor(value, shift, mask):
        i = 0
        result = 0
        shiftmask = 2**shift - 1
        while (i * shift) < L:
                partmask = (shiftmask << (L - shift)) >> (shift * i)
                part = value & partmask
                value ^= (part >> shift) & mask
                result |= part
                i += 1
        return result

def BitshiftRightXor(value, shift, mask):
        pmask = (value >> shift) & mask
        result = value ^ pmask
        return result

def unBitshiftLeftXor(value, shift, mask):
        i = 0
        result = 0
        shiftmask = 2**shift - 1
        while (i * shift) < L:
                partmask = shiftmask << (shift * i)
                part = value & partmask
                value ^= (part << shift) & mask
                result |= part
                i += 1
        return result


def BitshiftLeftXor(value, shift, mask):
        pmask = (value << shift) & mask
        result = value ^ pmask
        return result

def untransform(value):
        value = unBitshiftRightXor(value, 18, 0xffffffff)
        value = unBitshiftLeftXor(value,  15, 0xefc60000)
        value = unBitshiftLeftXor(value,   7, 0x9d2c5680)
        value = unBitshiftRightXor(value, 11, 0xffffffff)
        return value

def MTwister(sv, ndx):
        ndx = ndx % N
        y = (sv[ndx] & UM) | (sv[(ndx + 1) % N] & LM)
        sv[ndx] = sv[(ndx + M) % N] ^ (y >> 1)
        if y & 0x1:
                sv[ndx] ^= 0x9908b0df
        rn = sv[ndx]
        rn = BitshiftRightXor(rn, 11, 0xffffffff)
        rn = BitshiftLeftXor(rn,   7, 0x9d2c5680)
        rn = BitshiftLeftXor(rn,  15, 0xefc60000)
        rn = BitshiftRightXor(rn, 18, 0xffffffff)
        return rn

def getrandbits(sv, ndx, bits):
        bytes = ((bits - 1) / 32 + 1) * 4
        mask = 0xff
        r = []
        result = 0
        for i in range(0, bytes, 4):
                random = MTwister(sv, ndx + (i / 4))
                if bits < 32:
                        random = random >> (32 - bits)
                r.append( random        & mask)
                r.append((random >>  8) & mask)
                r.append((random >> 16) & mask)
                r.append((random >> 24) & mask)
                bits = bits - 32
        j = 0
        for b in r:
                result = (b << (8 * j)) | result
                j += 1
        return result, (i / 4) + 1

# getstatebits works OK when bits % 32 == 0
def getstatebits(sv, value, bits):
        bytes = ((bits - 1) / 32 + 1) * 4
        mask = 0xff
        r = []
        for i in range(0, bytes, 4):
                if bits < 32:
                        value = value << (32 - bits)
                j = 32 * (i/4)
                r.append((value >>  j)       & mask)
                r.append((value >> (j +  8)) & mask)
                r.append((value >> (j + 16)) & mask)
                r.append((value >> (j + 24)) & mask)
                bits = bits - 32
                result = 0
                j = 0
                for b in r:
                        result = (b << (8 * j)) | result
                        j += 1
                sv.append(untransform(result))
                del r[:]
        return (i / 4) + 1
