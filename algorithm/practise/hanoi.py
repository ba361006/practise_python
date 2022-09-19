def hanoi(n, src, aux, dst):
    if n == 1:
        print(f"move plate {n} from {src} to {dst}")
    else:
        hanoi(n-1, src, dst, aux)
        print(f"move plate {n} from {src} to {dst}")
        hanoi(n-1, aux, src, dst)


if __name__ == "__main__":
    hanoi(3, "A", "B", "C")
    