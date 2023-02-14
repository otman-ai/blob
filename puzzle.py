from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

rules = And(
    Or(AKnight,AKnave),
    Not(And(AKnight,AKnave)),
    Or(BKnight,BKnave),
    Not(And(BKnight,BKnave)),
    Or(CKnight,CKnave),
    Not(And(CKnight,CKnave)),
    )
# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    rules,
    Biconditional(AKnight,And(AKnight,AKnave)),
    Biconditional(AKnave,Not(And(AKnave,AKnight)))
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    rules,
    Biconditional(AKnight,And(BKnave,AKnave)),
    Biconditional(AKnave,Or(Not(AKnave),Not(BKnave)))
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."

sent_A = Or(And(AKnight,BKnight),And(AKnave,BKnave))
sent_B = Or(And(AKnight,BKnave),And(AKnave,BKnight))

knowledge2 = And(
   rules,
   Biconditional(AKnight,sent_A),Biconditional(AKnave,Not(sent_A)),
   Biconditional(BKnight,sent_B),Biconditional(BKnave,Not(sent_B))
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
sent_A2 = Or(Or(Biconditional(AKnight,AKnight),Biconditional(AKnave,Not(AKnight))),
Or(Biconditional(AKnight,AKnave),Biconditional(AKnave,Not(AKnave))))

sent_B2 = Or(Biconditional(BKnight,Or(Biconditional(AKnave,AKnave),Biconditional(AKnight,AKnave))),
Biconditional(BKnave,Not(Or(Biconditional(AKnave,AKnave),Biconditional(AKnight,AKnave)))))

sent_B22 = Or(Biconditional(BKnight,CKnave),Biconditional(BKnave,Not(CKnave)))

sent_C = Or(Biconditional(CKnave,Not(AKnight)),Biconditional(CKnight,AKnight))
knowledge3 = And(
    rules,
    sent_A2,
    sent_B2,
    sent_B22,
    sent_C
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
