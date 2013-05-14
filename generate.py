from pymarkovchain import MarkovChain


def main():
    with open('corpus.txt') as f:
        MarkovChain().generateDatabase(f.read())

        while True:
            print MarkovChain().generateString()
            raw_input()


if __name__ == '__main__':
    main()
