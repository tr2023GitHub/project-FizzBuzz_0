# ----- Test 1 for mentor Hexlet--------------
# Ask user to input number, if number is 0 stop print number
#print(" Welcome to Fizz Buzz!\n Submit a number and get an answer!")
#print ("Ask user to input number, if number is 0 stop print number")
#number=input ("Input Number:")
import click
@click.command()
@click.option('--count', default=1, help='Number of greetings.')
@click.option('--number', prompt='Your Number', help='Your Number to analyse')
def FIZZBUZZ(count,number):
    """Приветствует ИМЯ (`number`), несколько (`count`) раз."""
    for x in range(count):
        click.echo(f"Number: {number}!")
        n = int(number)
        while n != 0:
            match n:
                case n if (n % 3 == 0 and n % 5 == 0):
                    print("FizzBuzz")
                case n if (n % 3 == 0 and n % 5 != 0):
                    print("Fizz")
                case n if (n % 5 == 0 and n % 3 != 0):
                    print("Buzz")
                case _:
                    print(n)
            number = input("Input Number:")
            n = int(number)
        print(f"Stop, as Number:{n} ")

if __name__ == '__main__':
    FIZZBUZZ()

