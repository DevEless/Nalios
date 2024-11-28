# Nalios


You have 2 hours to do your first push in Git with what has been done.
Important note : please try to be honest with the timing. You can still push
afterwards if you want to.
- If no precision is given, use Python 3 to answer these exercises.
- Take your time, breath, you can do the questions in any order.
- If you don't know a full solution, you can explain what you wanted to do. Your logic will
be taken into account.
- Do Bonus points of exercises once you finish everything, don't lose time on it.
- import this - if you know you know, else you'll know
Ex 1: FizzBuzz
- Write a function that outputs numbers from 1 to 100 inclusive.
- If the number is a multiple of 3, print 'Fizz' instead
- If the number is a multiple of 5, print 'Buzz' instead
- If the number is a multiple of 3 AND 5, print 'FizzBuzz' instead
- Bonus point: make your function accept a dict parameter containing multiple: word to
output. So the program above would be
yourfunction({
'3': 'Fizz',
'5':'Buzz',
})
But we could totally send you
yourfunction({
'4': 'Fizz',
'9': 'Buzz',
'12': 'Lazz'
})

Ex 2: Game of Life
- Do you know the game of life ? You can find the rules here :
https://playgameoflife.com (bottom left, Explanation, or if you need more precision, ask
Google)
- Write a function that accepts a matrix in parameter and runs the Game of Life on it.
- Return the matrix after 5 iteration of the Game of Life.
- Bonus point: Just before returning the matrix, output it's result in HTML (don't need
CSS, ugly stuff working is good)
Ex 3: Hello, Nalios !
- In JavaScript, create a function that outputs "Hello, Nalios !"
- You can't use strings.
Ex 4: PSQL
- Write pseudo-SQL statements to create database tables to store the products of a basic
webshop. Each product has a name, a price, a creation date and may belong to several
categories. Categories have a name and a flag to indicate whether the category is
private or public.

- Write a SQL query to find the list of products that belong to more than 5 public
categories
Ex 5: MySum
- Write a function that takes an array of numbers in parameter (no joke : no None, no
strings, only real numbers)
- Output the sum of these number, without using the sum() function.
- Bonus Point: Use recursion to get this sum