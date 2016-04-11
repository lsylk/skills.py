# SOLUTIONS!

################################################################
# PART ONE


# 1. Write a function that does not take any arguments and
#    prints "Hello World".

def print_hello_world():
    print "Hello World"


# 2. Write a function that takes a name as a string and
#    prints "Hi" followed by the name.

def greeting_the_user(name):
    name = str(name)
    print "Hi %s" %name

# 3. Write a function that takes two integers and multiplies
#    them together. Print the result.

def multiply_numbers(num1, num2):
    result = num1 * num2
    print result

# 4. Write a function that takes a string and an integer and
#    prints the string that many times.

def print_string_n_time(string, n):
    print string * n

# 5. Write a function that takes an integer and prints "Higher
#    than 0" if higher than zero and "Lower than 0" if lower
#    than zero. If integer is 0 print "Zero".

def checking_range_of_n(n):
    if n > 0:
        print "Higher than zero"
    elif n < 0:
        print "Lower than zero"
    elif n == 0:
        print "Zero"

# 6. Write a function that takes an integer and returns a
#    boolean (True or False), depending on whether the number
#    is evenly divisible by 3.

def turning_int_into_boolean(num):
    num = int(num)
    if num%3 == 0:
        print True
    else:
        print False

# 7. Write a function that takes a sentence as one string and
#    returns the number of spaces.

def count_spaces(sentence):
    sentence = str(sentence)
    count = 0
    if 
    count += 1
    return count


# 8. Write a function that can be passed a meal price and a
#    tip percentage. It should return the total amount paid
#    (price + price * tip). **However:** passing in the tip
#    percentage should be optional; if not given, it should
#    default to 15%.

def meal_total_price(meal_price, tip_percentage=15):
    meal_price = float(meal_price)
    tip_percentage = (float(tip_percentage)/100)
    total_price = meal_price + (meal_price*tip_percentage)
    return total_price


# 9. Write a function that takes an integer as an argument and
#    returns two pieces of information as strings ---
#    "Positive" or "Negative" and "Even" or "Odd". The two strings
#	 should be returned in a list.

def type_of_integer(num):
    num = int(num)
    description_list = []
    if num > 0:
        description_list.append("Positive")
        if num%2 == 0:
            description_list.append("Even")
        elif num%2 != 0:
            description_list.append("Odd")
    elif num < 0:
        description_list.append("Negative")
        if num%2 == 0:
            description_list.append("Even")
        elif num%2 != 0:
            description_list.append("Odd")

    return description_list

#
# 	Then, write code that shows the calling of this function
# 	on a number and unpack what is returned into two
# 	variables --- sign and parity (whether it's positive
# 	or negative). Print sign and parity.


################################################################
# PART TWO


# 1. We have some code which is meant to calculate an item cost
#    by adding tax. Tax is normally 5% but it's higher in
#    California (7%).
#
#    Turn this into a function. Your function will pass in
#    the default tax amount (5%), a state abbreviaton, and the
#    default tax amount as parameters.
#    If the state is California, apply a 7% tax within the function.
#    Your function should return the total cost of the item including tax.

def total_price_of_item(item_price, state, tax=7):
    item_price = float(item_price)
    state = str(state).upper()
    if state != "CA":
        tax = 0.05
        total_price = item_price + (item_price*tax)
    else:
        tax = (float(tax)/100)
        total_price = item_price + (item_price*tax)
    return total_price

# 2. Turn the block of code from the directions into a function.
#	 Take a name and a job title as parameters, making it so the
# 	 job title defaults to "Engineer" if a job title is not passed in.
#	 Return the person's title and name.

def person_title(name, job_title="Engineer"):
    person_and_title = "%s, %s" %(job_title, name)
    return person_and_title


# 3. Given a receiver's name, receiver's job title, and sender's name, print the following letter:      
#       Dear JOB_TITLE RECEIVER_NAME, I think you are amazing! Sincerely,
#       SENDER_NAME. 
#    Use the function from #2 to construct the full title for the letter's greeting.

def print_letter(sender_name):
    def person_title(name, job_title):
        sender_name = str(senter_name).upper
    letter = "Dear " + person_and_title + ", I think you are amazing! Sincerely, %s" %sender_name

    return letter

# 4. Turn the block of code from the directions into a function. This
#    function will take a number and append it to *numbers*. It doesn't
#    need to return anything.

def append_number(num):
    num = int(num)
    num_list = []
    num_list.append(num)

    return None
