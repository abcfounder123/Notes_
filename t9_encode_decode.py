# ခလုတ်ဖုန်းနဲ့ စာရေးနည်းပါ။
# T9, encode and decode

encode = {'a': '2', 'b': '22', 'c': '222', 'd': '3', 'e': '33', 'f': '333', 'g': '4', 'h': '44', 'i': '444', 'j': '5', 'k': '55', 'l': '555', 'm': '6', 'n': '66', 'o': '666', 'p': '7', 'q': '77', 'r': '777', 's': '7777', 't': '8', 'u': '88', 'v': '888', 'w': '9', 'x': '99', 'y': '999', 'z': '9999', ' ': '0'}

text = input("Text = ").lower()
ans = ""
last = None

for word in text.split(' '):
    for c in word:
        if c in encode:
            if c == last:
                ans += " "
            ans += encode[c]
            last = c
    ans += '0'
    
print(ans)
print("- " * 39)

decode = {'2': 'a', '22': 'b', '222': 'c', '3': 'd', '33': 'e', '333': 'f', '4': 'g', '44': 'h', '444': 'i', '5': 'j', '55': 'k', '555': 'l', '6': 'm', '66': 'n', '666': 'o', '7': 'p', '77': 'q', '777': 'r', '7777': 's', '8': 't', '88': 'u', '888': 'v', '9': 'w', '99': 'x', '999': 'y', '9999': 'z', '0': ' '}

codes = input("Code = ")
ans = ""

for part in codes.split("0"):
    n = 0
    while n < len(part):
        code = part[n]
        if code == " ":
            part = part[n+1:]
            n = 0
            continue
        if part.count(code) >= 2:
            if code * 4 in part:
                ans += decode[code * 4]
                n += 4
            elif code * 3 in part:
                ans += decode[code * 3]
                n += 3
            elif code * 2 in part:
                ans += decode[code * 2]
                n += 2
        else:
            ans += decode[code]
            n += 1
    ans += " "
    
print(ans)
print("- " * 39)

# 44404666086660777722244666 6665550



