import re

def uk_postcodes(postcode):
    # This will check the regex pattern for UK postcodes
    fit = "^[A-Z]{1,2}[0-9R][0-9A-Z]? [0-9][A-Z]{2}$"
    
    # This will compile the regex pattern
    regex = re.compile(fit)
    
    # This will check the postcode to see if it fits the pattern
    if regex.match(postcode):
        print(f"{postcode} True")
    else:
        print(f"{postcode} False")

# This function should result in the match being found as true

print("\nRegex used: '^[A-Z]{1,2}[0-9R][0-9A-Z]? [0-9][A-Z]{2}$'")

print("\nTrue:")
uk_postcodes("M1 1AA")
uk_postcodes("M60 1NW")
uk_postcodes("CR2 6XH")
uk_postcodes("DN55 1PT")
uk_postcodes("W1A 1HQ")
uk_postcodes("EC1A 1BB")

# This function should result in the match being found as false
print("\nFalse:")
uk_postcodes("ABC 1234")
uk_postcodes("ZYXW 987")
uk_postcodes("SO16 ZFD")
uk_postcodes("8PA UR6")
uk_postcodes("S016 FD9")
uk_postcodes("16SO 9FD")

