# ui.py

import FreeSimpleGUI as sg
from models import Category, Transaction
from storage import load_data, save_data, get_transactions

def show_add_category_window(data):
    layout = [
        [sg.Text('Add New Category')],
        [sg.InputText(key='category')],
        [sg.Button('Add'), sg.Button('Cancel')]
    ]
    window = sg.Window('Add Category', layout)
    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Cancel'):
            break
        if event == 'Add':
            category = Category(values['category'])
            if category.is_valid() and category.name not in data['categories']:
                data['categories'].append(category.name)
                save_data(data)
                sg.popup('Category added successfully.')
            else:
                sg.popup_error('Invalid or duplicate category.')
            break
    window.close()

def show_add_transaction_window(data, trans_type, refresh_table_callback):
    if not data['categories']:
        sg.popup_error('Please add a category first.')
        return

    layout = [
        [sg.Text(f'Add {trans_type.capitalize()}')],
        [sg.InputText(key='title')],
        [sg.InputText(key='amount')],
        [sg.Combo(data['categories'], key='category', readonly=True)],
        [sg.Button('Add'), sg.Button('Cancel')]
    ]
    window = sg.Window(f'Add {trans_type.capitalize()}', layout)

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Cancel'):
            break
        if event == 'Add':
            try:
                amount = float(values['amount'])
            except ValueError:
                sg.popup_error('Amount must be a number.')
                continue

            transaction = Transaction(
                trans_type,
                values['title'],
                amount,
                values['category']
            )

            if transaction.is_valid():
                data['transactions'].append(transaction.to_dict())
                save_data(data)
                sg.popup(f'{trans_type.capitalize()} added successfully.')
                refresh_table_callback()
            else:
                sg.popup_error('Please complete all fields correctly.')
            break
    window.close()

def show_main_window():
    data = load_data()

    def refresh_table(window):
        transactions = get_transactions(data)
        table_data = [[t.title, t.amount, t.category, t.type] for t in transactions]
        window['table'].update(values=table_data)

    transactions = get_transactions(data)
    table_data = [[t.title, t.amount, t.category, t.type] for t in transactions]

    layout = [
        [sg.Text('Personal Finance Manager')],
        [sg.Table(values=table_data, headings=['Title', 'Amount', 'Category', 'Type'],
                  key='table', auto_size_columns=True, justification='center')],
        [sg.Button('Add Category'), sg.Button('Add Expense'), sg.Button('Add Income'), sg.Button('Exit')]
    ]

    window = sg.Window('Finance Manager', layout)

    while True:
        event, _ = window.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            break
        elif event == 'Add Category':
            show_add_category_window(data)
            refresh_table(window)
        elif event == 'Add Expense':
            show_add_transaction_window(data, 'expense', lambda: refresh_table(window))
        elif event == 'Add Income':
            show_add_transaction_window(data, 'income', lambda: refresh_table(window))

    window.close()
