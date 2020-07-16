def mod_inverse(a, m):
    '''
    Function which calculates the inverse modulo of a in base m
    This is the naive approach which iterates through all the numbers 0 to m-1
    :param a: the number for which the inverse will be determined
    :param m: the base in which the inverse will be computed
    :return: Integer denoting the inverse modulo of a, if it exists
             None, otherwise
    '''
    a = a % m
    for i in range(m):
        if (a * i) % m == 1:
            return i
    return None


def parse_equation(eq):
    '''
    Function which transform the equation input in a pair of the form (remainder, base module)
    :param eq: string of the form x = k mod m where k and m are numbers
    :return: pair of the form (remainder, base module)
    '''
    eq = eq.strip('\n').strip().split('=')[1]
    eq = eq.strip().split('mod')
    for i in range(len(eq)):
        eq[i] = eq[i].strip()
        eq[i] = int(eq[i])
    return eq


def read_equations():
    '''
    Function which reads the equations from the user
    :return: list of congruences represented as pairs of the form (remainder, base module)
    '''
    equations = []
    eq = input("Give me a congruence (press 0 to stop): ")
    while eq != '0':
        equations.append(parse_equation(eq))
        eq = input("Give me a congruence (press 0 to stop): ")
    return equations


def gcd(x, y):
    '''
    Function which calculates the gcd of 2 numbers
    Euler's algorithm
    :param x: Integer - first number
    :param y: Integer - second number
    :return: Integer - the gcd of the 2 numbers
    '''
    while y:
        x, y = y, x % y

    return x


def solve_system(equations):
    '''
    Function which solves a system of congruences
    :param equations: list of congruences represented as pairs of the form (remainder, base module)
    :return: x - the solution of the system, m - the base in which was calculated
    '''

    for i in range(len(equations)):
        for j in range(i+1, len(equations)):
            if gcd(equations[i][1], equations[j][1]) != 1:
                print("These 2 moduli are not coprime: " + str(equations[i][1]) + " " + str(equations[j][1]))
                return None, None

    m = 1

    # calculate m = m1 * m2 * m3 * ... * mn
    for i in equations:
        m *= i[1]
    ms = []

    # calculate m / mi, i=1..n and keep them in a list
    for i in equations:
        ms.append(int(m / i[1]))
    inverses = []

    # calculate ai = (m / mi)^(-1) mod mi
    for i in range(len(equations)):
        inverses.append(mod_inverse(ms[i], equations[i][1]))
    x = 0

    # calculate x = b1 * (m / m1) * a1 + ... + bn * (m / mn) * an where bi, i = 1..n are the modulo remainders
    for i in range(len(equations)):
        x += equations[i][0] * ms[i] * inverses[i]
    return x % m, m


def print_menu():
    '''
    Function which prints the menu
    '''
    print("1. Give equations ")
    print("2. Solve system ")
    print("0. Exit")


def main():
    ok = True
    equations = []
    while ok:
        print_menu()
        option = input("Give an option: ")
        if option == '1':
            equations = read_equations()
        elif option == '2':
            if len(equations) != 0:
                x, m = solve_system(equations)
                if x is not None and m is not None:
                    print("x = " + str(x) + " mod " + str(m))
            else:
                print("Give me a system!")
        elif option == '0':
            ok = False
        else:
            print("No such option!")


print(gcd(247, 7163))
main()
