#include <iostream>

uint32_t node_id = 0;
uint32_t failed = 0;

uint32_t popcnt(const uint32_t x)
{ return __builtin_popcount(x); }

uint32_t getMSBindex(const uint32_t x)
{ return 31 - __builtin_clz(x); }

uint32_t getMSBmask(const uint32_t x)
{ return 1 << getMSBindex(x); }

uint32_t notSimpleCase(const uint32_t x)
{ return ((x+1) & x) && ((x+2) & (x+1)); }


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

uint32_t test(const int32_t depth)
{
    if (depth)
    {
        const uint32_t left = test(depth - 1);
        const uint32_t right = test(depth - 1);
        ++node_id;
        if (left != node_id) ++failed;
        if (right != node_id) ++failed;
    }
    else
    {
        ++node_id;
    }

    return parent(node_id);
}

int main()
{
    test(3);
    std::cout << "nodes: " << node_id << '\n';
    std::cout << "failed: " << failed << '\n';
    std::cout << "parent: " << parent(31) << '\n';
}
