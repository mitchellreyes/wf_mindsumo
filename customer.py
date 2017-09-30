class customer():
    def __init__(self, m_id = 0, d_age = 0):
        self.masked_id = m_id
        self.age = d_age
        #checking_acct_ct
        self.checking_status = ''
        self.pref_contact_medium = ''
        self.checking_acct_count = []
        #checking acct balances
        self.checking_acct_balances = []
        #savings acct balances
        self.savings_acct_balances = []

        self.contact_mediums = {}

    def get_checking_account_count(self):
        return self.checking_acct_count
    def get_check_balances(self):
        return self.checking_acct_balances
    def get_checking_status(self):
        return self.checking_status
    def get_sav_balances(self):
        return self.savings_acct_balances