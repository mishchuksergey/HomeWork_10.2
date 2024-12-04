from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(input_user: str) -> str:
    """Функция, которая обрабатывает информацию как о картах, так и о счетах"""
    if "Счет" in input_user:
        return f"Счет {get_mask_account(input_user.split()[-1])}"
    else:
        card_number = get_mask_card_number(input_user.split()[-1])
        card_mask = input_user.replace(input_user.split()[-1], card_number)
        return card_mask


def get_date(date: str) -> str:
    """Функция которая возвращает дату в новом формате"""
    new_date = date[:10].split("-")
    return ".".join(new_date[::-1])
