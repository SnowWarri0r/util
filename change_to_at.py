def change_to_at(s: str):
    s = s.strip()
    ss = s.split("\n")
    for i in range(len(ss)):
        ss[i] = "@" + ss[i]
    res = " ".join(ss)
    print(res + " ")


# if __name__ == "__main__":

