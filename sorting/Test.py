import matplotlib.pyplot as plt
import random
import copy
from timeit import default_timer as timer
from Merge_Sort import merge_sort
from Insertion_Sort import insertion_sort
import latextable as latextable
from texttable import Texttable
from numpy import average


class Test:

    def __init__(self):
        self.__abscissa_axis = []
        self.__merge_sort_t = []
        self.__insertion_sort_t = []

    def process(self, min_dim, max_dim, dim_step, num_test, list_type='random'):

        ms_increasing_list = []
        ms_decreasing_list = []
        ms_lists = []
        is_lists = []
        merge_sort_times = []
        insertion_sort_times = []
        merge_sort_avg_time = []
        insertion_sort_avg_time = []

        for dim in range(min_dim, max_dim + dim_step, dim_step):

            # inizializza le liste dei tempi totali di ordinamento per array di stessa dimensione

            for n_test in range(num_test):

                # crea lista pseudo casuale di dimensione i con valori tra 1 e i distinti
                ms_random_list = random.sample(range(1, dim + 1), dim)

                #crea liste crescente e decrescente
                for j in range(1, dim + 1):
                    ms_increasing_list.append(j)
                    ms_decreasing_list.append(dim - j + 1)

                is_random_list = copy.deepcopy(ms_random_list)
                is_increasing_list = copy.deepcopy(ms_increasing_list)
                is_decreasing_list = copy.deepcopy(ms_decreasing_list)

                # for gen1, gen2 in zip(gen_sorter1, gen_sorter2):
                #     print(gen1)
                #     print(gen2)

                ms_lists.append(ms_random_list)
                ms_lists.append(ms_increasing_list)
                ms_lists.append(ms_decreasing_list)

                is_lists.append(is_random_list)
                is_lists.append(is_increasing_list)
                is_lists.append(is_decreasing_list)

                # esegue mergesort sulle liste e somma i tempi di ordinamento per num_test volte
                for list in ms_lists:
                    # for gen in gen_sorter1:
                    #     print(gen)

                    start = timer()
                    merge_sort(list, 0, dim - 1)
                    end = timer()
                    merge_sort_times.append(end - start)
                #print(merge_sort_times)

                # for gen in gen_sorter1:
                #     print(gen)

                # for gen1, gen2 in zip(gen_sorter1, gen_sorter2):
                #     print(gen1)
                #     print(gen2)

                # esegue insertion sort sulle liste e somma i tempi di ordinamento per num_test volte
                for list in is_lists:
                    start = timer()
                    insertion_sort(list)
                    end = timer()
                    insertion_sort_times.append(end - start)
                #print(insertion_sort_times)

                # for gen1, gen2 in zip(gen_sorter1, gen_sorter2):
                #     print(gen1)
                #     print(gen2)

                # svuota le liste per poter essere ricorstruite nel test successivo
                ms_random_list.clear()
                ms_increasing_list.clear()
                ms_decreasing_list.clear()

                is_random_list.clear()
                is_increasing_list.clear()
                is_decreasing_list.clear()

                ms_lists.clear()
                is_lists.clear()

            # calcola la media dei tempi di ordinamento dividendo i valori registrati per il valore di num_test

            for i in range(3):
                merge_sort_avg_time.append(average(merge_sort_times[i::3]))

            for i in range(3):
                insertion_sort_avg_time.append(average(insertion_sort_times[i::3]))

            # resgistra i valori delle dimensioni delle liste
            self.__abscissa_axis.append(dim)
            # registra i tempi di ordinamento medi di merge_sort su liste di stessa dimensione
            self.__merge_sort_t.append(copy.deepcopy(merge_sort_avg_time))
            # registra i tempi di ordinamento medi di insertion sort su liste di stessa dimensione
            self.__insertion_sort_t.append(copy.deepcopy(insertion_sort_avg_time))

            # azzera i tempi di ordinamento totali e medi registrati per poterli usare per le liste di dimensione
            # diversa successive
            merge_sort_times.clear()
            insertion_sort_times.clear()
            merge_sort_avg_time.clear()
            insertion_sort_avg_time.clear()

    def plot_merge_insertion_comparison(self):
        plt.subplot(121)
        plt.xlabel('Dimensione (n)')
        plt.ylabel('Tempo (s)')
        plt.title('Merge-Sort')

        line1, = plt.plot(self.__abscissa_axis, [row[0] for row in self.__merge_sort_t])
        line2, = plt.plot(self.__abscissa_axis, [row[1] for row in self.__merge_sort_t])
        line3, = plt.plot(self.__abscissa_axis, [row[2] for row in self.__merge_sort_t])

        plt.legend((line1, line2, line3), ['Pseudo-casuale', 'Crescente', 'Decrescente'])

        plt.subplot(122)
        plt.xlabel('Dimensione (n)')
        plt.ylabel('Tempo (s)')
        plt.title('Insertion-Sort')

        line1, = plt.plot(self.__abscissa_axis, [row[0] for row in self.__insertion_sort_t])
        line2, = plt.plot(self.__abscissa_axis, [row[1] for row in self.__insertion_sort_t])
        line3, = plt.plot(self.__abscissa_axis, [row[2] for row in self.__insertion_sort_t])

        plt.legend((line1, line2, line3), ['Pseudo-casuale', 'Crescente', 'Decrescente'])

        plt.show()

    def plot_merge_insertion_casual_insert_case(self):

        plt.xlabel('Dimensione (n)')
        plt.ylabel('Tempo (s)')
        plt.title('Merge-Sort e Insertion-Sort su liste pseudo-casuali')

        line1, = plt.plot(self.__abscissa_axis, [row[0] for row in self.__merge_sort_t])
        line2, = plt.plot(self.__abscissa_axis, [row[0] for row in self.__insertion_sort_t])

        plt.legend((line1, line2), ['Merge-Sort', 'Insertion-Sort'])

        plt.show()

    def plot_merge_insertion_increasing_insert_case(self):

        plt.xlabel('Dimensione (n)')
        plt.ylabel('Tempo (s)')
        plt.title('Merge-Sort e Insertion-Sort su liste ordinate')

        line1, = plt.plot(self.__abscissa_axis, [row[1] for row in self.__merge_sort_t])
        line2, = plt.plot(self.__abscissa_axis, [row[1] for row in self.__insertion_sort_t])

        plt.legend((line1, line2), ['Merge-sort', 'Insertion-sort'])

        plt.show()

    def plot_merge_insertion_decreasing_insert_case(self):

        plt.xlabel('Dimensione (n)')
        plt.ylabel('Tempo (s)')
        plt.title('Merge-Sort e Insertion-Sort su liste ordinate inversamente')

        line1, = plt.plot(self.__abscissa_axis, [row[2] for row in self.__merge_sort_t])
        line2, = plt.plot(self.__abscissa_axis, [row[2] for row in self.__insertion_sort_t])

        plt.legend((line1, line2), ['Merge-sort', 'Insertion-sort'])

        plt.show()

    def latex_tables(self):
        table = Texttable()
        table.set_cols_align(["c"] * 3)

        table.set_cols_dtype(['i', 't', 't'])

        table.add_rows([["Dimensione", "Merge-Sort", "Insertion-Sort"]])
        for i in range(len(self.__abscissa_axis)):
            table.add_row(
                [str(self.__abscissa_axis[i]), str(self.__merge_sort_t[i][0]), str(self.__insertion_sort_t[i][0])]
            )

        print('\nTexttable Table ordinamento casuale:')
        print(table.draw())

        print('\nTexttable Latex ordinamento casuale:')
        print(latextable.draw_latex(table,
                                    caption="Merge-Sort e Insertion-Sort a confronto per liste casuali"))

        table.reset()

        table.set_cols_align(["c"] * 3)

        table.set_cols_dtype(['i', 't', 't'])

        table.add_rows([["Dimensione", "Merge-Sort", "Insertion-Sort"]])

        for i in range(len(self.__abscissa_axis)):
            table.add_row(
                [str(self.__abscissa_axis[i]), str(self.__merge_sort_t[i][1]), str(self.__insertion_sort_t[i][1])]
            )

        print('\nTexttable Table ordinamento crescente:')
        print(table.draw())

        print('\nTexttable Latex ordinamento crescente:')
        print(latextable.draw_latex(table,
                                    caption="Merge-Sort e Insertion-Sort a confronto per liste ordinate"))

        table.reset()

        table.set_cols_align(["c"] * 3)

        table.set_cols_dtype(['i', 't', 't'])

        table.add_rows([["Dimensione", "Merge-Sort", "Insertion-Sort"]])
        for i in range(len(self.__abscissa_axis)):
            table.add_row(
                [str(self.__abscissa_axis[i]), str(self.__merge_sort_t[i][2]), str(self.__insertion_sort_t[i][2])]
            )

        print('\nTexttable Table ordinamento decrescente:')
        print(table.draw())

        print('\nTexttable Latex ordinamento decrescente:')
        print(latextable.draw_latex(table,
                                    caption="Merge-Sort e Insertion-Sort a confronto per liste ordinate inversamente"))
