import tkinter as tk
from tkinter import ttk
from ff_scraper import get_trade_evaluation, get_all_players
import matplotlib.pyplot as plt

team_a_selected_players = set()
team_b_selected_players = set()
trade_history = []

def filter_listbox(listbox, players, search_term, selected_players_set):
    listbox.delete(0, tk.END)
    for player in players:
        if search_term.lower() in player.lower():
            listbox.insert(tk.END, player)

def evaluate_trade():
    team_a_players = list(team_a_selected_players)
    team_b_players = list(team_b_selected_players)
    
    message, value_team_a, value_team_b = get_trade_evaluation(team_a_players, team_b_players)
    display_message = f"{message}\n\nTeam A Total Points: {value_team_a:.2f}\nTeam B Total Points: {value_team_b:.2f}"
    result_label.config(text=display_message)

    # Store this trade in the trade history
    trade = {
        'team_a_players': team_a_players,
        'team_b_players': team_b_players,
        'value_team_a': value_team_a,
        'value_team_b': value_team_b
    }
    trade_history.append(trade)

def on_select_A(event):
    current_selection = team_a_listbox.curselection()
    selected_players = {team_a_listbox.get(i) for i in current_selection}
    team_a_selected_players.update(selected_players)
    team_a_selected_label.config(text=', '.join(team_a_selected_players))

def on_select_B(event):
    current_selection = team_b_listbox.curselection()
    selected_players = {team_b_listbox.get(i) for i in current_selection}
    team_b_selected_players.update(selected_players)
    team_b_selected_label.config(text=', '.join(team_b_selected_players))

def clear_selections():
    team_a_selected_players.clear()
    team_b_selected_players.clear()
    team_a_listbox.selection_clear(0, tk.END)
    team_b_listbox.selection_clear(0, tk.END)
    team_a_selected_label.config(text='')
    team_b_selected_label.config(text='')

def show_history():
    history_window = tk.Toplevel(root)
    history_window.title("Trade History")
    
    text_widget = tk.Text(history_window, wrap=tk.WORD, width=60, height=20)
    text_widget.pack(padx=10, pady=10)
    
    for trade in trade_history:
        text_widget.insert(tk.END, f"Team A: {', '.join(trade['team_a_players'])} ({trade['value_team_a']:.2f} points)\n")
        text_widget.insert(tk.END, f"Team B: {', '.join(trade['team_b_players'])} ({trade['value_team_b']:.2f} points)\n")
        text_widget.insert(tk.END, '-'*50 + '\n')
    
    # Graphical representation using matplotlib
    def plot_graph():
        team_a_values = [trade['value_team_a'] for trade in trade_history]
        team_b_values = [trade['value_team_b'] for trade in trade_history]

        plt.bar(range(len(team_a_values)), team_a_values, label='Team A')
        plt.bar(range(len(team_b_values)), team_b_values, label='Team B', bottom=team_a_values)
        plt.ylabel('Trade Value')
        plt.xlabel('Trade Number')
        plt.title('Trade History Graphical Representation')
        plt.legend()
        plt.show()

    plot_button = ttk.Button(history_window, text="Show Graph", command=plot_graph)
    plot_button.pack(pady=10)

root = tk.Tk()
root.title("Trade Value Calculator")

all_players = sorted(get_all_players())

team_a_listbox = tk.Listbox(root, selectmode=tk.MULTIPLE, exportselection=0, width=40, height=15)
team_a_listbox.grid(row=2, column=0, padx=10, pady=5)
team_a_listbox.bind('<<ListboxSelect>>', on_select_A)

team_b_listbox = tk.Listbox(root, selectmode=tk.MULTIPLE, exportselection=0, width=40, height=15)
team_b_listbox.grid(row=2, column=1, padx=10, pady=5)
team_b_listbox.bind('<<ListboxSelect>>', on_select_B)

for player in all_players:
    team_a_listbox.insert(tk.END, player)
    team_b_listbox.insert(tk.END, player)

search_var_A = tk.StringVar()
search_var_A.trace('w', lambda name, index, mode, var=search_var_A: filter_listbox(team_a_listbox, all_players, var.get(), team_a_selected_players))
search_bar_A = ttk.Entry(root, textvariable=search_var_A, width=37)
search_bar_A.grid(row=1, column=0, padx=10, pady=5, sticky='NW')

search_var_B = tk.StringVar()
search_var_B.trace('w', lambda name, index, mode, var=search_var_B: filter_listbox(team_b_listbox, all_players, var.get(), team_b_selected_players))
search_bar_B = ttk.Entry(root, textvariable=search_var_B, width=37)
search_bar_B.grid(row=1, column=1, padx=10, pady=5, sticky='NW')

team_a_selected_label = ttk.Label(root, text="", wraplength=250)
team_a_selected_label.grid(row=3, column=0, padx=10, pady=5)

team_b_selected_label = ttk.Label(root, text="", wraplength=250)
team_b_selected_label.grid(row=3, column=1, padx=10, pady=5)

evaluate_button = ttk.Button(root, text="Evaluate", command=evaluate_trade)
evaluate_button.grid(row=4, column=0, pady=10)

history_button = ttk.Button(root, text="Trade History", command=show_history)
history_button.grid(row=4, column=1, pady=10)

clear_button = ttk.Button(root, text="Clear Selections", command=clear_selections)
clear_button.grid(row=5, column=0, columnspan=2, pady=10)

result_label = ttk.Label(root, text="", wraplength=400)
result_label.grid(row=6, column=0, columnspan=2, padx=10, pady=5)

root.iconphoto(False, tk.PhotoImage(file='C:\\Users\\benne\\OneDrive\\Desktop\\ISTA498 Capstone\\ffl.png'))
root.mainloop()
