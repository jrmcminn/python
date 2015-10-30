stopwords = ["about", "above", "above", "across", "after", "afterwards", "again", "against", "all", "almost", "alone",
             "along", "already", "also","although","always","am","among", "amongst", "amoungst", "amount",  "an", "and",
             "another", "any","anyhow","anyone","anything","anyway", "anywhere", "are", "around", "as",  "at", "back","be",
             "became", "because","become","becomes", "becoming", "been", "before", "beforehand", "behind", "being", "below",
             "beside", "besides", "between", "beyond", "bill", "both", "bottom","but", "by", "call", "can", "cannot", "cant",
             "co", "con", "could", "couldnt", "cry", "de", "describe", "detail", "do", "done", "down", "due", "during", "each",
             "eg", "eight", "either", "eleven","else", "elsewhere", "empty", "enough", "etc", "even", "ever", "every", "everyone",
             "everything", "everywhere", "except", "few", "fifteen", "fify", "fill", "find", "fire", "first", "five", "for",
             "former", "formerly", "forty", "found", "four", "from", "front", "full", "further", "get", "give", "go", "had",
             "has", "hasnt", "have", "he", "hence", "her", "here", "hereafter", "hereby", "herein", "hereupon", "hers", "herself",
             "him", "himself", "his", "how", "however", "hundred", "ie", "if", "in", "inc", "indeed", "interest", "into", "is",
             "it", "its", "itself", "keep", "last", "latter", "latterly", "least", "less", "ltd", "made", "many", "may", "me",
             "meanwhile", "might", "mill", "mine", "more", "moreover", "most", "mostly", "move", "much", "must", "my", "myself",
             "name", "namely", "neither", "never", "nevertheless", "next", "nine", "no", "nobody", "none", "noone", "nor", "not",
             "nothing", "now", "nowhere", "of", "off", "often", "on", "once", "one", "only", "onto", "or", "other", "others", "otherwise",
             "our", "ours", "ourselves", "out", "over", "own","part", "per", "perhaps", "please", "put", "rather", "re", "same", "see",
             "seem", "seemed", "seeming", "seems", "serious", "several", "she", "should", "show", "side", "since", "sincere", "six",
             "sixty", "so", "some", "somehow", "someone", "something", "sometime", "sometimes", "somewhere", "still", "such", "system",
             "take", "ten", "than", "that", "the", "their", "them", "themselves", "then", "thence", "there", "thereafter", "thereby",
             "therefore", "therein", "thereupon", "these", "they", "thickv", "thin", "third", "this", "those", "though", "three", "through",
             "throughout", "thru", "thus", "to", "together", "too", "top", "toward", "towards", "twelve", "twenty", "two", "un", "under", "until",
             "up", "upon", "us", "very", "via", "was", "we", "well", "were", "what", "whatever", "when", "whence", "whenever", "where", "whereafter",
             "whereas", "whereby", "wherein", "whereupon", "wherever", "whether", "which", "while", "whither", "who", "whoever", "whole", "whom",
             "whose", "why", "will", "with", "within", "without", "would", "yet", "you", "your", "yours", "yourself", "yourselves", "the", "hello",]

#def remove_stop_words(stopwordlist, stopwords):  #defining a new function called remove stopwords
        #if not stopwordlist: 
                #userswords = raw_input("what is your name: ")
                #stopwordlist = userwords.split() #splitting the userwords
        #stopword_list = []
        #for word in wordlist:
                #if word.lower() in stopwords:
                        #stopword_list.append('*') #this section is stating if and where a stopword is there, and if it needs to be appended or not
                #else:
                        #stopword_list.append(word)
        #return stopword_list 
        #stopword_list.join(sequence) 

#wordlist = "My name is jack?".split() #trying to split up this first sentence to throw away my name and is
#stopword_list = remove_stop_words(wordlist) 



fname=raw_input("Hello, what is your name?") #asking first question
fname=raw_input("Cool, nice to meet you " + fname) #returning the users name when they enter there name

print("I'm Jackbot, lets have a conversation")
inputString = raw_input("How old are you?")

age = int(inputString)
if((age <= 1) and (age <= 9)) : #if age is less than or equal to 1 and less than or equal to 9, print the response below. The response is based on what the user enters between the parameters that i have stated.
	print("Your a youngen")

if((age >= 11) and (age <= 19)):
	print("Your in your prime, go and party!")

if((age >=21) and (age <= 29)):
	print("At your age, you must live life to the fullest!")

