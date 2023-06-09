def main():
    height = 0
    while height < 1 or height > 8:
        height = int(input("Height: "))

    for i in range(height):
        for j in range(height - i - 1):
            print(" ", end="")
        for k in range(i + 1):
            print("#", end="")
        print()

if __name__ == "__main__":
    main()
