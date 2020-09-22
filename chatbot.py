a = [
    '- Trouble Breathing', '- Persistent pain', '- Pressure in the chest',
    '- New confusion', '- Inability to wake or stay awake',
    '- Bluish lips or face'
]
b = [
    '- Fever of 100F (37.8 C) or above'
    '- Trouble breathing',
    '- Possible fever symptoms: alternating chills and sweating',
    '- Shortness of breath', '- Severe wheezing',
    '- Chills or repeated shaking with chills', '- Muscle or body aches',
    '- Sore throat', '- Loss of smel or taste, or change in taste',
    '- Nausea, vomiting, or diarrhea', '- Headache'
]
c = ['- Shared a home', '- Been within 6 feet of the person for at least 5 minutes', '- Got sneezed on or coughed', '- Shared eating or drinking utensils or other items', '- Hugged or kissed or come into close contact']
d = ['- Wash your hands often', '- Avoid close contact', '- Always wear your mask in public', '- Cover your coughs and sneezes', '- Clean and disinfect regularly']

print("Hello, my name is Corona! I am your personal healthcare assistant!")
print()
name = input("What is your name? \n \n")
print()
print(
    "Hello " + name +
    ", I will just ask you a few questions to see if you need to be tested for COVID-19. Is that okay?"
)
print()
answer = input()
code = "maybe"
while (code == "maybe"):
    if (answer == "no"):
        print()
        print("Okay, thank you for your time!")
        code = "no"
    elif (answer == "yes"):
        print()
        print("Do you have any of these emergency signs:")
        print()
        print(*a, sep="\n")
        print()
        answer1 = input("")
    elif (answer1 == "yes"):
        print()
        print(
            "I suggesst that you immediately seek medical attention and let them know that you may have COVID-19."
        )
        code = "no"
    elif (answer1 == "no"):
        print()
        print(
            "Did you have any of these types of contact with someone that is confirmed with COVID-19:"
        )
        print()
        print(*c, sep="\n")
        print()
        passcode = "no";
        answer2 = input()
        if(answer2 == "no"):
          print()
          print(
                "Okay, Did you show any of these symptoms in the last 48 hours:"
            )
          print()
          print(*b, sep="\n")
          print()
          answer3 = input()
          if (answer3 == "no" and passcode == "no"):
              print()
              print(
                "Okay, your responses indicate that you do not need to get tested for COVID-19. You are safe!" )
              print()
              print(
                    "A quick reminder on how to stay safe during this pandemic: ")
              print()
              print(*d, sep="\n")
              print()
              code= "no";
          if (answer3 == "yes"):
                print()
                print(
                "How many of these symptoms did you face in the last 48 hours?"
            )
                print();
                number = input();
                number = int(number);
                if (number == 1 or number == 0):
                  if(passcode =='no'):
                     print (
                    "You do not seem to be having multiple of these symptoms. This could mean that you do not have COVID. However, you can choose to get tested, just to be safe that it is not COVID. "
                     )
                     print()
                     print(
                    "A quick reminder on how to stay safe during this pandemic: ")
                     print()
                     print(*d, sep="\n")
                     print()
                     code = "no";

                if (number >1):
                  print()
                  print(
                      "Since you seem to be having multiple symptoms, I recommend that you go get tested for COVID to be safe. Please Schedule an appointment with your medical professional to get tested just to be safe."
                  )
                  print();
                  print(
                    "A quick reminder on how to stay safe during this pandemic: " )
                  print()
                  print(*d, sep="\n")
                  print()
                  code = "no";

        if (answer2 == "yes" or answer2 == "maybe"):
            passcode = "yes"
            print()
            print(
                "Okay, Did you show any of these symptoms in the last 48 hours:"
            )
            print()
            print(*b, sep="\n")
            print()
            answer4 = input()
           
            if(answer4 == "no" and passcode == "yes"):
               print()
               print("Even though you do not show any of the symptoms, but you have come into contact with a person who has COVID-19, I suggest you get tested for COVID.");
               print();
               print("A quick reminder on how to keep yourself safe during this pandemic. ");
               code = "no";
            if (answer4 == "yes"):
              print()
              print(
                "How many of these symptoms did you face in the last 48 hours?"
            )
              print();
              number = input();
              number = int(number);
              if (number == 1 or number == 0):
                  if(passcode == "yes"):
                    print()
                    print(
                     "Even though you do not show any symptoms, you did come into contact with a person who has COVID. So I recommend that you get tested for COVID-19. "
                )
                    print()
                    print(
                    "A quick reminder on how to stay safe during this pandemic: "
                )
                    print()
                    print(*d, sep="\n")
                    print()
                    code = "no";
                  if(passcode =='no'):
                     print (
                    "You do not seem to be having multiple of these symptoms. This could mean that you do not have COVID. However, you can choose to get tested, just to be safe that it is not COVID. "
                     )
                     print()
                     print(
                    "A quick reminder on how to stay safe during this pandemic: ")
                     print()
                     print(*d, sep="\n")
                     print()
                     code = "no";

              if (number >1):
                if(passcode == "yes"):
                  print()
                  print(
                     "Since you seem to be having multiple symptoms and came in contact with a person who has COVID, I recommend you get tested for COVID. Please schedule for an appointment with your medical professional to get tested."
                )
                  print();
                  print(
                    "A quick reminder on how to stay safe during this pandemic: "
                )
                  print()
                  print(*d, sep="\n")
                  print()
                  code = "no";
                if(passcode == "no"):
                  print()
                  print(
                      "Since you seem to be having multiple symptoms, I recommend that you go get tested for COVID to be safe. Please Schedule an appointment with your medical professional to get tested just to be safe."
                  )
                  print();
                  print(
                    "A quick reminder on how to stay safe during this pandemic: " )
                  print()
                  print(*d, sep="\n")
                  print()
                  code = "no";
