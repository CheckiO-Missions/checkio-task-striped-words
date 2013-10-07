"""
TESTS is a dict with all you tests.
Keys for this will be categories' names.
Each test is dict with
    "input" -- input data for user function
    "answer" -- your right answer
    "explanation" -- not necessary key, it's using for additional info in animation.
"""

TESTS = {
    "Basics": [
        {
            "input": "My name is ...",
            "answer": 3,
            "explanation": 0
        },
        {
            "input": "Hello world",
            "answer": 0,
            "explanation": 0
        },
        {
            "input": "A quantity of striped words.",
            "answer": 1,
            "explanation": 0
        },
        {
            "input": "Dog,cat,mouse,bird.Human.",
            "answer": 3,
            "explanation": 0
        },

    ],
    "Extra": [
        {
            "input": "Lorem ipsum dolor sit amet, consectetuer adipiscing elit.",
            "answer": 5},
        {
            "input": "To take a trivial example, which of us ever undertakes laborious physical exercise, except to obtain some advantage from it?",
            "answer": 8},
        {
            "input": "The European languages are members of the same family. Their separate existence is a myth.",
            "answer": 6},
        {
            "input": "For science, music, sport, etc, Europe uses the same vocabulary. The languages only differ in their grammar, their pronunciation and their most common words.",
            "answer": 6},

    ],
    "Extra2": [
        {
            "input": "1 2 3 12 13",
            "answer": 0},
        {
            "input": "1st 2a ab3er root rate",
            "answer": 1},
        {
            "input": "JJJ:qwerty,iddqd,hoho",
            "answer": 1},
        {
            "input": "I can see dead people. yes,no.",
            "answer": 2},
    ]
}
