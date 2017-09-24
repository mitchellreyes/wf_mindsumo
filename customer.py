class customer():
    def __init__(self, m_id = 0, d_age = 0):
        self.masked_id = m_id
        self.age = d_age
        #checking_acct_ct
        self.checking_acct_count = []
        #checking acct balances
        self.checking_acct_balances = []
        #savings acct balances
        self.savings_acct_balances = []

        self.contact_mediums = {}
        #branch visits
        #phone_banker_cnt
        #mobile_bank_cnt
        #online_bank_cnt
        #direct_mail_cnt
        #direct_email_cnt
        #direct_phone_cnt