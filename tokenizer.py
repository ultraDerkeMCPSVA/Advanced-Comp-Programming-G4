test_string = (
        "void foobar(void)\n"
        "{\n"
        "\t// comment\n"
        "}"
    )


special_chars = (
        "\t",
        " ",
        "\n",
        "\b"
    )

def tokenize(string):
    stripped, temp, spacelen, strlen = False, "", 0, len(string)
    for idx, x in enumerate(string):
        if x in special_chars:
            start, stripped, spacelen = idx, True, spacelen + 1
            continue
        elif stripped is True: break
        temp += x
    string = string[len(temp) + spacelen:strlen]
    return temp, string


def get_all_words():
    word, string = "", test_string
    while True:
        word, string = tokenize(string)
        print(word)
        if word is "": break

get_all_words()

template = (
        "void {}(void) {{\n"
        "\tint something = {};\n"
        "\tprintf(\"%d\\n\", something)\n"
        "}}\n"
    )

with open('bank_info.bnk', mode='w') as f:
    f.write(template.format("foo", 67))
