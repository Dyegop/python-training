import re

"""
Check out how many times the word BALLOON can be formed within a string
"""

raw_string = "BAOOLLNNOLOLGBAXNNWDOOAABAAPÑMOOEENLLOOOOOOLLNBMMKAOPOOPLAJDIWPQODJANPJOPOJADUATYABDVCKÑAOOAODJABNCJACBAIKDOAHAHAAANNNOOLLABBBAGATAII"
pattern = re.compile("[BALON]")


def solution(string: str):
    check = {"B": 1, "A": 1, "L": 2, "O": 2, "N": 1}
    match = re.findall(pattern, string)
    counter = {}
    for letter in match:
        counter[letter] = match.count(letter)
    result = {k: int(counter[k]/check[k]) for k in counter}
    print(min(result.values()))


solution(raw_string)
