a = input("What is the Answer to the Great Question Of Life, the Universe, and Everything? ")

match a.lower().strip():
    case "42" | "forty-two" | "forty two":
        print("Yes")
    case _:
        print("No")