if((age >= 31) and (age <= 39)):
	print("Any Gray hairs yet? haha")

if((age >= 41) and (age <= 49)):
	print("Your approaching the big 50, one of the best birthdays ever!")

if((age >= 51) and (age <= 59)):
	print("Take it chilled and relax, you deserve it at your age!")

if((age >= 61) and (age <= 69)):
	print("Welcome to the time of your life where you can do what you want and nobody can question it! haha")

if((age >= 71) and (age <= 79)):
	print("I bet you have seen a massive shift in technology since you've been alive!")

if((age >= 81) and (age <= 89)):
	print("approaching 90, you must take very good care of yourself")
	
if((age >= 91) and (age <= 99)):
	print("approaching 100, you can expect a letter from the queen soon! ")

if(age==10): #if the age is equal to 10 then it outputs a specific response. This is the same for the 10-100 birthdays
        print("10 years old, such a fun age.:)")
if(age==20):
        print("20 years old, great age for partying! Not far off the big 21st birthday, haha!")
if(age==30):
        print("30 years old is such a quality age! Hope you had a great 30th birthday party!:)")
if(age==40):
        print("40 years of age! I hope you had a great 40th birthday!:)")
if(age==50):
        print("50 years of age! The 50th birthday party must have been amazing! Hope you had a great day!:)")
if(age==60):
        print("60 years of age! Your now at the age where no-one can tell you what to do! Haha ;)")
if(age==70):
        print("70 years of age! Hope your having a fantastic retirement! :)")
if(age==80):
        print("80 years of age! Hope your healthy and well! :)")
if(age==90):
        print("90 years of age! You must look after yourself, hope your healthy and well! :)")
if(age==100):
        print("100 years of age! Thats a fantastic achievment, congratulations on your letter from the queen!:)")



fname=raw_input("Is the weather cold, warm or hot today?")
fname=raw_input("i see," + fname)

inputString = raw_input("What's the exact temprature today in celcuis (c)?")

weather = int(inputString)
if((weather >=1) and (weather <=4)):
        print("Oooh! Thats very cold, hot water bottle and thermals tonight!")

if((weather >=6) and (weather <=9)):
        print("pretty chilly today, keep the heating on!")

if((weather >=11) and (weather <=14)):
        print("Not a shorts day today! Haha!")

if((weather >=16) and (weather <=19)):
        print("Its getting warmer, good day for a trip out maybe.")

if((weather >=21) and (weather <=24)):
        print("Thats a good temprature! Make sure you make the most of it!")

if((weather >=26) and (weather <=29)):
        print("Thats is a good temprature! Make sure you put plenty of sun cream on")

if((weather >=31) and (weather <=34)):
        print("Oooh what a belter! Plenty of cold drinks today and maybe even a swim!")

if((weather >=36) and (weather <=39)):
        print("Wow! thats insanley hot, make sure to keep hydrated and out of the sun, you dont want to get sun stroke!")

if((weather >=41) and (weather <=44)):
        print("Wow, that is so hot! You need to wear plenty of suncream")

if((weather >=46) and (weather <=49)):
        print("Im shocked! That must be a new record!")

if((weather >=50) and (weather <=100)):
        print("any tempreture over 50 will be a new record my freind!")


if(weather==0): #if the weather is equal to 0 then it outputs a specific response. This is the same for temprature between 0-50 
        print("Thats so cold, remember to wrap up warm and wear gloves")
if(weather==5):
        print("Wow! 5 celcuis, a piping hot drink is in order")
if(weather==10):
        print("10 celcuis! Thats what i call a cold day, that type of weather calls for films and a warm blanket")
if(weather==15):
        print("15 celcuis is quite a cool day i would say")
if(weather==20):
        print("20 celcuis is a nice temprature, not to hot but not to cold. :)")
if(weather==25):
        print("25 celcuis, this type of weather calls for a picnic")
if(weather==30):
        print("30 celcuis, wow, time for a BBQ! Haha. :)")
if(weather==35):
        print("35 celcuis, a beautiful heat, remember to apply lots of suncream and wear your sunglasses")
if(weather==40):
        print("40 celcuis, that is one hot day! Remember to keep yourself hydrated, you dont want to get sun stroke")
if(weather==45):
        print("45 celcuis, thats ridicously hot, remember to stay in the shade, you dont want sun stroke")
if(weather==50):
        print("50 celcuis, wow, thats what i call a heatwave!")

fname=raw_input("Lovely speaking to you today, have a nice day") #ending the conversation


   

