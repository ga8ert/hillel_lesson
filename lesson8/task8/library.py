rules = {
    "Rock": {"Rock": "Draw", "Paper": "Loss", "Scissors": "Win"},
    "Paper": {"Rock": "Win", "Paper": "Draw", "Scissors": "Loss"},
    "Scissors": {"Rock": "Loss", "Paper": "Win", "Scissors": "Draw"}
}

def number_conversion(number):
    """
    This function converts the result
    """
    if number == 1:
        return "Rock"
    elif number == 2:
        return "Paper"
    elif number == 3:
        return "Scissors"

