import random
from timeit import default_timer as timer

import matplotlib.pyplot as plt

from BST import BST
from RBT import RBT

import latextable as latextable
from texttable import Texttable


class Test:

    def __init__(self, min_dim, max_dim, dim_step, num_tests_per_dim=100):
        self.ordered_case_bst_insert_time = []
        self.ordered_case_rbt_insert_time = []

        self.ordered_case_bst_height = []
        self.ordered_case_rbt_height = []
        self.unordered_case_bst_height = []
        self.unordered_case_rbt_height = []

        self.ordered_case_bst_search_time = []
        self.ordered_case_rbt_search_time = []

        self.unordered_case_bst_insert_time = []
        self.unordered_case_rbt_insert_time = []

        self.unordered_case_bst_search_time = []
        self.unordered_case_rbt_search_time = []

        self.min_dim = min_dim
        self.max_dim = max_dim
        self.dim_step = dim_step
        self.num_tests_per_dim = num_tests_per_dim

        self._table = Texttable()
        self._table.set_cols_align(["c"] * 5)
        self._table.set_cols_dtype(['i', 'e', 'f', 'e', 'f'])
        self.plt = plt

    def process_ordered_test(self):

        for i in range(self.min_dim, self.max_dim + self.dim_step, self.dim_step):

            insert_bst_time = 0
            insert_rbt_time = 0
            search_bst_time = 0
            search_rbt_time = 0
            bst_height = 0
            rbt_height = 0

            for k in range(self.num_tests_per_dim):

                ordered_case_bst = BST()

                ordered_case_rbt = RBT()

                bst_start = timer()

                for j in range(i):
                    ordered_case_bst.insert(j)

                bst_end = timer()

                rbt_start = timer()

                for j in range(i):
                    ordered_case_rbt.insert(j)

                rbt_end = timer()

                insert_bst_time = insert_bst_time + bst_end - bst_start
                insert_rbt_time = insert_rbt_time + rbt_end - rbt_start

                bst_start = timer()

                for j in range(i):
                    ordered_case_bst.find(j)

                bst_end = timer()

                rbt_start = timer()

                for j in range(i):
                    ordered_case_rbt.find(j)

                rbt_end = timer()

                search_bst_time = search_bst_time + bst_end - bst_start
                search_rbt_time = search_rbt_time + rbt_end - rbt_start

                bst_height = bst_height + ordered_case_bst.get_height()
                rbt_height = rbt_height + ordered_case_rbt.get_height()

            self.ordered_case_bst_insert_time.append(
                insert_bst_time / self.num_tests_per_dim)  # si deve mettere il tempo di inserimento di tutti i valori o il tempo
            self.ordered_case_rbt_insert_time.append(
                (insert_rbt_time / self.num_tests_per_dim))  # di inserimento medio di ogni valore (nel caso della seconda dividi per il numero di nodi)

            self.ordered_case_bst_search_time.append(
                search_bst_time / self.num_tests_per_dim)  # si deve mettere il tempo di ricerca di tutti i valori o il tempo
            self.ordered_case_rbt_search_time.append(
                search_rbt_time / self.num_tests_per_dim)  # di ricerca medio di ogni valore (nel caso della prima togli il numero di nodi)

            self.ordered_case_bst_height.append(bst_height/self.num_tests_per_dim)
            self.ordered_case_rbt_height.append(rbt_height / self.num_tests_per_dim)

    def process_unordered_test(self):

        for i in range(self.min_dim, self.max_dim + self.dim_step, self.dim_step):

            insert_bst_time = 0
            insert_rbt_time = 0
            search_bst_time = 0
            search_rbt_time = 0
            bst_height = 0
            rbt_height = 0

            for k in range(self.num_tests_per_dim):

                unordered_case_bst = BST()
                unordered_case_rbt = RBT()

                unordered_list = random.sample(range(i), i)
                bst_start = timer()

                for j in range(i):
                    unordered_case_bst.insert(unordered_list[j])

                bst_end = timer()

                rbt_start = timer()

                for j in range(i):
                    unordered_case_rbt.insert(unordered_list[j])

                rbt_end = timer()

                insert_bst_time = insert_bst_time + bst_end - bst_start
                insert_rbt_time = insert_rbt_time + rbt_end - rbt_start

                bst_start = timer()

                for j in range(i):
                    unordered_case_bst.find(j)

                bst_end = timer()

                rbt_start = timer()

                for j in range(i):
                    unordered_case_rbt.find(j)

                rbt_end = timer()

                search_bst_time = search_bst_time + bst_end - bst_start
                search_rbt_time = search_rbt_time + rbt_end - rbt_start

                bst_height = bst_height + unordered_case_bst.get_height()
                rbt_height = rbt_height + unordered_case_rbt.get_height()

            self.unordered_case_bst_insert_time.append(
                insert_bst_time / self.num_tests_per_dim)  # si deve mettere il tempo di inserimento di tutti i valori o il tempo
            self.unordered_case_rbt_insert_time.append(
                insert_rbt_time / self.num_tests_per_dim)  # di inserimento medio di ogni valore (nel caso della seconda dividi per il numero di nodi)

            self.unordered_case_bst_search_time.append(
                search_bst_time / self.num_tests_per_dim)  # si deve mettere il tempo di ricerca di tutti i valori o il tempo
            self.unordered_case_rbt_search_time.append(
                search_rbt_time / self.num_tests_per_dim)  # di ricerca medio di ogni valore (nel caso della seconda dividi per il numero di nodi)

            self.unordered_case_bst_height.append(bst_height / self.num_tests_per_dim)
            self.unordered_case_rbt_height.append(rbt_height / self.num_tests_per_dim)

    def plot_ordered_insert(self):

        dim = range(self.min_dim, self.max_dim + self.dim_step, self.dim_step)

        #self.plt.subplot(221)
        self.plt.plot(dim, self.ordered_case_rbt_insert_time)
        self.plt.plot(dim, self.ordered_case_bst_insert_time)
        self.plt.xlabel('dimensione')
        self.plt.ylabel('tempo')
        self.plt.title("ABR vs ARN nell'inserimento ordinato")
        self.plt.legend(['ARN', 'ABR'])

    def plot_unordered_insert(self):

        dim = range(self.min_dim, self.max_dim + self.dim_step, self.dim_step)

        #self.plt.subplot(222)
        self.plt.plot(dim, self.unordered_case_rbt_insert_time)
        self.plt.plot(dim, self.unordered_case_bst_insert_time)
        self.plt.xlabel('dimensione')
        self.plt.ylabel('tempo')
        self.plt.title("ABR vs ARN nell'inserimento non ordinato")
        self.plt.legend(['ARN', 'ABR'])

    def plot_ordered_search(self):

        dim = range(self.min_dim, self.max_dim + self.dim_step, self.dim_step)

        #self.plt.subplot(223)
        self.plt.plot(dim, self.ordered_case_rbt_search_time)
        self.plt.plot(dim, self.ordered_case_bst_search_time)
        self.plt.xlabel('dimensione')
        self.plt.ylabel('tempo')
        self.plt.title('ABR vs ARN nella ricerca ordinata')
        self.plt.legend(['ARN', 'ABR'])

    def plot_unordered_search(self):
        dim = range(self.min_dim, self.max_dim + self.dim_step, self.dim_step)

        #self.plt.subplot(224)
        self.plt.plot(dim, self.unordered_case_rbt_search_time)
        self.plt.plot(dim, self.unordered_case_bst_search_time)
        self.plt.xlabel('dimensione')
        self.plt.ylabel('tempo')
        self.plt.title('ABR vs ARN nella ricerca non ordinata')
        self.plt.legend(['ARN', 'ABR'])

    def show_plot(self):
        self.plt.show()

    def build_ordered_insert_table(self):
        self._table.add_rows([["Dimensione", "Inserimento ordinato ARN", "Altezza ARN", "Inserimento ordinato ABR", "Altezza ABR"]])

        for i in range(self.min_dim, self.max_dim + self.dim_step, self.dim_step):
            self._table.add_row(
                [str(i),
                 self.ordered_case_rbt_insert_time[int((i - self.min_dim) / self.dim_step)],
                 self.ordered_case_rbt_height[int((i - self.min_dim) / self.dim_step)],
                 self.ordered_case_bst_insert_time[int((i - self.min_dim) / self.dim_step)],
                 self.ordered_case_bst_height[int((i - self.min_dim) / self.dim_step)]]
            )

    def print_ordered_insert_table(self):
        self.build_ordered_insert_table()
        print('\nTexttable Table inserimento ordinato')
        print(self._table.draw())
        self.print_ordered_insert_latex_code()
        self.reset()

    def print_ordered_insert_latex_code(self):
        print('\nTexttable Latex inserimento ordinato')
        print(latextable.draw_latex(self._table,
                                    caption="Tempo medio impiegato per inserire valori ordinati all'interno di ABR e ARN"))

    def build_unordered_insert_table(self):
        self._table.add_rows([["Dimensione", "Inserimento in ARN", "Altezza ARN", "Inserimento in ABR", "Altezza ABR"]])

        for i in range(self.min_dim, self.max_dim + self.dim_step, self.dim_step):
            self._table.add_row(
                [str(i),
                 self.unordered_case_rbt_insert_time[int((i - self.min_dim) / self.dim_step)],
                 self.unordered_case_rbt_height[int((i - self.min_dim) / self.dim_step)],
                 self.unordered_case_bst_insert_time[int((i - self.min_dim) / self.dim_step)],
                 self.unordered_case_bst_height[int((i - self.min_dim) / self.dim_step)]]
            )

    def print_unordered_insert_table(self):
        self.build_unordered_insert_table()
        print('\nTexttable Table inserimento non ordinato')
        print(self._table.draw())
        self.print_unordered_insert_latex_code()
        self.reset()

    def print_unordered_insert_latex_code(self):
        print('\nTexttable Latex inserimento non ordinato')
        print(latextable.draw_latex(self._table,
                                    caption="Tempo medio impiegato per inserire valori inseriti casualmente all'interno di ABR e ARN"))

    def build_ordered_search_table(self):
        self._table.add_rows([["Dimensione", "Ricerca in ARN", "Altezza ARN", "Ricerca in ABR", "Altezza ABR"]])

        for i in range(self.min_dim, self.max_dim + self.dim_step, self.dim_step):
            self._table.add_row(
                [str(i),
                 self.ordered_case_rbt_search_time[int((i - self.min_dim) / self.dim_step)],
                 self.ordered_case_rbt_height[int((i - self.min_dim) / self.dim_step)],
                 self.ordered_case_bst_search_time[int((i - self.min_dim) / self.dim_step)],
                 self.ordered_case_bst_height[int((i - self.min_dim) / self.dim_step)]]
            )

    def print_ordered_search_table(self):
        self.build_ordered_search_table()
        print('\nTexttable Table ricerca ordinata')
        print(self._table.draw())
        self.print_ordered_search_latex_code()
        self.reset()

    def print_ordered_search_latex_code(self):
        print('\nTexttable Latex Ricerca ordinata')
        print(latextable.draw_latex(self._table,
                                    caption="Tempo medio impiegato per la ricerca di valori ordinati all'interno di ABR e ARN"))

    def build_unordered_search_table(self):
        self._table.add_rows([["Dimensione", "Ricerca in ARN", "Altezza ARN", "Ricerca in ABR", "Altezza ABR"]])

        for i in range(self.min_dim, self.max_dim + self.dim_step, self.dim_step):
            self._table.add_row(
                [str(i),
                 self.unordered_case_rbt_search_time[int((i - self.min_dim) / self.dim_step)],
                 self.unordered_case_rbt_height[int((i - self.min_dim) / self.dim_step)],
                 self.unordered_case_bst_search_time[int((i - self.min_dim) / self.dim_step)],
                 self.unordered_case_bst_height[int((i - self.min_dim) / self.dim_step)]]
            )

    def print_unordered_search_table(self):
        self.build_unordered_search_table()
        print('\nTexttable Table Ricerca non ordinata')
        print(self._table.draw())
        self.print_unordered_search_latex_code()
        self.reset()

    def print_unordered_search_latex_code(self):
        print('\nTexttable Latex Ricerca non ordinata')
        print(latextable.draw_latex(self._table,
                                    caption="Tempo medio impiegato per la ricerca di valori inseriti casualmente all'interno di ABR e ARN"))

    def reset(self):
        self._table.reset()
        self._table.set_cols_align(["c"] * 5)
        self._table.set_cols_dtype(['i', 'e', 'f', 'e', 'f'])


def main():
    rbt = RBT()

    for i in range(10):
        rbt.insert(i+1)

    rbt.get_node(1).get_right().print()
    rbt.x_order()
    print(rbt.get_height())


if __name__ == "__main__":
    main()
