import tkinter as tk


def List_color(window_name, text, var_name):
    frame = tk.Frame(window_name)
    frame.pack(side=tk.LEFT)

    label = tk.Label(frame, text=text)
    label.pack()

    listbox = tk.Listbox(frame)
    colors = ['blue', 'red', 'yellow', 'green']
    for color in colors:
        listbox.insert(tk.END, color)
    listbox.pack()

    listbox.bind('<<ListboxSelect>>', lambda event, name=var_name: selected_item(event, name))


def selected_item(event, var_name):
    selected_index = event.widget.curselection()
    if selected_index:
        selected_value = event.widget.get(selected_index[0])  # Get the first selected item
        globals()[var_name] = selected_value
        return selected_value


def validate_choice(code):
    if color1:
        code.append(color1)
    if color2:
        code.append(color2)
    if color3:
        code.append(color3)
    if color4:
        code.append(color4)
    print("Code validé :", code)


def Code():
    code = []
    windows_mastermind_1 = tk.Tk()

    windows_mastermind_1.geometry("900x500")
    windows_mastermind_1.title("Choose your mastermind code")

    List_color(windows_mastermind_1, 'Color 1:', 'color1')
    List_color(windows_mastermind_1, 'Color 2:', 'color2')
    List_color(windows_mastermind_1, 'Color 3:', 'color3')
    List_color(windows_mastermind_1, 'Color 4:', 'color4')

    Validate_choice = tk.Button(windows_mastermind_1, text="Validate color chosen",
                                command=lambda: (validate_choice(code), windows_mastermind_1.destroy()))
    Validate_choice.pack(side=tk.BOTTOM)

    windows_mastermind_1.mainloop()
    return code


def Result_bad(good, mid, false):
    windows_mastermind_2 = tk.Tk()
    label = tk.Label(windows_mastermind_2,
                     text=f'You got {good} good color(s) at the right place, {mid} good color(s) at the wrong place, and {false} bad color(s)')
    label.pack()
    quit_button = tk.Button(windows_mastermind_2, text='OK', command=windows_mastermind_2.destroy)
    quit_button.pack()
    windows_mastermind_2.mainloop()


def Result_good():
    windows_mastermind_2 = tk.Tk()
    label = tk.Label(windows_mastermind_2, text='You got 4 good colors in the right place, you won!')
    label.pack()
    quit_button = tk.Button(windows_mastermind_2, text='OK', command=windows_mastermind_2.quit)
    quit_button.pack()
    windows_mastermind_2.mainloop()

def code_check(code, code_secret):
    good = 0
    mid = 0

    if code == code_secret:
        Result_good()
        exit()
    else:
        for i in range(4):
            if code[i] == code_secret[i]:
                good += 1

        # Create a list of counts for colors
        code_count = {}
        secret_count = {}

        for i in range(4):
            # Count occurrences of each color in the player's guess
            if code[i] in code_count:
                code_count[code[i]] += 1
            else:
                code_count[code[i]] = 1

            # Count occurrences of each color in the secret code
            if code_secret[i] in secret_count:
                secret_count[code_secret[i]] += 1
            else:
                secret_count[code_secret[i]] = 1

        # Calculate mid (right color but wrong position)
        for color in code_count:
            if color in secret_count:
                mid += min(code_count[color], secret_count[color])

        mid -= good  # Adjust mid count

        false = 4 - mid - good  # Calculate false colors
        Result_bad(good, mid, false)

color1 = ''
color2 = ''
color3 = ''
color4 = ''

code_secret = Code()

for _ in range(8):
    code = Code()
    code_check(code, code_secret)
