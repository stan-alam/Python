from collections import Counter

responses = [
    "bepsi",
    "stonks",
    "sheck"
]

print("they voted for {} meme_grammar".format (
Counter(responses).most_common(1)[0][0]
    )
)
