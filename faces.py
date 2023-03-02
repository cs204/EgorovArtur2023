def main():
    s=input()
    print(convert(s))
def convert(s):
    s=s.replace(":)","\N{Slightly Smiling face}")
    s=s.replace(":(","\N{Slightly Frowning face}")
    return(s)
main()