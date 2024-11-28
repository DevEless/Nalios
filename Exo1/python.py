#Ex 1: FizzBuzz
# - Write a function that outputs numbers from 1 to 100 inclusive.
# - If the number is a multiple of 3, print 'Fizz' instead
# - If the number is a multiple of 5, print 'Buzz' instead
# - If the number is a multiple of 3 AND 5, print 'FizzBuzz' instead
# - Bonus point: make your function accept a dict parameter containing multiple: word to
# output. So the program above would be
# yourfunction({
# '3': 'Fizz',
# '5':'Buzz',
# })
# But we could totally send you
# yourfunction({
# '4': 'Fizz',
# '9': 'Buzz',
# '12': 'Lazz'
# })



def FizzOrBuzz(start=1, end=100):
#En param de la fonction il y a , le chiffre de départ et le nombre de fin donc on va parcourir les nombres de 1 a 100
    for num in range(start, end +1):
        #Je boucle sur les nombre se trouvant entre start et end grace a la methode range()
        if num % 3 == 0 and num % 5 ==0:
            #condition qui vérifie grace a un modulo si le nombre est divisible par trois et 5
            print("FizzBuzz")
        elif num % 3 == 0:
            #vérifie si le nombre est divisible seulement par trois
            print("Fizz")
        elif num % 5 == 0:
            #idem mais par 5
            print("Buzz")
        else:
            #je print les nombre un par un grace a ma boucle
            print(num)

FizzOrBuzz()
#Lancement de ma fonction


#Bonus

