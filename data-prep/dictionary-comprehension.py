import random

# Key: word, value: character count
# Example list with random sentences (from https://randomwordgenerator.com/sentence.php):
sentences = ["The chic gangster liked to start the day with a pink scarf.", "The wooden spoon couldn’t cut but left emotional scars.", 
             "Tomatoes make great weapons when water balloons aren’t available.", "Weather is not trivial - it's especially important when you're standing in it.",
             "Getting up at dawn is for the birds.", "I just wanted to tell you I could see the love you have for your child by the way you look at her.",
             "The delicious aroma from the kitchen was ruined by cigarette smoke.", "Bill ran from the giraffe toward the dolphin.", "The crowd yells and screams for more memes.",
             "Mothers spend months of their lives waiting on their children.", "Gwen had her best sleep ever on her new bed of nails.", 
             "We're careful about orange ping pong balls because people might think they're fruit.", "I'd rather be a bird than a fish.",
             "He picked up trash in his spare time to dump in his neighbor's yard.", "For the 216th time, he said he would quit drinking soda after this last Coke.", 
             "When he asked her favorite number, she answered without hesitation that it was diamonds.", "With a single flip of the coin, his life changed forever.",
             "You'll see the rainbow bridge after it rains cats and dogs.", "He didn't understand why the bird wanted to ride the bicycle."]

#Random choice:
sentence = random.choice(sentences)

#Create dictionary
dict = {item:len(item) for item in sentence.split()}

print(dict)

# Change code as needed!
