import sys
from Test import *
sys.setrecursionlimit(10000)


def main():

    #test = Test(min_prob=0, max_prob=50, prob_step=5, min_graph_dim=3, max_graph_dim=30, dim_step=3)
    test = Test(min_prob=5, max_prob=5, prob_step=5, min_graph_dim=10, max_graph_dim=300, dim_step=10)

    test.process()

    test.print_probability_invariant_table(5)
    test.plot_size_variant()


if __name__ == "__main__":
    main()
