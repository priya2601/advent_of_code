# encryption handshakes


def part1(cardpub=5764801, doorpub=17807724, sub=7):
    loopsize = 0
    val = 1
    while val != cardpub:
        val *= sub
        val %= 20201227
        loopsize += 1
    sub = doorpub
    val = 1
    for i in range(loopsize):
        val *= sub
        val %= 20201227
    return val


print(part1())
print(part1(15733400, 6408062))







15733400
6408062