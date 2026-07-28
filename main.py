"""Interactive command-line program for Add2Num."""

from my_big_number import MyBigNumber


def main(stn1=None, stn2=None, show_steps=False):
    """Run the CLI and return the calculated sum."""
    if stn1 is None:
        stn1 = input("First number: ")
    if stn2 is None:
        stn2 = input("Second number: ")

    result = MyBigNumber(show_steps).sum(stn1, stn2)
    print(result)
    return result


if __name__ == "__main__":
    main()
