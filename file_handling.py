
topics = {
    "Python": [
        {
            "questions": "What is the output of the following code: print(type([]))?",
            "options": ["A) <class 'list'>", "B) <class 'dict'>", "C) <class 'tuple'>", "D) <class 'set'>"],
            "answer": "A"
        },
        {
            "questions": "Which of the following is the correct syntax to create a function in Python?",
            "options": ["A) function myFunction()", "B) def myFunction():", "C) create myFunction()", "D) func myFunction():"],
            "answer": "B"
        },
        {
            "questions": "What is the result of 3 * 1 ** 3?",
            "options": ["A) 3", "B) 1", "C) 9", "D) 27"],
            "answer": "A"
        },
        {
            "questions": "How do you insert a comment in Python?",
            "options": ["A) // This is a comment", "B) # This is a comment", "C) /* This is a comment */", "D) <!-- This is a comment -->"],
            "answer": "B"
        },
        {
            "questions": "Which method can be used to remove whitespace from a string?",
            "options": ["A) strip()", "B) trim()", "C) len()", "D) slice()"],
            "answer": "A"
        },
        {
            "questions": "What is the output of the following code: print(2 == 2 == 1)?",
            "options": ["A) True", "B) False", "C) 1", "D) 0"],
            "answer": "B"
        },
        {
            "questions": "Which of the following is not a valid variable name in Python?",
            "options": ["A) my_var", "B) 2ndVar", "C) var_2", "D) _myVar"],
            "answer": "B"
        },
        {
            "questions": "What will be the output of this code: print(bool(0))?",
            "options": ["A) True", "B) False", "C) None", "D) Error"],
            "answer": "B"
        },
        {
            "questions": "Which data type is immutable in Python?",
            "options": ["A) List", "B) Set", "C) Dictionary", "D) Tuple"],
            "answer": "D"
        },
        {
            "questions": "What does the len() function do?",
            "options": ["A) Returns the length of an object", "B) Returns the first element of an object", "C) Returns the type of an object", "D) Returns the last element of an object"],
            "answer": "A"
        },
    ],
    "RDBMS": [
        {
            "questions": "What does SQL stand for?",
            "options": ["A) Structured Query Language", "B) Standard Query Language", "C) Simple Query Language", "D) Sequential Query Language"],
            "answer": "A"
        },
        {
            "questions": "Which command is used to retrieve data from a database?",
            "options": ["A) SELECT", "B) RETRIEVE", "C) GET", "D) FETCH"],
            "answer": "A"
        },
        {
            "questions": "Which of the following is a primary key?",
            "options": ["A) A unique identifier for a record", "B) A foreign key", "C) A duplicate value", "D) An index"],
            "answer": "A"
        },
        {
            "questions": "What is a foreign key?",
            "options": ["A) A key referencing a primary key in another table", "B) A unique identifier", "C) A column with null values", "D) A temporary key"],
            "answer": "A"
        },
        {
            "questions": "Which SQL keyword is used to sort the result set?",
            "options": ["A) ORDER BY", "B) SORT BY", "C) ARRANGE BY", "D) ALIGN BY"],
            "answer": "A"
        },
        {
            "questions": "What does the COUNT() function do in SQL?",
            "options": ["A) Counts the number of rows", "B) Counts the number of columns", "C) Sums up numeric values", "D) Returns the maximum value"],
            "answer": "A"
        },
        {
            "questions": "Which SQL statement is used to insert data into a table?",
            "options": ["A) INSERT INTO", "B) ADD DATA", "C) INPUT INTO", "D) ADD ROW"],
            "answer": "A"
        },
        {
            "questions": "What is a JOIN in SQL?",
            "options": ["A) Combining rows from two or more tables", "B) Creating a new table", "C) Deleting rows from a table", "D) Modifying existing rows"],
            "answer": "A"
        },
        {
            "questions": "Which of the following is not a type of JOIN?",
            "options": ["A) INNER JOIN", "B) OUTER JOIN", "C) CROSS JOIN", "D) FULL KEY JOIN"],
            "answer": "D"
        },
        {
            "questions": "Which command is used to delete a table in SQL?",
            "options": ["A) DROP TABLE", "B) DELETE TABLE", "C) REMOVE TABLE", "D) ERASE TABLE"],
            "answer": "A"
        },
    ],
    "JavaScript": [
        {
            "questions": "What is JavaScript primarily used for?",
            "options": ["A) Styling web pages", "B) Server-side programming", "C) Client-side scripting", "D) Database management"],
            "answer": "C"
        },
        {
            "questions": "Which of the following is used to declare a variable in JavaScript?",
            "options": ["A) var", "B) let", "C) const", "D) All of the above"],
            "answer": "D"
        },
        {
            "questions": "What is the output of '2' + 2 in JavaScript?",
            "options": ["A) 4", "B) 22", "C) Error", "D) None of the above"],
            "answer": "B"
        },
        {
            "questions": "Which symbol is used for comments in JavaScript?",
            "options": ["A) //", "B) #", "C) /* */", "D) <!-- -->"],
            "answer": "A"
        },
        {
            "questions": "Which method is used to find the length of a string?",
            "options": ["A) length", "B) size", "C) len()", "D) getSize()"],
            "answer": "A"
        },
        {
            "questions": "Which keyword is used to define a function in JavaScript?",
            "options": ["A) function", "B) def", "C) func", "D) define"],
            "answer": "A"
        },
        {
            "questions": "What is the purpose of the 'this' keyword in JavaScript?",
            "options": ["A) Refers to the current object", "B) Refers to the parent object", "C) Refers to the global object", "D) None of the above"],
            "answer": "A"
        },
        {
            "questions": "What is the DOM in JavaScript?",
            "options": ["A) Document Object Model", "B) Data Object Manager", "C) Document Oriented Model", "D) Data Object Model"],
            "answer": "A"
        },
        {
            "questions": "Which of the following is a valid way to define an array in JavaScript?",
            "options": ["A) []", "B) Array()", "C) Both A and B", "D) None of the above"],
            "answer": "C"
        },
        {
            "questions": "Which method is used to add elements to an array?",
            "options": ["A) push()", "B) add()", "C) append()", "D) insert()"],
            "answer": "A"
        },
    ],
}



def register():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    
    with open("user_data.txt", "a") as file:
        file.write(f"{username}:{password}\n")
    print("Registration successful!")



def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    
    with open("user_data.txt", "r") as file:
        for line in file:
            stored_username, stored_password = line.strip().split(":")
            if username == stored_username and password == stored_password:
                print("Login successful!")
                return True
    print("Invalid credentials!")
    return False



def run_quiz(topic):
    questions = topics.get(topic, [])
    score = 0
    for q in questions:
        print(q["questions"])
        for option in q["options"]:
            print(option)
        answer = input("Your answer (A, B, C, or D): ").upper()
        if answer == q["answer"]:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer was {q['answer']}.\n")

    print(f"Your final score is: {score}/{len(questions)}")


def main():
    while True:
        choice = input("1: Register\n2: Login\n3: Exit\nChoose an option: ")
        if choice == "1":
            register()
        elif choice == "2":
            if login():
                print("Select a topic: Python, RDBMS, JavaScript")
                topic = input("Enter the topic: ").lower()
                if topic in topics:
                    run_quiz(topic)
                else:
                    print("Invalid topic!")
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice! Try again.")



main()