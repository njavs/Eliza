import re
import random

eliza_says = "Hi, I'm Eliza. What brings you here today?"

# History structure to store user's inputs to reference later
history = []
historyCount = 0

# Randomly generated canned responses to "Yes"
def respond_to_yes():
    responseNum = str(random.randint(1,5))

    eliza_says = {
        '1': "I see. Tell me more...",
        '2': "Is that so?",
        '3': "Interesting. Tell me more...",
        '4': "Go on.",
        '5': "Why do you think that is?"
    } [responseNum]

    return eliza_says

# Randomly generated canned responses to "No"
def respond_to_no():
    responseNum = str(random.randint(1,5))

    eliza_says = {
        '1': "Why not?",
        '2': "No? Why not?",
        '3': "Can you explain to me why not?",
        '4': "No? Tell me more...",
        '5': "Why do you think not?"
    } [responseNum]

    return eliza_says

# Randomly generated canned responses to "I am _(so)_ and _(so)_"
def i_am_response(user_input):
    responseNum = str(random.randint(1,3))
    a = re.search("(\\bam\\b | \\b'm\\b)", user_input)
    adjs = user_input[a.end():]

    # Regex-modify the input string
    user_input = re.sub('\\bmy\\b', "your", user_input, 0, 0)
    user_input = re.sub("^My\\b", "Your", user_input, 0, 0)
    user_input = re.sub("^I\\b", "You", user_input, 0, 0)
    user_input = re.sub("\\bI\\b", "you", user_input, 0, 0)
    user_input = re.sub("\\bam\\b", "are", user_input, 0, 0)
    user_input = re.sub("\\bme\\b", "you", user_input, 0, 0)
    user_input = re.sub("\\bwe\\b", "you", user_input, 0, 0)
    user_input = re.sub("^We\\b", "You", user_input, 0, 0)

    eliza_says = {
        '1': "Did you come to me because you believe you are " + adjs + "?",
        '2': "Why do you think that you are" + adjs + "?",
        '3': user_input + "?"
    } [responseNum]

    return eliza_says

# Randomly generated canned responses to Category-Less inputs
def misc_response(user_input):
    responseNum = str(random.randint(1,5))
    historyNum = random.randint(0,historyCount-1)
    adjectiveNum = random.randint(0, 2)
    adjectives = [" ", ", interesting...", ", okay..."]

    ui = ""
    count = 0
    for c in user_input:
        count = count + 1
        # Don't add period
        if count is len(user_input) and c is '.':
            continue
        ui += c

    eliza_says = {
        '1': "I see. Can you elaborate for me?",
        '2': "Tell me more...",
        '3': "Go on...",
        '4': "Hmm" + adjectives[adjectiveNum] + " \"" + history[historyNum] + "\" Can you tell me a bit more about that?",
        '5': ui + "?"
    } [responseNum]

    return eliza_says

# Main script
while True:
    user_input = raw_input(eliza_says + "\n")
    history.append(user_input)
    historyCount = historyCount + 1

    # Canned responses
    if (str.lower(user_input).find("yes") != -1) or (str.lower(user_input).find("yeah") != -1):
        eliza_says = respond_to_yes()
        continue

    if (str.lower(user_input).find(" no ") != -1) or (str.lower(user_input).find(" nah ") != -1):
        eliza_says = respond_to_no()
        continue

    if (str.lower(user_input).find("i don't know") != -1) or (str.lower(user_input).find("i have no idea") != -1):
        eliza_says = "What makes you think you don't know?"
        continue

    elif (str.lower(user_input).find("always") != -1):
        eliza_says = "Can you think of a specific example?"
        continue

    elif (str.lower(user_input).find("never") != -1):
        eliza_says = "Never?"
        continue

    elif (str.lower(user_input).find("died") != -1):
        eliza_says = "I see. Tell me more."
        continue

    elif (str.lower(user_input).find("sorry") != -1):
        eliza_says = "No need to apologize. Go on."
        continue

    elif (user_input[len(user_input) - 1] == "?"):
        eliza_says = "I'm afraid I'm not here to answer questions. I can only help you answer them yourself."
        continue

    # Regex-modified responses
    eliza_says = re.sub('\\bmy\\b', "your", user_input, 0, 0)
    eliza_says = re.sub("^My\\b", "Your", eliza_says, 0, 0)
    eliza_says = re.sub("^I\\b", "You", eliza_says, 0, 0)
    eliza_says = re.sub("\\bI\\b", "you", eliza_says, 0, 0)
    eliza_says = re.sub("\\bam\\b", "are", eliza_says, 0, 0)
    eliza_says = re.sub("\\bme\\b", "you", eliza_says, 0, 0)
    eliza_says = re.sub("\\bwe\\b", "you", eliza_says, 0, 0)
    eliza_says = re.sub("^We\\b", "You", eliza_says, 0, 0)

    if (str.lower(user_input).find(" am ") != -1):
        eliza_says = i_am_response(user_input)
        continue

    eliza_says = misc_response(eliza_says)