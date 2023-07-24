letters=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
playing = " "
final = " "
org = " "

def encrypt(str,n):
    result = []
    for x in str:
        if x == " ":
            convert = "  "
            result.append(convert)
        else:
            convert = (letters.index(x) +n) %26
            result.append(letters[convert])
    final = " ".join(result)
    print(final)
    return final

def decrypt(str,n):
    back = []
    for x in str:
        if x == " ":
            original = "  "
            back.append(original)
        else:
            original = (letters.index(x) -n) %26
            back.append(letters[original])
    org = " ".join(back)
    print(org)

str=input("\nType the word you want encrypted? ")
# This moves the letters e.g. 2 would change A to C, B to D etc.
n=int(input("\nEnter a number for the key? "))
final=encrypt(str,n)

print("\nThe text will now be decrypted. ")
# This changes the letters back to the original word.
decrypt(final,n)
