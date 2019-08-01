from random import randint


def main():
    while True:
        print('Select option; 1 for add movie, 2 for GIVE ME A SUGGESTION')
        selection = input()
        if selection == '1':
            with open('movies', 'a') as movies:
                print('Add a movie title: ')
                movie = input()
                movies.write(movie + '\n')
                print('Movie added')
        elif selection == '2':
            movies = open('movies', 'r')
            movie_list = movies.readlines()
            random_num = randint(0, len(movie_list) -1)
            print(movie_list[random_num])
            movies.close()
        else:
            print('Exiting...')
            exit

if __name__ == '__main__':
    main()
