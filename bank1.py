def main():
    greeting = input("input word: ")
    print(value(greeting))


def value(greeting):
    greeting = greeting.lower()

    if greeting[:5] == "hello":
        return 0
    elif greeting[0] == "h":
        return 20
    else:
        return 100




if __name__ == "__main__":
    main()