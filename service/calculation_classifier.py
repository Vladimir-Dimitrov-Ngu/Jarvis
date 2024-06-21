import re

calc_regex = re.compile(
    r"(вычис|считат|корен|сколь|плюс|минус|умножить|делить|\+|\-|\*|\/)", re.IGNORECASE
)


def calc_classify(texts):
    if type(texts) is list:
        results = []
        for text in texts:
            if calc_regex.search(text):
                results.append((text, "calc"))
            else:
                results.append((text, "other"))
    else:
        if calc_regex.search(texts):
            results = True
        else:
            results = False

    return results


if __name__ == "__main__":
    texts = [
        "Сколько будет 2 плюс 2?",
        "Какая сегодня погода?",
        "Посчитай мне, сколько будет 5 умножить на 6.",
        "Вычислить 3 в степени 4?",
        "Сколько будет корень из 16?",
        "Как тебя зовут?",
        "2 + 2",
        "Сколько будет 2 плюс 2 умножить на 3?",
    ]
    classified_texts = calc_classify(texts)
    for text, label in classified_texts:
        print(f"Text: {text}, Label: {label}")
