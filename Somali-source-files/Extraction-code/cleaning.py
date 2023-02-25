
import time
alphabet = "efghijklmnoqrstuwxy"
def shrink(file, char):
    # Reads the file and only extract content that start withe the desired letter.
    with open(file, "r") as raw_file:
        lines = raw_file.readlines()
    container = []
    for line in lines:
        if line[0] == char:
            inner = line.split(" ")
            if inner[0].isalpha():
                container.append(inner[0])
            elif inner[0][-1] == "¹":
                container.append(inner[0][:-1])
                
    return container


def write_to_file(container, char):
    with open("dictionary-words/"+char+".txt", "a") as file:
        for word in container:
            file.write(word+"\n")
    print("writen to: " + char + ".txt", "numbers of workds: " + str(len(container)))
    
def tokenizer(container):
    tokens = {word for word in container}
    return tokens


###### Uncomment this to write to words to their respective file

# for letter in alphabet:
#     container = shrink("../disposable/"+letter+"-raw.txt", letter)
#     tokens = tokenizer(container)
#     write_to_file(tokens, letter)
#     time.sleep(3)

