def score_answer(answer):
    words = len(answer.split())

    if words < 10:
        return 4
    elif words < 20:
        return 7
    return 9