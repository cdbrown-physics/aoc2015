from numpy import prod


if __name__ == "__main__":
    totalWrapping = 0
    bowLength = 0
    with open("input.txt", 'r') as file:
        for line in file:
            line = line.strip('\n')
            l, w, h = [int(s) for s in line.split('x')]
            sides = [2*l*w, 2*w*h, 2*h*l]
            side_ = [l*w, w*h, h*l]
            totalWrapping += sum(sides) + min(side_)
            
            bowdist = l*w*h
            foo = [l,w,h]
            foo.remove(max(foo))
            parim = foo[0] + foo[0] + foo[1] + foo[1]
            
            bowLength += bowdist + parim     
    

    print(totalWrapping)
    print(bowLength)
            
    