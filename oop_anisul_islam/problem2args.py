
def student_details(**details):
    print(details)
    try:
        roll = details['roll']
        class_no = details['class']
        name = details['name']
    except:
        pass
    try:
        print(roll, class_no, name)
    except UnboundLocalError:
        print("pass")
student_details(roll="100", class_no="11")    