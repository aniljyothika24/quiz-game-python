
quiz = [
    {
    "question" : "which planet is closest to earth?",
    "options" : ["Mercury", "Jupiter", "Earth","Venus"],
    "answer" : "Mercury"
    },
    {
    "question" : "what is the largest ocean in the world?",
    "options" : ["Atlantic ocean", "Pacific ocean", "Arctic Ocean","Southern Ocean"],
    "answer" : "Pacific Ocean"
    },
    {
    "question" : "what is the tallest mountain in the world?",
    "options" : ["K2", "Mount Everest", "Mount Kilimanjaro","Kangchenjunga"],
    "answer" : "Mount Everest"
    },
    {
    "question" : "Name the lightsest gas.",
    "options" : ["Oxygen", "Hydrogen", "Helium","Nitrogen"],
    "answer" : "Hydrogen"
    },
    {
    "question" : "How many bones are in the adult human body?",  
    "options" : ["106","206","306","406"],
    "answer" : "206"
    }
]


while True:
    score=0
    choice = int(input("1.Start Quiz \n2.Exit \n1/2? "))
    if choice == 1:
        for question in quiz:
            print(question["question"])
            print(question["options"])
            user_ans=input("Type your answer- ").lower()
            if user_ans == question["answer"].lower():
                print("Yayy!!Correct Answer")
                score += 1
            else:
                print("wrong answer")          
    else:
        exit()
    print("Your total score is - ",score,"/5")


    