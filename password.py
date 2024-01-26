ask = input("plz text x to start")
if ask == "x":
 codes = []
 for n in range(10000):
    code = f"{n:04d}"
    codes.append(code)
 codes_ = "\n".join(codes)
with open("digits.txt", "w") as f:
 print(codes_, file=f)

