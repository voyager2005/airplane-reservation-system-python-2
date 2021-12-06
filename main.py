from AirplaneReservationSystem import *
import time

# --------- DISPLAYING WELCOME ----------
display_welcome()

# ------- AAROGYA SETU APPLICATION ----------
# declaring a few global variables
response = ""
counter = 0
AaroyaSetu = False

text1 = "Please note that the information from this chat will be used " \
        " monitoring & management of the current health crisis "
text1_1 = "and research in the fight against COVID-19"
text2 = "Please answer with a yes/no"

text3 = "Are you experiencing any of the following symptoms? "  # paragraph 2
text3_1 = "Cough, Fever, Difficulty in breathing, loss of senses and taste"

text4 = "Have you ever had any of the following: "  # paragraph 3
text4_1 = "Diabetes, Hypertension, Lung disease, Heart Disease, Kidney Disorder"

text5 = "Have you travelled anywhere internationally in the last 28-45 days?"  # paragraph 4

text6 = "Do any of the following apply to you?"
text6_1 = "I have recently interacted or lived with someone who has tested positive for COVID -19 "  # paragraph 5
text6_2 = "I am a healthcare worker and I examined a COVID-19 confirmed case without protective gear"

allocatedParagraphs = [text1, text1_1, text2, text3, text3_1, text4, text4_1, text5, text6, text6_1, text6_2]
paragraphNumber = 0

while paragraphNumber < len(allocatedParagraphs):
    currentParagraph = allocatedParagraphs[paragraphNumber]
    i = 0

    for j in range(len(currentParagraph)):
        ch = currentParagraph[i]
        print(ch, end="")
        i = i + 1
        time.sleep(0)

    if paragraphNumber == 2 or paragraphNumber == 4 or paragraphNumber == 6 or paragraphNumber == 7 or paragraphNumber == 10:
        if paragraphNumber == 2:
            print("", end="\n")
        else:
            userResponse = input("\n")
            if userResponse == "yes":
                counter = counter + 1

    paragraphNumber = paragraphNumber + 1
    print("", end="\n")

if counter >= 1:
    print("You have moderate chances of contracting the the COVID-19 virus \n"
          "we would advice you to stay at home, wear a mask and isolate yourself for the next 7-14 days")
    AaroyaSetu = False
else:
    print("There is little to no chance that you have contracted the virus based on the information "
          "provided but we require you to produce a COVID-19 negative result 78 hours before your flight")
    AaroyaSetu = True

# ----- AIRPLANE SEAT RESERVATION -----
if AaroyaSetu:
    constant_details()
    display_aeroplane_seat()
