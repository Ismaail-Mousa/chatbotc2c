import random

def chatbot():
    print("Welcome to Math Helper Bot!")
    name = input("What's your name? ")
    age = input("How old are you? ")
    print(f"Nice to meet you, {name}! It's great to chat with someone who is {age} years old.")
    
    print("\nHow can I help you today?")
    
    while True:
        print("\nPlease choose an option from the list below:")
        print("1. Learn a fact about Algebra")
        print("2. Learn a fact about Geometry")
        print("3. Learn a fact about Calculus")
        print("4. Exit the conversation")
        
        choice = input("Enter the number of your choice: ")
        
        if choice == "1":
            algebra_facts = [
                "The word 'algebra' comes from the Arabic word 'al-jabr', which means 'reunion of broken parts'.",
                "Algebra was formalized by the Persian mathematician Al-Khwarizmi in the 9th century.",
                "In algebra, a variable represents an unknown value that can change.",
                "Linear equations are called 'linear' because their graph forms a straight line.",
                "Algebra is used in cryptography to secure digital communications."
            ]
            print(random.choice(algebra_facts))
        elif choice == "2":
            geometry_facts = [
                "Euclid is known as the 'Father of Geometry' for his work in the field over 2,000 years ago.",
                "The sum of the angles in a triangle is always 180 degrees in Euclidean geometry.",
                "A circle has infinite lines of symmetry because it looks the same when rotated.",
                "The Pythagorean Theorem relates the sides of a right triangle: \(a^2 + b^2 = c^2\).",
                "The term 'geometry' comes from Greek words meaning 'earth measurement'.",
                "Archimedes discovered formulas for the areas and volumes of shapes, paving the way for integral calculus."
            ]
            print(random.choice(geometry_facts))
        elif choice == "3":
            calculus_facts = [
                "Calculus was independently developed by Isaac Newton and Gottfried Wilhelm Leibniz in the 17th century.",
                "The term 'calculus' comes from the Latin word meaning 'small stone', used for counting.",
                "Differentiation in calculus helps find rates of change, such as speed or acceleration.",
                "Integration in calculus can calculate areas under curves and the total accumulation of quantities.",
                "The Fundamental Theorem of Calculus links differentiation and integration as inverse processes.",
                "Calculus is widely used in physics, engineering, economics, and biology to model dynamic systems."
            ]
            print(random.choice(calculus_facts))
        elif choice == "4":
            print(f"Goodbye, {name}! Have a great day!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

chatbot()
