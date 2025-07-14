def print_formatted(number):
    width = len(bin(number)[2:])  # Get width of binary representation
    output  = []
    for i in range(1, number + 1):
        deci = str(i).rjust(width)
        octal = oct(i)[2:].rjust(width)
        hexa = hex(i)[2:].upper().rjust(width)
        binary = bin(i)[2:].rjust(width)
        print(deci, octal, hexa, binary)
        output.append(f"{deci} {octal} {hexa} {binary}")
    return output


# n = int(input())
# w = len("{0:b}".format(n))
# for i in range(1,n+1):
#   print ("{0:{width}d} {0:{width}o} {0:{width}x} {0:{width}b}".format(i, width=w))

