from Test import Test
import sys

sys.setrecursionlimit(15000)


def main():

    test = Test(20, 500, 20)
    #test = Test(5, 25, 5)

    test.process_ordered_test()
    test.process_unordered_test()

    test.print_ordered_insert_table()
    test.print_unordered_insert_table()
    test.print_ordered_search_table()
    test.print_unordered_search_table()

    test.plot_ordered_insert()
    test.show_plot()

    test.plot_unordered_insert()
    test.show_plot()

    test.plot_ordered_search()
    test.show_plot()

    test.plot_unordered_search()
    test.show_plot()


if __name__ == "__main__":
    main()
