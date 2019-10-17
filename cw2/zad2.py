def fun(data_text):
    return dict({"length": len(data_text),
                 #"length": data_text.count('') - 1,
                 "letters": list(data_text),
                 "big_letters": data_text.upper(),
                 "small_letters": data_text.lower()})


print(fun("Przykladowy tekst"))