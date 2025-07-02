
"""
converts celsius to fahrenheit
"""
def cel2fah(c):
    return (c * 9 / 5) + 32

"""
converts fahrenheit to celsius
"""
def fah2cel(f):
    return 5/9 * (f - 32)

"""
converts kilometers to miles
"""
def km2mi(km):
    return km / 1.60934

"""
converts miles to kilometers
"""
def mi2km(mi):
    return mi * 1.60934


if __name__ == "__main__":

    for c in range(0, 21, 5):
        f = round(cel2fah(c))
        print(f"{c} C is {f} F")

    print()
    for f in range(20, 41, 5):
        c = round(fah2cel(f))
        print(f"{f} F is {c} C")

    print()
    for km in range(1, 6):
        mi = round(km2mi(km), 1)
        print(f"{km} km is {mi} mi")

    print()
    for mi in range(5, 10):
        km = round(mi2km(mi), 1)
        print(f"{mi} mi is {km} km")
