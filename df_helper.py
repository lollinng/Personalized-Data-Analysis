import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from xtyping import Self


class helper():

    def __init__(self):
        plt.rcParams["figure.figsize"] = (14, 7.5)
        Self.Every_total = ['Total Theory', 'Total Practicals', 'percent']

    def SEfunction(self, roll_number):
        SE = pd.read_excel('attendance.xlsx', sheet_name='SE')
        SE_theory = ['DM', 'FDS', 'OOP', 'CG', 'DELD']
        SE_theory_total = [37, 37, 37, 34, 22]
        SE_pracs = ['DSL(AS)', 'DSL(DC)', 'OOPL', 'CGL', 'DEL', 'BCS']
        SE_pracs_total = [14, 13, 16, 14, 12, 10]
        SE_Every_total = [167, 75, 100]
        print(SE[0:1])
        self.student(roll_number, SE_theory,
                     SE_theory_total, SE, "SE_roll_theory")
        self.student(roll_number, SE_pracs,
                     SE_pracs_total, SE, "SE_roll_pracs")
        self.student(roll_number, Self.Every_total,
                     SE_Every_total, SE, "SE_roll_all")

    def BEfunction(self, roll_number):
        BE = pd.read_excel('attendance.xlsx', sheet_name='BE')
        BE_theory = ['HPC', 'AI&R', 'DA', 'DM&W', 'STQA']
        BE_theory_total = [36, 35, 34, 36, 36]
        BE_pracs = ['LP-I (RK)', 'LP-I(MM)', 'LP-II (PG)', 'LP-II(AAJ)']
        BE_pracs_total = [15, 11, 12, 10]
        BE_Every_total = [177, 48, 100]
        self.student(roll_number, BE_theory,
                     BE_theory_total, BE, "BE_roll_theory")
        self.student(roll_number, BE_pracs,
                     BE_pracs_total, BE, "BE_roll_pracs")
        self.student(roll_number, Self.Every_total,
                     BE_Every_total, BE, "BE_roll_all")

    def TEfunction(self, roll_number):
        TE = pd.read_excel('attendance.xlsx', sheet_name='TE')
        TE_theory = ['TOC', 'DBMS', 'SEPM', 'ISEE', 'CN']
        TE_theory_total = [35, 35, 37, 34, 37]
        TE_pracs = ['DBMSL(DC)', 'DBMSL(SP)', 'SDL(PG)', 'SDL(AJ)', 'CNL']
        TE_pracs_total = [17, 14, 12, 10, 12]
        TE_Every_total = [179, 54, 100]
        self.student(roll_number, TE_theory,
                     TE_theory_total, TE, "TE_roll_theory")
        self.student(roll_number, TE_pracs,
                     TE_pracs_total, TE, "TE_roll_pracs")
        self.student(roll_number, Self.Every_total,
                     TE_Every_total, TE, "TE_roll_all")

    def student(self, roll_no, subj_list, tot_sub_list, df, place):
        X = subj_list
        total = tot_sub_list
        print(df[0:1])
        # print(df.head())
        value = df[df['SrNo.'] == int(roll_no)]
        if len(total) == 3:
            values = np.array([
                int(value[X[0]])/total[0],
                int(value[X[1]])/total[1],
                int(value[X[2]])/total[2],
            ])
        if len(total) == 4:
            values = np.array([
                int(value[X[0]])/total[0],
                int(value[X[1]])/total[1],
                int(value[X[2]])/total[2],
                int(value[X[3]])/total[3],
            ])
        elif len(total) == 5:
            values = np.array([
                int(value[X[0]])/total[0],
                int(value[X[1]])/total[1],
                int(value[X[2]])/total[2],
                int(value[X[3]])/total[3],
                int(value[X[4]])/total[4]
            ]
            )
        elif len(total) == 6:
            values = np.array([
                int(value[X[0]])/total[0],
                int(value[X[1]])/total[1],
                int(value[X[2]])/total[2],
                int(value[X[3]])/total[3],
                int(value[X[4]])/total[4],
                int(value[X[5]])/total[5]
            ]
            )
        print(values)
        x = np.linspace(-1, 5, 30)
        y = [0.3]*30
        plt.bar(X, values, 0.4, label='Percentage attendance')
        plt.plot(x, y, '-r', label='minimum criteria')

        plt.xlabel("Theory Subjects")
        plt.ylabel("Attendance Percentage")
        print(roll_no)
        plt.title("Theory Subject attendance of roll no."+str(roll_no))
        plt.legend()
        plt.savefig('static/images/'+place+'.png')
        plt.clf()

    def defaulters(self, df):
        defaulters = df[(df['percent'] <= 35)]
        roll = list(defaulters['SrNo.'])
        names = list(defaulters['Name'])
        perc = list(defaulters['percent'])
        return roll, names, perc


# obj = helper()
# roll_no = 46
# helper.student(roll_no, SE_theory, SE_theory_total, SE)
# helper.student(roll_no, SE_pracs, SE_pracs_total, SE)
# helper.student(roll_no, Every_total, SE_Every_total, SE)

# helper.student(roll_no, BE_theory, BE_theory_total, BE)
# helper.student(roll_no, BE_pracs, BE_pracs_total, BE)
# helper.student(roll_no, Every_total, BE_Every_total, BE)

# helper.student(roll_no, TE_theory, TE_theory_total, TE)
# helper.student(roll_no, TE_pracs, TE_pracs_total, TE)
# helper.student(roll_no, Every_total, SE_Every_total, SE)
