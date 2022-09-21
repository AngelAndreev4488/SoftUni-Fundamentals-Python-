test_str = input()


res = [idx for idx in range(len(test_str)) if test_str[idx].isupper()]
print(str(res))