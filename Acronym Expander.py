# Ari Evans
# Acronym Expander, expand out the acronyms in a given string
# Will translate anywhere it sees the letters, haha! egg turns into egood game.

ChatAcronyms  = {"lol": "laugh out loud", 
                 "dw": "don't worry", 
                 "hf": "have fun", 
                 "gg": "good game", 
                 "brb": "be right back", 
                 "g2g": "got to go", 
                 "wtf": "what the fuck", 
                 "wp": "well played", 
                 "gl": "good luck", 
                 "imo": "in my opinion"}

while True:
    raw_input = input("Enter a string you want the acronyms expanded in: ")
    for item in range(len(ChatAcronyms)):
        if list(ChatAcronyms)[item] in raw_input:
            raw_input = raw_input.replace(list(ChatAcronyms)[item], ChatAcronyms[list(ChatAcronyms)[item]])
    print("Translated string:\n"+raw_input+"\n")