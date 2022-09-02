num_students = int(input("Enter number of students: "))
weights_lbs = []
for i in range(num_students):
    while True:
        try:
            weight = input("Weight of {0} student".format(i + 1))
            weight = float(weight)
            weights_lbs.append(weight)
            break
        except Exception:
            print("invalid weight, enter again.")
weights_kgs = [0.453592 * w for w in weights_lbs]
print("weight in kgs: ", weights_kgs)