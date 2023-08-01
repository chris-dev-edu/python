class BankAccount:
    def __init__(self, account_number, owner, balance=0, password=None):
        self.account_number = account_number
        self.owner = owner
        self.balance = balance
        self.password = password

    def deposit(self, amount, password):
        if self.check_password(password):
            self.balance += amount
            print(f"{self.owner}님의 계좌({self.account_number})에 {amount}원이 입금되었습니다. 현재 잔액: {self.balance}원")
        else:
            print("비밀번호가 틀렸습니다. 입금이 취소되었습니다.")

    def withdraw(self, amount, password):
        if self.check_password(password):
            if amount > self.balance:
                print("잔액이 부족합니다.")
            else:
                self.balance -= amount
                print(f"{self.owner}님의 계좌({self.account_number})에서 {amount}원이 출금되었습니다. 현재 잔액: {self.balance}원")
        else:
            print("비밀번호가 틀렸습니다. 출금이 취소되었습니다.")

    def transfer(self, other_account, amount, password):
        if self.check_password(password):
            if amount > self.balance:
                print("잔액이 부족합니다.")
            else:
                self.balance -= amount
                other_account.balance += amount
                print(f"{self.owner}님의 계좌({self.account_number})에서 {other_account.owner}님의 계좌({other_account.account_number})로 {amount}원이 이체되었습니다.")
                print(f"{self.owner}님의 현재 잔액: {self.balance}원, {other_account.owner}님의 현재 잔액: {other_account.balance}원")
        else:
            print("비밀번호가 틀렸습니다. 이체가 취소되었습니다.")

    def get_balance(self):
        return self.balance

    def get_account_info(self):
        return f"계좌 번호: {self.account_number}, 소유자: {self.owner}, 잔액: {self.balance}원"

    def check_password(self, password):
        return self.password == password


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
