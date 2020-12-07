# customs form


def get_input(filename):
    forms = []
    form = []
    with open(filename) as fil:
        lines = fil.readlines()
        for line in lines:
            if line != '\n':
                form.append(line.strip())
            if line == '\n' and form != '':
                forms.append(form)
                form = []
    return forms


def count_yes_each(form):
    return len(set(''.join(form)))


def count_yes_all(form):
    s = set(form[0])
    for ele in form:
        s = s.intersection(set(ele))
    return len(s)


def total_yes(forms):
    total = 0
    for form in forms:
        total += count_yes_all(form)
    return total


forms = get_input('aoc6_input.txt')
print(total_yes(forms))


