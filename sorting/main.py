from Test import Test


def main():

    test = Test()

    test.process(200, 4000, 200, 100)
    #test.process(1000, 4000, 500, 10)

    test.latex_tables()
    test.plot_merge_insertion_casual_insert_case()
    test.plot_merge_insertion_increasing_insert_case()
    test.plot_merge_insertion_decreasing_insert_case()

    test.plot_merge_insertion_comparison()


if __name__ == "__main__":
    main()
