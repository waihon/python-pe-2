def print_leds(num):
    if not str(num).isdigit():
        return

    leds = [
        ['    #', '#####', '#####', '#   #', '#####', '#####', '#####', '#####', '#####', '#####'], 
        ['    #', '    #', '    #', '#   #', '#    ', '#    ', '    #', '#   #', '#   #', '#   #'], 
        ['    #', '#####', '#####', '#####', '#####', '#####', '    #', '#####', '#####', '#   #'], 
        ['    #', '#    ', '    #', '    #', '    #', '#   #', '    #', '#   #', '    #', '#   #'], 
        ['    #', '#####', '#####', '    #', '#####', '#####', '    #', '#####', '#####', '#####'],
    ]

    for row in range(5):
        for digit in str(num):
            try:
                digit = int(digit) - 1
                print(leds[row][digit], end=" ")
            except:
                continue # skip non number
        print()
    print()

if __name__ == "__main__":
    print_leds(1234567890)
    print_leds(9876543210)
    print_leds(1357902468)
    print_leds(2468135790)
