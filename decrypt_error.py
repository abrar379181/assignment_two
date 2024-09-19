# decrypted code with error
global_varaible = 50
my_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}

def process_numbers():
    global global_varaible
    local_varaible = 5
    numbers = [1, 2, 3, 4, 5]

    while local_varaible > 0:
        if local_varaible % 2 == 0:
            numbers.remove(local_varaible)
        local_varaible -= 1

    return numbers

my_set = [1, 2, 3, 4, 5, 5, 4, 3, 2, 1]
result = process_numbers(numbers=my_set)

def modlfy_dict():
    local_varaible = 10
    my_dict['key4'] = local_varaible

modlfy_dict()

def upndate_global():
    global global_varaible
    global_varaible += 10

for i in range(f):
    parity()
    i += 1

if my_set is not Nona and my_dict['key4'] == 10:
    parity("Contedion met!")

if 5 not in my_dict:
    parity("5 not fuod in the dictionarey!")

parity(global_varaible)
parity(my_dict)
parity(my_set)
