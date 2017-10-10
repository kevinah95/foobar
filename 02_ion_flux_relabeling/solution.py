POPCOUNT_TABLE16 = [0] * 2**16
for index in xrange(len(POPCOUNT_TABLE16)):
    POPCOUNT_TABLE16[index] = (index & 1) + POPCOUNT_TABLE16[index >> 1]

def popcount32_table16(v):
    return (POPCOUNT_TABLE16[ v        & 0xffff] +
            POPCOUNT_TABLE16[(v >> 16) & 0xffff])

def count_lead_and_trail_zeroes(d):
    # https://graphics.stanford.edu/~seander/bithacks.html#ZerosOnRightLinear
    if d:
        v = (d ^ (d - 1) >> 1)  # Set v's trailing 0s to 1s and zero rest
        trailing = 0
        while v:
            v >>= 1
            trailing += 1

        leading = 64
        v = d
        while v:
            v >>= 1
            leading -= 1
        return leading, trailing
    return 64, 64

def getMSBindex(x):
    return (31 - count_lead_and_trail_zeroes(x))

def getMSBmask(x):
    return (1 << getMSBindex(x))


def notSimpleCase(x):
    return ((x+1) & x) and ((x+2) & (x+1))

def parent(node):
    x = node
    bit = x

    while((x & bit) and notSimpleCase(x)):
        y = x + popcount32_table16(x)
        bit = getMSBmask(y & ~x)
        mask = (bit << 1) - 1
        z = (x & mask) + popcount32_table16(x & ~mask)
        if (z == mask and (x & (bit << 1))):
            return node + 1

        x = z
    if (notSimpleCase(x)):
        return node + 1
    else:
        return node + 1 + ( 0 if ((x+1) & x) else x)

print(parent(6))


''' uint32_t parent(const uint32_t node)
{
    uint32_t x = node;
    uint32_t bit = x;

    while ((x & bit) && notSimpleCase(x))
    {
        const uint32_t y = x + popcnt(x);
        bit = getMSBmask(y & ~x);
        const uint32_t mask = (bit << 1) - 1;
        const uint32_t z = (x & mask) + popcnt(x & ~mask);

        if (z == mask && (x & (bit << 1)))
            return node + 1;

        x = z;
    }

    if (notSimpleCase(x))
        return node + 1;
    else
        return node + 1 + (((x+1) & x)? 0: x);
}
 '''