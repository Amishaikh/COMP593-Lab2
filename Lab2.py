def main():

    #: Step 2 - Create a complex data structure
    about_me = {
        'full_name'      : 'Amir Shaikh',
        'student_id'     :  102356554,
        'pizza_toppings' : [
            'CHEESE',
            'CHICKEN',
            'BACON'
        ],
        'movies' :[
            {'title' : 'Avengers : End game',
            'genre' : 'Action'},
            {'title' : 'Dune',
             'genre' : 'Sci-Fi'},

        ] 
    }
    

    #: Step 3 - Add another movie to the data structure
    about_me['movies'].append({'title' : 'The Jungle Book',
                               'genre' : 'Fiction'})
    print_student_name_and_id(about_me)

    #Printing pizza toppings in bullet points and adding toppings and printing in bullet points  
    print_pizza_toppings(about_me)
    about_me = add_pizza_toppings(about_me, ('Onions', 'Black Olives', 'Mushrooms', 'peppers'))
    print_pizza_toppings(about_me) 

    # Printing movie genres and titles
    print_movie_genres(about_me)
    print_movie_titles(about_me['movies'])

    return
    

#: Step 4 - Function that prints student name and ID	
def print_student_name_and_id(name_id):
    full_name  = name_id['full_name']
    first_name = (full_name.split(' ')[0])
    student_id = name_id['student_id']

    print(f'My name is {full_name}, but you can call me Sir {first_name}.')

    print(f'My student ID is {student_id}.\n')

    return
    
# : Step 5 - Function that adds pizza toppings to data structure
def add_pizza_toppings(data_stru, toppings):
    data_stru['pizza_toppings'].extend(toppings)
    data_stru['pizza_toppings'] = sorted([topping.lower() for topping in data_stru["pizza_toppings"]])

    return data_stru

#: Step 6 - Function that prints bullet list of pizza toppings
def print_pizza_toppings(data_stru):
    print("My favourite pizza toppings are:")
    for topping in data_stru["pizza_toppings"]:
        print(f"- {topping}")
    print()

    return

#: Step 7 - Function that prints comma-separated list of movie genres
def print_movie_genres(data_stru):
    genres = [movie['genre'] for movie in data_stru['movies']]
    print("I like to watch " + ", ".join(genres) + " movies.")
    

#: Step 8 - Function that prints comma-separated list of movie titles
def print_movie_titles(movie_list):
    titles = [movie['title'].title() for movie in movie_list]

#Bonus Part.
    #using if command to print 'and' after 2 titles.
    if len(titles) > 1:
        #if len > 1 then adding 'and' before last title.
        titles[-1] = 'and ' + titles[-1]

    print("Some of my favourite movies are " + ", ".join(titles) + "!\n")
    
if __name__ == '__main__':
    main()