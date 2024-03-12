import latextable as latextable
from texttable import Texttable
from Graph import Graph
import matplotlib.pyplot as plt
import numpy


class Test:

    def __init__(self, min_prob, max_prob, prob_step, min_graph_dim, max_graph_dim, dim_step, num_tests_per_graph=100):
        self._table = Texttable()
        self._table.set_cols_align(["c"] * 2)
        self._table.set_cols_dtype(['i', 'f'])
        self.min_prob = min_prob
        self.max_prob = max_prob
        self.prob_step = prob_step
        self.min_graph_dim = min_graph_dim
        self.max_graph_dim = max_graph_dim
        self.dim_step = dim_step
        self.num_tests_per_graph = num_tests_per_graph
        self.num_scc = []

    def process(self):
        for i in numpy.arange(self.min_prob, self.max_prob + self.prob_step, self.prob_step):
            sub_list = []
            for j in range(self.min_graph_dim, self.max_graph_dim + self.dim_step, self.dim_step):
                num_tot_scc = 0
                for k in range(self.num_tests_per_graph):
                    graph = Graph()
                    graph.random_v(j)
                    graph.random_adj(i/100)

                    graph.dfs()

                    transpose_graph = graph.get_transpose()

                    transpose_graph.dfs()

                    num_tot_scc = num_tot_scc + transpose_graph.get_scc()

                average_scc = num_tot_scc / self.num_tests_per_graph

                sub_list.append(average_scc)

            self.num_scc.append(sub_list)

    def build_size_invariant_table(self, dim):
        self._table.add_rows([["Probabilità", "Numero medio di CFC"]])
        values = [item[range(self.min_graph_dim, self.max_graph_dim + self.dim_step, self.dim_step).index(dim)] for item in self.num_scc]
        for i in numpy.arange(self.min_prob, self.max_prob + self.prob_step, self.prob_step):
            self._table.add_row(
                [str(i) + "\%", values[int((i - self.min_prob) / self.prob_step)]]
            )

    def print_size_invariant_table(self, dim):
        if dim in range(self.min_graph_dim, self.max_graph_dim + self.dim_step, self.dim_step):
            self.build_size_invariant_table(dim)
            print('\nTexttable Table dimensione ' + str(dim) + ':')
            print(self._table.draw())
            self.print_size_invariant_latex_code(dim)
            self.reset()
        else:
            print("errore nel print")

    def print_size_invariant_latex_code(self, dim):
        print('\nTexttable Latex dimensione ' + str(dim) + ':')
        print(latextable.draw_latex(self._table,
                                    caption="Numero di CFC al variare della probabilità di presenza di archi per grafi di dimensione di " + str(
                                        dim) + " nodi"))

    def build_probability_invariant_table(self, prob):
        self._table.add_rows([["Dimensione", "Numero medio di CFC"]])
        my_range = numpy.arange(self.min_prob, self.max_prob + self.prob_step, self.prob_step)
        values = self.num_scc[int(numpy.where(my_range == prob)[0])]
        for i in range(self.min_graph_dim, self.max_graph_dim + self.dim_step, self.dim_step):
            self._table.add_row(
                [str(i), str(values[int((i - self.min_graph_dim) / self.dim_step)])]
            )

    def print_probability_invariant_table(self, prob):
        if prob in numpy.arange(self.min_prob, self.max_prob + self.prob_step, self.prob_step):
            self.build_probability_invariant_table(prob)
            print('\nTexttable Table probabilità ' + str(prob) + '%:')
            print(self._table.draw())
            self.print_probability_invariant_latex_code(prob)
            self.reset()
        else:
            print("errore nel print")

    def print_probability_invariant_latex_code(self, prob):
        print('\nTexttable Latex probabilità ' + str(prob) + '%:')
        print(latextable.draw_latex(self._table,
                                    caption="Numero di CFC al variare del numero di nodi per grafi con probabilità di presenza di archi del " + str(
                                        prob) + "\%"))

    def plot_size_variant(self):

        abscissa_axis = []

        for i in range(self.min_graph_dim, self.max_graph_dim + self.dim_step, self.dim_step):
            abscissa_axis.append(i)

        for i in range(int((self.max_prob - self.min_prob + self.prob_step) / self.prob_step)):
            plt.plot(abscissa_axis, self.num_scc[i])

        plt.xlabel('dimensione')
        plt.ylabel('numero di CFC')
        #plt.title('SCC algorithm')
        plt.legend([(str(i) + "%") for i in numpy.arange(self.min_prob, self.max_prob + self.prob_step, self.prob_step)])

        plt.show()

    def plot_probability_variant(self):

        abscissa_axis = []

        for i in numpy.arange(self.min_prob, self.max_prob + self.prob_step, self.prob_step):
            abscissa_axis.append(i)

        for i in range(int((self.max_graph_dim - self.min_graph_dim + self.dim_step) / self.dim_step)):
            plt.plot(abscissa_axis, [row[i] for row in self.num_scc])

        plt.xlabel('probabilità di presenza di archi (in %)')
        plt.ylabel('numero di CFC')
        #plt.title('algoritmo SCC')
        plt.legend([(str(i) + " nodi") for i in range(self.min_graph_dim, self.max_graph_dim + self.dim_step, self.dim_step)])

        plt.show()

    def reset(self):
        self._table.reset()
        self._table.set_cols_align(["c"] * 2)
        self._table.set_cols_dtype(['i', 'f'])
