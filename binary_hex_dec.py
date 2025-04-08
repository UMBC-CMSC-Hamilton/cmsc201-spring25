"""
    Number Systems

        Decimal = live our lives in most of the time
        Binary = 0 or 1 those are the digits, bits = binary digits
        Hexadecimal = Base 16 system 2^4 = 16, basically a shorthand for binary

        Octal = base 8, older computers often had words that were in multiples of 3
            This is also just a shorthand for binary, just in a different condition

    What is decimal?
        83 = 8 * 10 + 3
        4931 = 4 * 1000 + 9 * 100 + 3 * 10 + 1 * 10^0
        Notice that there are 10 digits, from 0 -> 9, 10 is not a digit
            10 = base

    What if we exchange the powers of 10 for the powers of 2?
        2 * 2^3 + 0 * 2^2 + 2 * 1 + 1 * 1
        In order to get uniqueness and a bunch of other nice properties we restrict the digits
            down to bits 0, or 1
        5 in binary
        101b = 1 * 2^2 + 0 * 2^1 + 1 * 2^0 = 5(dec)
        1011 = 1 * 2^3 + 0 * 2^2 + 1 * 2^1 + 1 * 2^0 = 11 (dec)

        Separate groups of 4 bits like this:
        0111 1101 = 0 * 2^7 + 1 * 2^6 + 1 * 2^5 + 1 * 2^4 + 1 * 2^3 + 1 * 2^2 + 1 * 2^0  [skip 2^1]
                  = 64 + 32 + 16 + 8 + 4 + 1 = 125 (dec)

        0011 1010 0011 = 1 + 2 + 32 + 128 + 256 + 512 = 768 + 128 + 32 + 3 = 931 (dec)
        notice that it took 10 bits to represent a 3 digit number.

        47281 => (15 bits)

        binary -> dec

    How do we convert from decimal into binary?
        9(d) into binary

        Rule:
            Ask - is it even or odd? num % 2, odd => bit is 1, even => bit is 0
            Divide the number by 2 [integer divide, so ignore remainders]
            Write the answer from lowest bit up [might feel backwards]

        9 (odd) => 4 (even) => 2 (even) => 1 (odd)
        8421
        1001b = 8 + 1 = 9 [good]

        61(d) => binary
        61 (odd) => 30 (even) => 15 (odd) => 7 (odd) => 3 (odd) => 1(odd)
        0011 1101 => 32 + 16 + 8 + 4 + 1 = 61 [good]

        244
        244 (even) => 122 (even) => 61 (odd) => 30 (even) => 15 odd => 7 odd => 3 (odd) => 1 (odd)
        1111 0100

        533 (finally)
        533 (odd) => 266 (even) => 133 (odd) => 66 (even) => 33 (odd) => 16 (even) => 8(even), 4(even)
            2(even), 1(odd)
        0010 0001 0101 = 512 + 16 + 4 + 1 = 533

        128 into binary (use the method anyway)
        128 (even) => 64 (even) => 32 (even) => 16 (even) => 8 (even) => 4 (even) => 2(even) => 1 (odd)
        1000 0000

        write 1000(d) in decimal 1000, 10,000, 100


    Let's Talk about Hex[adecimal]
        Hex is used as a shorthand for binary

        Base 16 system theres a slight problem.
            We need hexits that go from 0 -> 15, turns out we dont have those.
            Borrow 0->9 as usual.
            a = 10
            b = 11
            c = 12
            d = 13
            e = 14
            f = 15
        binary dec  hex     bin     dec hex bin     dec hex     bin     dec hex
        0000    0   0       0100    4   4   1000    8   8       1100    12  c
        0001    1   1       0101    5   5   1001    9   9       1101    13  d
        0010    2   2       0110    6   6   1010    10  a       1110    14  e
        0011    3   3       0111    7   7   1011    11  b       1111    15  f

        1001 0011 1010 0000 1110 0011 1101 => hex
        (table read)
        93a0e3d

        a97c into binary
        (table read)
        1010 1001 0111 1100


        1011 1000 0110 1010 0011 0110
        into hex =>
        b86a36

        0001 1010 0011 1100 1010 1100 0010 1010 0001 1010 0011 1100 1010 1100 0010 1010
        single 64 bit number [kinda big in binary]

        bin <-> dec
        bin <-> hex
        dec <-> hex [haven't done yet]

        Hex into Decimal first:
            256 16  1
            4   a   f = 4 * 256 + 10 * 16 + 15 = 1024 + 160 + 15 = 1199

            c5 into decimal => [exam question]
            12 * 16 + 5 = 192 + 5 = 197
            4096    256     16      1
            c       2       a       7 => decimal
            12 * 4096 + 2 * 256 + 10 * 16 + 7 = dont compute it

        Decimal into hex:
            decimal => binary => hex

            837 into hex
            837 (odd) => 418 (even) => 209 (odd) => 104 (even) => 52 (even) => 26 (even) => 13 (odd)
                => 6 (even) => 3(odd) => 1(odd)
            0011 0100 0101
            345 (in hex)
"""

print(hex(837))
# 0x is a standard notation out in computer science indicates the number is hex
a = 0x442
b = 0b101010101010
print(a, b)
print(bin(a), bin(b))
print(hex(a), hex(b))
print(type(hex(a)))

# a rule we learned is that you cant start a variable with a number
# here's why
x = 0b00100011100
y = 0xa13ff
z = 0o1712635271717  # octal - super rare
print(x, y, z)


"""
What did we miss with hex last time?
hex = hexadecimal = base 16, 16 = 2^4 we can express 4 binary bits as one hex digit

    converting from decimal to hex [i showed you a quick example where we converted from dec-> binary-> hex]

    Let me show you how to convert directly.
    

83[d] into hex

until number == 0
    bit = number % 2 
    number //= 2
    
until number == 0
    hex_digit = number % 16 (might have to convert if the result is 10, 11, 12, 13, 14, 15)
    number //= 16
Ex 1:
    83 d into hex
    
    83 % 16 = 3
    first digit is 3
    83 // 16 = 5
    5 % 16 = 5, so then we get:
    
    0x53  remember 0x not actually part of the number its just telling you that its base 16
    
Ex 2: 287 into hex

287 % 16 = 287 - 272 = 15 => f [1s place]
287 // 16 = 17

17 % 16 = 1 [16s place]
17 // 16 = 1

1 % 16 = 1 <-- hundreds place [256s place]
1 // 16 = 0

0x11f

Ex: 5948 into hex
12 => c
5948 / 16 = 371
371 % 16 = 3
371 // 16 = 23
23 % 16 = 7
23 // 16 = 1
the last digit is 1

0x173c
"""

