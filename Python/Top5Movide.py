movies = []
print("Enter your top 5 movie in order: ")
for i in range(1, 6):
    movie = input(f"{i}. ").strip().title()
    while movie == "":
        print("Blank is not accepted")
        movie = input()
    movies.append(movie)
ask = True
while ask == True:
    print("\nTop 5 Movie Menu")
    print("=================")
    print("1. See the top 5")
    print("2. Add a movie to the top 5")
    print("3. Quit program")
    select = input("Selection: ")
    check = True
    while check == True:
        try:
            select = int(select)
            if select > 3 or select < 1:
                print("Invalid selection. Please enter 1-3")
                select = input()
            else:
                check = False
        except ValueError:
            print("Invalid selection. Please enter 1-3")
            select = input()
    if select == 1:
        print("\nTop 5 Movies")
        print("============")
        for i in range(1, 6):
            print(f"{i}. {movies[i-1]}")
    elif select == 2:
        print("\nAdd movie")
        print("=========")
        add = input("Movie name: ").title().strip()
        while add == "":
            print("Sorry, the movie name cannot be blank. Please try again.")
            add = input()
        position = input("What position in the top 5 (0 to return to menu without adding): ")
        check = True
        while check == True:
            try:
                position = int(position)
                if position > 5 or position < 0:
                    print("Invalid position. Please enter 0-5")
                    position = input()
                else:
                    check = False
            except ValueError:
                print("Invalid position. Please enter 0-5")
                position = input()
        if position > 0:
            confirm = input(f"Warning! This will remove {movies[position-1]} from the top 5. Are you sure? (Y/N) ")
            while confirm.lower() != "y" and confirm.lower() != "n":
                print("Invalid answer. Please enter Y or N")
                confirm = input()
            if confirm.lower() == "y":
                movies.insert(position-1, add)
                movies.pop(position)
                print(f"Okay, {add} has been inserted into the top 5 in position {position}.")
    elif select == 3:
        print("Goodbye!")
        ask = False
