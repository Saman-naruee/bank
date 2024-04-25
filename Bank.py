import csv
from time import sleep
############################# FKUNCTION'S #############################
def give_me_file_path(path = 'datafile.txt'):
    return path
class Main():
    def __init__(self, d = None):
        self.bank = Bank()
        # for that time you want to import onother file...
                
    def run(self, data):
        self.data = data
        while True:
            user_ = str(input('...\nwhat can I do?(1,2,3,4):\n1.Make an account\n2.Diposit\n3.withdrow\n4.transfer\n'))
            if user_ == '1':
                nam = input('Enter your name:')
                pas = input('Enter your pass:')
                self.bank.add_account(nam, pas)
            elif user_ == '2':
                self.data = list(self.bank.deposit(self.bank.read_data()))
                self.bank.bank_write_data(self.data )
            elif user_ == '3':
                self.data = list(self.bank.withdraw(self.bank.read_data()))
                self.bank.bank_write_data(self.data)
            elif user_ == '4':
                self.data = list(self.bank.transfer(self.bank.read_data()))
                self.bank.bank_write_data(self.data)
            else:
                print('wrong input!')
                if user_ == '':
                    break
        return self.data
    def write_data(self, data):
        with open(give_me_file_path(), 'w') as file:
            for line in data:
                for ele in line:
                    file.write(str(ele) +',')
                file.write('\n')


def main():
    for word in 'Hello! and wellcome to online bank app'.split():
        print(word, end=' ')
        sleep(0.2)
    main_program = Main()
    data = main_program.bank.read_data()
    final_data = main_program.run(data)
    main_program.write_data(final_data)

class Account:
    def __init__(self, name, number, password):
        self.name = name
        self.balance = 0
        self.account_number = number
        self.password = password

    def show_info(self):
        # {"Name" : self.name , "Account number" : self.account_number, "Balance" : self.balance, "Password" : self.password}
        print(f'your account created:\nname:{self.name}\naccount number: {self.account_number}\nbalance: {self.balance}$\npassword: {self.password}\n')
        return f'{self.name},{self.account_number},{self.balance},{self.password}'
class Bank:
    def __init__(self):
        self.accounts = []
        self.last_account_number = 5859831084020000

    def add_account(self, name, password):
        self.last_account_number += 1
        acc = Account (name, self.last_account_number ,password) #    
        self.accounts.append(acc.show_info())
        with open(give_me_file_path(), '+a') as file:
            for acount in self.accounts:
                file.write(acount)
                file.write('\n')
    
    def bank_write_data(self, data):
        with open(give_me_file_path(), 'w') as file:
            for line in data:
                for ele in line:
                    file.write(str(ele) +',')
                file.write('\n')

    def read_data(self):
        # csv.reader("")
        list_data = []
        with open(give_me_file_path()) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                list_data.append(row)
        return list((list_data))
    def show_all_accounts(self):
        for account in self.accounts:
            print(account)

    def deposit(self, data) -> list:
        self.user_input_pass = str(input('Enter your password: '))
        self.ac_num = str(input('Enter your account number:'))
        for line in range(len(data)):
            if str(data[line][1]) == self.ac_num and str(data[line][3]) == self.user_input_pass:
                self.amount = input('Enter your amount: ')
                data[line] = [data[line][0], self.ac_num, int(data[line][2]) + int(self.amount), self.user_input_pass]
                print(f'Your balance updated: ---> {int(data[line][2] )}')
                return data
        print('Your account doesnt found!')
        return data
    
    def withdraw(self, data):
        self.user_input_pass = str(input('Enter your password: '))
        self.ac_num = input('Enter your account number:')
        for line in range(len(data)):
            if data[line][1] == self.ac_num and data[line][3] == self.user_input_pass:
                self.amount = input('Enter your amount: ')
                if int(data[line][2]) < int(self.amount):
                    print('Not enough money!')
                    break
                data[line] == [data[line][0], self.ac_num, int(data[line][2] - self.amount), self.user_input_pass]
                print(f'Your balance updated: {data[line][2]} ---> {int(data[line][2] - self.amount)}')
                return data
        print('Your account doesnt found!')
        return data


        

with open(give_me_file_path(), 'w') as file:
    file.write('')
main()