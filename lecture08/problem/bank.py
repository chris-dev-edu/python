class BankAccount:
    def __init__(self, account_number, owner, balance=0, password=None):

    def deposit(self, amount, password):

    def withdraw(self, amount, password):

    def transfer(self, other_account, amount, password):

    def get_balance(self):

    def get_account_info(self):

    def check_password(self, password):


# 은행 계좌 객체 생성
account1 = BankAccount("123-456-789", "Alice", 10000, "1234")
account2 = BankAccount("987-654-321", "Bob", 5000, "5678")

# 계좌 정보 출력
print(account1.get_account_info())
print(account2.get_account_info())

# 비밀번호를 틀리게 입력하여 입금, 출금, 이체 시도
account1.deposit(3000, "1111")
account1.withdraw(2000, "1111")
account1.transfer(account2, 5000, "1111")

# 올바른 비밀번호를 입력하여 입금, 출금, 이체
account1.deposit(3000, "1234")
account1.withdraw(2000, "1234")
account1.transfer(account2, 5000, "1234")
