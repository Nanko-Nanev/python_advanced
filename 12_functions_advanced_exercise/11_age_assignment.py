def age_assignment(*names, **kwargs):
    name_age = {}
    for name in names:
        for age in kwargs.items():
            if name[0] == age[0]:
                name_age[name] = age[1]

    return name_age


print(age_assignment("Peter", "George", G=26, P=19))

print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))