def filter_by_state(dictionary: dict, state: str) -> list[dict]:
    """Функция,которая возвращает новый список словарей, содержащий только те словари,
    у которых ключ state соответствует указанному значению"""
    new_dictionary: list[dict] = [{}]
    for date in dictionary:
        if date["state"] == state:
            new_dictionary.append(date)
    return new_dictionary


def sort_by_date(dictionary: dict, ascending=False) -> list[dict]:
    """Функция, которая возвращает новый список, отсортированный по дате"""
    if ascending == False:
        return sorted(dictionary, key=lambda ascending: ascending["date"])
    else:
        return sorted(dictionary, key=lambda ascending: ascending["date"], reverse=True)