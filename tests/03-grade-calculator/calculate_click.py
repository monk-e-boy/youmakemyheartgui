

mark_string = i.text

result = ""

if mark_string == "":
    result = "Error."
else:
    mark = int(mark_string)
    
    if mark < 20:
        result = "Sorry, that's a fail"
    elif mark < 40:
        result = "Pass"
    # TODO put the rest of the checks here


print(result)
msg.text = "Grade: " + result