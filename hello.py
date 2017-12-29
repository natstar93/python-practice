def greet(name, iteration):
    print('{iteration}: hello {name}'.format(iteration=iteration, name=name))

def main():
    print('It works')
    name = input('What is your name?\n')
    print ('Hi, %s.' %name)
    blerbs = ['nat', 'pto', 'dusky']
    for i, name in enumerate(blerbs):
        greet(name, i)
    curr, acc = (1, 1)
    while acc < 100:
        print ('acc is {0}'.format(acc))
        curr, acc = (acc, curr + acc)

if __name__ == '__main__':
    main()
