"""
Chicago bridge scoring engine.
Contract format: "4H N", "3NT S", "6S X E", "3D XX N"
Result format: "==", "+1", "-2"
"""

SUIT_TRICKS = {
    "C": 20,
    "D": 20,  # minors
    "H": 30,
    "S": 30,  # majors
    "NT": 30,  # NT (first trick is 40, handled separately)
}


def get_vulnerability(board_num):
    """Chicago vulnerability cycles over 4 boards."""
    cycle = (board_num - 1) % 4
    return {
        0: "none",
        1: "ns",
        2: "ew",
        3: "both",
    }[cycle]


def is_vulnerable(declarer, board_num):
    vuln = get_vulnerability(board_num)
    if vuln == "none":
        return False
    if vuln == "both":
        return True
    if declarer in ("N", "S"):
        return vuln == "ns"
    if declarer in ("E", "W"):
        return vuln == "ew"
    return False


def parse_contract(contract_str):
    """
    Parse contract string into components.
    Examples: "4H N", "3NT S X", "6S X E", "3D XX N"
    Returns: (level, suit, declarer, doubled, redoubled)
    """
    parts = contract_str.strip().upper().split()
    if len(parts) < 2:
        raise ValueError(f"Invalid contract: {contract_str}")

    # First part is level+suit e.g. "4H" or "3NT"
    level_suit = parts[0]
    level = int(level_suit[0])
    suit = level_suit[1:]  # "H", "S", "NT", "C", "D"

    doubled = False
    redoubled = False
    declarer = None

    for part in parts[1:]:
        if part == "X":
            doubled = True
        elif part == "XX":
            redoubled = True
        elif part in ("N", "S", "E", "W"):
            declarer = part

    if declarer is None:
        raise ValueError(f"No declarer in contract: {contract_str}")

    return level, suit, declarer, doubled, redoubled


def parse_result(result_str):
    """
    Parse result string.
    "==" -> 0, "+1" -> 1, "-2" -> -2
    """
    result_str = result_str.strip()
    if result_str == "==":
        return 0
    return int(result_str)


def calculate_score(contract_str, result_str, board_num):
    """
    Calculate bridge score.
    Returns score from declarer's perspective (positive = made, negative = down).
    """
    try:
        level, suit, declarer, doubled, redoubled = parse_contract(contract_str)
        tricks_result = parse_result(result_str)
        vuln = is_vulnerable(declarer, board_num)

        if tricks_result < 0:
            return calculate_undertricks(tricks_result, doubled, redoubled, vuln)
        else:
            return calculate_make(level, suit, tricks_result, doubled, redoubled, vuln)

    except Exception as e:
        return None  # invalid input


def calculate_make(level, suit, overtricks, doubled, redoubled, vuln):
    # Trick score per bid trick
    if suit == "NT":
        trick_score = 40 + (level - 1) * 30  # first trick 40, rest 30
    else:
        trick_score = SUIT_TRICKS[suit] * level

    # Apply doubling to trick score
    if redoubled:
        trick_score *= 4
    elif doubled:
        trick_score *= 2

    # Game/part score bonus
    if trick_score >= 100:
        game_bonus = 500 if vuln else 300
    else:
        game_bonus = 50  # part score bonus

    # Slam bonuses
    slam_bonus = 0
    if level == 6:
        slam_bonus = 750 if vuln else 500
    elif level == 7:
        slam_bonus = 1500 if vuln else 1000

    # Overtrick score
    if redoubled:
        overtrick_score = overtricks * (400 if vuln else 200)
    elif doubled:
        overtrick_score = overtricks * (200 if vuln else 100)
    else:
        overtrick_score = overtricks * SUIT_TRICKS[suit]
        if suit == "NT":
            overtrick_score = overtricks * 30

    # Insult bonus for doubled/redoubled make
    insult = 0
    if redoubled:
        insult = 100
    elif doubled:
        insult = 50

    return trick_score + game_bonus + slam_bonus + overtrick_score + insult


def calculate_undertricks(tricks_down, doubled, redoubled, vuln):
    n = abs(tricks_down)

    if not doubled and not redoubled:
        return -(50 * n if not vuln else 100 * n)

    if doubled:
        if not vuln:
            # 100, 200, 200, 200...
            score = 100
            score += min(n - 1, 2) * 200
            score += max(n - 3, 0) * 300
        else:
            # 200, 300, 300...
            score = 200
            score += (n - 1) * 300
        return -score

    if redoubled:
        if not vuln:
            score = 200
            score += min(n - 1, 2) * 400
            score += max(n - 3, 0) * 600
        else:
            score = 400
            score += (n - 1) * 600
        return -score


def vulnerability_display(board_num):
    """Human readable vulnerability for display."""
    vuln = get_vulnerability(board_num)
    return {
        "none": "None",
        "ns": "N/S",
        "ew": "E/W",
        "both": "Both",
    }[vuln]
