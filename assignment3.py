import random

movies = [
    "manichitrathazhu",
    "drishyam",
    "drishyam 2",
    "premam",
    "lucifer",
    "empuraan",
    "bhoothakaalam",
    "kumbalangi nights",
    "bangalore days",
    "ustad hotel",
    "traffic",
    "ambili",
    "thondimuthalum driksakshiyum",
    "maheshinte prathikaaram",
    "virus",
    "take off",
    "uyare",
    "helen",
    "android kunjappan",
    "jan e man",
    "home",
    "jaya jaya jaya jaya hey",
    "romancham",
    "aavesham",
    "premalu",
    "neru",
    "2018",
    "the great indian kitchen",
    "joji",
    "nayattu",
    "malik",
    "kappela",
    "kurup",
    "minnal murali",
    "pathaanam",
    "comrade in america",
    "charlie",
    "annayum rasoolum",
    "ustad hotel",
    "salt n pepper",
    "22 female kottayam",
    "diamond necklace",
    "thattathin marayathu",
    "vikruthi",
    "sufiyum sujathayum",
    "thinkalazhcha nischayam",
    "super sharanya",
    "operation java",
    "aarkkariyam",
    "kuttavum shikshayum",
    "undha",
    "pathemari",
    "perumthachan",
    "spadikam",
    "commissioner",
    "king",
    "rajamanikyam",
    "chotta mumbai",
    "classmates",
    "meesha madhavan",
    "naran",
    "rasathanthram",
    "kannur squad",
    "aadu",
    "aadu 2",
    "amar akbar anthony",
    "oru vadakkan selfie",
    "thanneer mathan dinangal",
    "super deluxe",
    "premalu",
    "romancham",
    "falimy",
    "mukundan unni associates",
    "thallumaala",
    "jana gana mana",
    "malayankunju",
    "turbo",
    "aavesham",
    "kishkindha kaandam",
    "anweshippin kandethum",
    "kannur squad",
    "kaathal",
    "nanpakal nerathu mayakkam",
    "purusha pretham",
    "sulaikha manzil",
    "madhuram",
    "joji",
    "cu soon",
    "forensic",
    "ezra",
    "varathan",
    "iyobinte pusthakam",
    "munthirivallikal thalirkkumbol",
    "action hero biju",
    "thamaasha",
    "thinkalazhcha nischayam"
]

movie = random.choice(movies)

guessed = ""
chances = 7
name_chances = 2

while chances > 0:
    for i in movie:
        if i in guessed:
            print(i, end=" ")
        else:
            print("_", end=" ")
    print()
    choice = input("Enter the letter or movie name: ").lower()
    if len(choice) > 1:
        if choice == movie:
            print("You Win!")
            break
        else:
            name_chances = name_chances - 1
            print("Wrong movie name")
            print("Guess Movie name chances remaining:-", name_chances)
            if name_chances == 0:
                print("You Lose!")
                print("Movie was:", movie)
                break
    else:
        if choice in movie:
            guessed = guessed + choice
            print("Correct!")
        else:
            chances = chances - 1
            print("Wrong letter")
            print("Remaining Chances:", chances)
    complete = True

    for i in movie:
        if i not in guessed:
            complete = False

    if complete:
        print("You Win!")
        print("Movie:", movie)
        break