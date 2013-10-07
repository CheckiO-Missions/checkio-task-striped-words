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
            "input": "Dog,cat,mouse,bird.Human.",
            "answer": 3,
            "explanation": 0
        },
    ]
}
