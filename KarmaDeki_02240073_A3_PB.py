import unittest
from KarmaDeki_02240073_A3_PA import BankAccount, PersonalAccount, BusinessAccount, BankingSystem, LoginError   

class TestBankingSystem(unittest.TestCase):

    def setUp(self):
        self.bank = BankingSystem()
        self.personal = self.bank.create_account("1")
        self.business = self.bank.create_account("2")

    def test_deposit_negative_amount(self):
        result = self.personal.deposit(-100)
        self.assertEqual(result, "OH HO! Invalid amount.")

    def test_withdraw_zero(self):
        result = self.personal.withdraw(0)
        self.assertEqual(result, "SORRY! Insufficient funds.")

    def test_topup_invalid_number(self):
        self.personal.funds = 100
        result = self.personal.topup_mobile("123", 10)
        self.assertEqual(result, "Invalid number or amount.")

    def test_login_invalid_credentials(self):
        with self.assertRaises(LoginError):
            self.bank.login("99999", "1234")

    def test_transfer_to_nonexistent_account(self):
        fake_recipient = PersonalAccount("00000", "0000")
        result = self.personal.transfer(50, fake_recipient)
        self.assertEqual(result, "OOPS! Transfer failed.")

    # 3. Testing individual main methods
    def test_valid_deposit(self):
        self.personal.funds = 0
        result = self.personal.deposit(100)
        self.assertEqual(result, "Your deposit was successful.")
        self.assertEqual(self.personal.funds, 100)

    def test_valid_withdraw(self):
        self.personal.funds = 200
        result = self.personal.withdraw(150)
        self.assertEqual(result, "Your withdrawal was successful.")
        self.assertEqual(self.personal.funds, 50)

    def test_insufficient_funds_withdraw(self):
        self.personal.funds = 20
        result = self.personal.withdraw(50)
        self.assertEqual(result, "SORRY! Insufficient funds.")

    def test_successful_transfer(self):
        self.personal.funds = 200
        result = self.personal.transfer(50, self.business)
        self.assertEqual(result, "Successfully transfered.")  

    def test_successful_topup(self):
        self.personal.funds = 100
        result = self.personal.topup_mobile("12345678", 50)
        self.assertEqual(result, "Mobile 12345678 topped up with 50.")
        self.assertEqual(self.personal.funds, 50)

if __name__ == '__main__':
    unittest.main()
