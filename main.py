import tkinter as tk
from tkinter import ttk
import time
import winsound as ws


class Clock:
    def __init__(self):
        self.stage = 0
        self.focus = 25
        self.rest = 5
        self.long = 15
        self.cycle = 5
        self.e = 0
        self.paused = False
        self.actual = time.time()
        self.focus_color = 'red'
        self.rest_color = 'blue'
        self.memo = []
        self.day = time.strftime('%j')

        with open('memo.txt', 'r') as f:
            for line in f:
                self.memo.append(int(line[:-1]))

        self.week_auxiliar = 0
        w = time.strftime('%w')
        for x in range(int(w)):
            self.week_auxiliar += self.memo[int(self.day) - 1 - x]
        self.month_auxiliar = 0
        m = time.strftime('%d')
        for y in range(int(m)):
            self.month_auxiliar += self.memo[int(self.day) - y]

        self.root = tk.Tk()
        self.root.title('Pomodoro')
        self.root.iconbitmap(r'C:\Users\rafae_000\PycharmProjects\pomodoro\Bingxueling-Fruit-Vegetables-Tomato.ico')
        self.tab_parent = ttk.Notebook(self.root)
        self.tab1 = ttk.Frame(self.tab_parent)
        self.tab2 = ttk.Frame(self.tab_parent)
        self.tab3 = ttk.Frame(self.tab_parent)
        self.tab4 = ttk.Frame(self.tab_parent)

        self.tab_parent.add(self.tab1, text='Timer')
        self.tab_parent.add(self.tab2, text='Configure')
        self.tab_parent.add(self.tab3, text='Custom')
        self.tab_parent.add(self.tab4, text='Stats')
        self.tab_parent.pack()

        self.minute = tk.Label(self.tab1, text="00", font=('Helvetica', 80), fg='red')
        self.separator = tk.Label(self.tab1, text=':', font=('Helvetica', 80), fg='red')
        self.second = tk.Label(self.tab1, text="00", font=('Helvetica', 80), fg='red')
        self.start = tk.Button(self.tab1, text='Start', command=self.update_clock)
        self.stop = tk.Button(self.tab1, text='Break', command=self.pause)
        self.restart = tk.Button(self.tab1, text='Restart', command=self.restart)

        self.minute.grid(row=0)
        self.separator.grid(row=0, column=1)
        self.second.grid(row=0, column=2)
        self.start.grid(row=1, column=0)
        self.stop.grid(row=1, column=1)
        self.restart.grid(row=1, column=2)

        self.focus_label = tk.Label(self.tab2, text='Focus time: ')
        self.rest_label = tk.Label(self.tab2, text='Short break time: ')
        self.long_label = tk.Label(self.tab2, text='Long break time: ')
        self.cycle_label = tk.Label(self.tab2, text='Pomodoros to long break: ')

        self.focus_value = tk.Label(self.tab2, text=(str(self.focus) + 'min'), borderwidth=3, relief='sunken', width=8)
        self.rest_value = tk.Label(self.tab2, text=(str(self.rest) + 'min'), borderwidth=3, relief='sunken', width=8)
        self.long_value = tk.Label(self.tab2, text=(str(self.long) + 'min'), borderwidth=3, relief='sunken', width=8)
        self.cycle_value = tk.Label(self.tab2, text=(str(self.cycle)), borderwidth=3, relief='sunken', width=8)

        self.focus_entry = tk.Entry(self.tab2, width=3)
        self.rest_entry = tk.Entry(self.tab2, width=3)
        self.long_entry = tk.Entry(self.tab2, width=3)
        self.cycle_entry = tk.Entry(self.tab2, width=3)

        self.focus_button = tk.Button(self.tab2, text='Edit', command=lambda: self.edit(self.focus_entry.get(), 'f'))
        self.rest_button = tk.Button(self.tab2, text='Edit', command=lambda: self.edit(self.rest_entry.get(), 'r'))
        self.long_button = tk.Button(self.tab2, text='Edit', command=lambda: self.edit(self.long_entry.get(), 'l'))
        self.cycle_button = tk.Button(self.tab2, text='Edit', command=lambda: self.edit(self.cycle_entry.get(), 'c'))

        self.focus_label.grid(row=0, column=0, sticky='W')
        self.rest_label.grid(row=1, column=0, sticky='W')
        self.long_label.grid(row=2, column=0, sticky='W')
        self.cycle_label.grid(row=3, column=0, sticky='W')

        self.focus_value.grid(row=0, column=1)
        self.rest_value.grid(row=1, column=1)
        self.long_value.grid(row=2, column=1)
        self.cycle_value.grid(row=3, column=1)

        self.focus_entry.grid(row=0, column=2)
        self.rest_entry.grid(row=1, column=2)
        self.long_entry.grid(row=2, column=2)
        self.cycle_entry.grid(row=3, column=2)

        self.focus_button.grid(row=0, column=3)
        self.rest_button.grid(row=1, column=3)
        self.long_button.grid(row=2, column=3)
        self.cycle_button.grid(row=3, column=3)

        self.number_color = tk.Label(self.tab3, text='Color during focus: ')
        self.c1 = tk.Button(self.tab3, bg='#000000',
                            width=1, command=lambda: self.change_color('n', self.c1.cget('bg')))
        self.c2 = tk.Button(self.tab3, bg='#800080',
                            width=1, command=lambda: self.change_color('n', self.c2.cget('bg')))
        self.c3 = tk.Button(self.tab3, bg='#FF0000',
                            width=1, command=lambda: self.change_color('n', self.c3.cget('bg')))
        self.c4 = tk.Button(self.tab3, bg='#FFB833',
                            width=1, command=lambda: self.change_color('n', self.c4.cget('bg')))
        self.c5 = tk.Button(self.tab3, bg='#FFFF00',
                            width=1, command=lambda: self.change_color('n', self.c5.cget('bg')))
        self.c6 = tk.Button(self.tab3, bg='#008000',
                            width=1, command=lambda: self.change_color('n', self.c6.cget('bg')))
        self.c7 = tk.Button(self.tab3, bg='#00FFFF',
                            width=1, command=lambda: self.change_color('n', self.c7.cget('bg')))
        self.c8 = tk.Button(self.tab3, bg='#0000FF',
                            width=1, command=lambda: self.change_color('n', self.c8.cget('bg')))
        self.c9 = tk.Button(self.tab3, bg='#A52A2A',
                            width=1, command=lambda: self.change_color('n', self.c9.cget('bg')))
        self.c10 = tk.Button(self.tab3, bg='#FFFFFF',
                             width=1, command=lambda: self.change_color('n', self.c10.cget('bg')))
        self.c11 = tk.Button(self.tab3, bg='#FFC0CB',
                             width=1, command=lambda: self.change_color('n', self.c11.cget('bg')))
        
        self.number_color_2 = tk.Label(self.tab3, text='Color during break: ')
        self.d1 = tk.Button(self.tab3, bg='#000000',
                            width=1, command=lambda: self.change_color('r', self.c1.cget('bg')))
        self.d2 = tk.Button(self.tab3, bg='#800080',
                            width=1, command=lambda: self.change_color('r', self.c2.cget('bg')))
        self.d3 = tk.Button(self.tab3, bg='#FF0000',
                            width=1, command=lambda: self.change_color('r', self.c3.cget('bg')))
        self.d4 = tk.Button(self.tab3, bg='#FFB833',
                            width=1, command=lambda: self.change_color('r', self.c4.cget('bg')))
        self.d5 = tk.Button(self.tab3, bg='#FFFF00',
                            width=1, command=lambda: self.change_color('r', self.c5.cget('bg')))
        self.d6 = tk.Button(self.tab3, bg='#008000',
                            width=1, command=lambda: self.change_color('r', self.c6.cget('bg')))
        self.d7 = tk.Button(self.tab3, bg='#00FFFF',
                            width=1, command=lambda: self.change_color('r', self.c7.cget('bg')))
        self.d8 = tk.Button(self.tab3, bg='#0000FF',
                            width=1, command=lambda: self.change_color('r', self.c8.cget('bg')))
        self.d9 = tk.Button(self.tab3, bg='#A52A2A',
                            width=1, command=lambda: self.change_color('r', self.c9.cget('bg')))
        self.d10 = tk.Button(self.tab3, bg='#FFFFFF',
                             width=1, command=lambda: self.change_color('r', self.c10.cget('bg')))
        self.d11 = tk.Button(self.tab3, bg='#FFC0CB',
                             width=1, command=lambda: self.change_color('r', self.c11.cget('bg')))

        self.background_color = tk.Label(self.tab3, text='Background color: ')
        self.e1 = tk.Button(self.tab3, bg='#000000',
                            width=1, command=lambda: self.change_color('a', self.c1.cget('bg')))
        self.e2 = tk.Button(self.tab3, bg='#800080',
                            width=1, command=lambda: self.change_color('a', self.c2.cget('bg')))
        self.e3 = tk.Button(self.tab3, bg='#FF0000',
                            width=1, command=lambda: self.change_color('a', self.c3.cget('bg')))
        self.e4 = tk.Button(self.tab3, bg='#FFB833',
                            width=1, command=lambda: self.change_color('a', self.c4.cget('bg')))
        self.e5 = tk.Button(self.tab3, bg='#FFFF00',
                            width=1, command=lambda: self.change_color('a', self.c5.cget('bg')))
        self.e6 = tk.Button(self.tab3, bg='#008000',
                            width=1, command=lambda: self.change_color('a', self.c6.cget('bg')))
        self.e7 = tk.Button(self.tab3, bg='#00FFFF',
                            width=1, command=lambda: self.change_color('a', self.c7.cget('bg')))
        self.e8 = tk.Button(self.tab3, bg='#0000FF',
                            width=1, command=lambda: self.change_color('a', self.c8.cget('bg')))
        self.e9 = tk.Button(self.tab3, bg='#A52A2A',
                            width=1, command=lambda: self.change_color('a', self.c9.cget('bg')))
        self.e10 = tk.Button(self.tab3, bg='#FFFFFF',
                             width=1, command=lambda: self.change_color('a', self.c10.cget('bg')))
        self.e11 = tk.Button(self.tab3, bg='#FFC0CB',
                             width=1, command=lambda: self.change_color('a', self.c11.cget('bg')))

        self.number_color.grid(row=0, column=0)
        self.c1.grid(row=0, column=1)
        self.c2.grid(row=0, column=2)
        self.c3.grid(row=0, column=3)
        self.c4.grid(row=0, column=4)
        self.c5.grid(row=0, column=5)
        self.c6.grid(row=0, column=6)
        self.c7.grid(row=0, column=7)
        self.c8.grid(row=0, column=8)
        self.c9.grid(row=0, column=9)
        self.c10.grid(row=0, column=10)
        self.c11.grid(row=0, column=11)

        self.number_color_2.grid(row=1, column=0)
        self.d1.grid(row=1, column=1)
        self.d2.grid(row=1, column=2)
        self.d3.grid(row=1, column=3)
        self.d4.grid(row=1, column=4)
        self.d5.grid(row=1, column=5)
        self.d6.grid(row=1, column=6)
        self.d7.grid(row=1, column=7)
        self.d8.grid(row=1, column=8)
        self.d9.grid(row=1, column=9)
        self.d10.grid(row=1, column=10)
        self.d11.grid(row=1, column=11)

        self.background_color.grid(row=2, column=0)
        self.e1.grid(row=2, column=1)
        self.e2.grid(row=2, column=2)
        self.e3.grid(row=2, column=3)
        self.e4.grid(row=2, column=4)
        self.e5.grid(row=2, column=5)
        self.e6.grid(row=2, column=6)
        self.e7.grid(row=2, column=7)
        self.e8.grid(row=2, column=8)
        self.e9.grid(row=2, column=9)
        self.e10.grid(row=2, column=10)
        self.e11.grid(row=2, column=11)

        self.focus_today = tk.Label(self.tab4, text='Focus today: ')
        self.focus_week = tk.Label(self.tab4, text='Focus this week: ')
        self.focus_month = tk.Label(self.tab4, text='Focus this month: ')

        self.today_value = tk.Label(self.tab4, text=(str(round(self.memo[int(self.day) - 1] / 60, 1)) + 'h'))
        self.week_value = tk.Label(self.tab4, text=(str(round(self.week_auxiliar / 60, 1)) + 'h'))
        self.month_value = tk.Label(self.tab4, text=str(round(self.month_auxiliar / 60, 1)) + 'h')

        self.focus_today.grid(row=0, column=0)
        self.focus_week.grid(row=1, column=0)
        self.focus_month.grid(row=2, column=0)
        self.today_value.grid(row=0, column=1)
        self.week_value.grid(row=1, column=1)
        self.month_value.grid(row=2, column=1)

        self.root.mainloop()

    def update_clock(self):
        if self.e == 0:
            self.actual = time.time()
            self.e += 1
        if self.stage % 2 == 1:
            self.minute.config(fg=self.rest_color)
            self.second.config(fg=self.rest_color)
            self.separator.config(fg=self.rest_color)
            if self.stage == self.cycle:
                now = round(60 * self.long - time.time() + self.actual)
            else:
                now = round(60 * self.rest - time.time() + self.actual)

        else:
            self.minute.config(fg=self.focus_color)
            self.second.config(fg=self.focus_color)
            self.separator.config(fg=self.focus_color)
            now = round(60 * self.focus - time.time() + self.actual)
            if self.stage == self.cycle + 1:
                self.stage = 0

        if len(str(now // 60)) == 1:
            minute = '0' + str(now // 60)
        else:
            minute = str(now // 60)

        if len(str(now % 60)) == 1:
            second = '0' + str(now % 60)
        else:
            second = str(now % 60)
        self.minute.configure(text=minute)
        self.second.configure(text=second)
        if now != 0:
            if self.paused:
                self.actual += 1
            self.root.after(1000, self.update_clock)
        else:
            ws.PlaySound('smokealarm.wav', ws.SND_ALIAS)
            self.stage += 1
            self.e = 0
            if self.stage % 2 == 1:
                self.memo[int(self.day) - 1] += self.focus
                self.atualize()

    def edit(self, value, target):
        if target == 'f':
            self.focus_value.config(text=(str(value) + 'min'))
            self.focus = int(value)
        elif target == 'r':
            self.rest_value.config(text=(str(value) + 'min'))
            self.rest = int(value)
        elif target == 'l':
            self.long_value.config(text=(str(value) + 'min'))
            self.long = int(value)
        else:
            self.cycle_value.config(text=str(value))
            self.cycle = int(value)

    def pause(self):
        if self.paused:
            self.paused = False
            self.stop.config(text='Pause')
        else:
            self.paused = True
            self.stop.config(text='Resume')

    def restart(self):
        self.e = 0
        
    def change_color(self, target, color):
        if target == 'n':
            if self.stage % 2 == 0:
                self.minute.config(fg=color)
                self.second.config(fg=color)
                self.separator.config(fg=color)
            self.focus_color = color
        elif target == 'r':
            if self.stage % 2 == 1:
                self.minute.config(fg=color)
                self.second.config(fg=color)
                self.separator.config(fg=color)
            self.rest_color = color
        else:
            self.minute.config(bg=color)
            self.second.config(bg=color)
            self.separator.config(bg=color)

    def atualize(self):
        with open('memo.txt', 'w') as f:
            for line in self.memo:
                f.write(str(line) + '\n')
        self.today_value.config(text=(str(round(self.memo[int(self.day) - 1] / 60, 1)) + 'h'))
        w = time.strftime('%w')
        for x in range(int(w)):
            self.week_auxiliar += self.memo[int(self.day) - 1 - x]
        self.week_value.config(text=(str(round(self.week_auxiliar / 60, 1)) + 'h'))
        m = time.strftime('%d')
        for y in range(int(m)):
            self.month_auxiliar += self.memo[int(self.day) - y]
        self.month_value.config(text=(str(round(self.month_auxiliar / 60, 1)) + 'h'))


app = Clock()
