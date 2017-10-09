def parent():





uint32_t parent(const uint32_t node)
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
