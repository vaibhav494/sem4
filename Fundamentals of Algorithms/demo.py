def robinkarp(string, pattern):
    if len(string) < len(pattern):
        return False
    
    psum = sum([ord(char)-96 for char in pattern])
    ssum = sum([ord(char)-96 for char in string[0:len(pattern)]])

    for i in range(len(string)-len(pattern)+1):
        if i != 0 :
            ssum = ssum + ord(string[i+len(pattern)-1]) - 96

        cc = string[i:i+len(pattern)]
        if psum == ssum:
            if check(cc, pattern):
                return True
        ssum = ssum - ord(string[i]) + 96

def check(ss, pattern):
    for i in range(len(ss)):
        if ss[i] != pattern[i]:
            return False
    return True

string = "ccaccaaedba"
pattern = "dba"
print(robinkarp(string, pattern))