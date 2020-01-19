# So next time you get a parsing question, one of your first thoughts should be "use a stack!"

# In this problem, we can realize our stack would only hold '(' characters. So instead of storing each of those characters in a stack, we can store the number of items our stack would be holding.


def parantheticals(input_string, input_index):
    count = 0
    result = ""
    for i in range(input_index, len(input_string)):
        if(input_string[i] == "("):
            count += 1
            if(count == 0):
                result = i
                break
        elif(input_string[i] == ")"):
            count -= 1
            if(count == 0):
                result = i
                break
        else:
            continue
    return result


print(parantheticals("Sometimes (when I nest them (my parentheticals) too much (like this (and this))) they get confusing", 10))

print(parantheticals("That gets us from O(n)O(n) space to O(1)O(1) space.", 21))
