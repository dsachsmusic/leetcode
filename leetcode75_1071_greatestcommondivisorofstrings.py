#this was generated using chatgpt, from my powershell (which might be wrong)
str1 = "ABCABC"
str2 = "ABCABCABCABC"

shorter_string = min(str1, str2, key=len)
longer_string = max(str1, str2, key=len)

for i in range(len(shorter_string), 0, -1):
    shorter_string_base_try = shorter_string[:i]
    shorter_string_base_try_test = ""
    if len(longer_string) % len(shorter_string_base_try) == 0:
        for j in range(1, len(longer_string) // len(shorter_string_base_try) + 1):
            shorter_string_base_try_test += shorter_string_base_try

        if shorter_string_base_try_test == longer_string:
            print(shorter_string_base_try)
            break