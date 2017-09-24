import pandas as pd
from customer import customer


def read_data():
    customer_list = {}

    #reads csv into dataframe
    df = pd.read_csv('MonthEndBalances.csv')

    #creates a customer instance for each masked id
    for index, row in df.iterrows():
        if row['masked_id'] not in customer_list:
            c = customer()
            c.age = int(row['age'])
            c.id = row['masked_id']
            customer_list.update({int(row['masked_id']) : c})
    #splits the data to each customer
    for index, row in df.iterrows():
        customer_list.get(row['masked_id']).checking_acct_count.append(row['checking_acct_ct'])
        customer_list.get(row['masked_id']).checking_acct_balances.append("%.2f" % row['check_bal_altered'])
        customer_list.get(row['masked_id']).savings_acct_balances.append("%.2f" % row['sav_bal_altered'])
        if 'branch_visit_cnt' not in customer_list.get(row['masked_id']).contact_mediums:
            customer_list.get(row['masked_id']).contact_mediums.update({'branch_visit_cnt' : [row['branch_visit_cnt']]})
        else:
            customer_list.get(row['masked_id']).contact_mediums['branch_visit_cnt'].append(row['branch_visit_cnt'])

        if 'phone_banker_cnt' not in customer_list.get(row['masked_id']).contact_mediums:
            customer_list.get(row['masked_id']).contact_mediums.update({'phone_banker_cnt': [row['phone_banker_cnt']]})
        else:
            customer_list.get(row['masked_id']).contact_mediums['phone_banker_cnt'].append(row['phone_banker_cnt'])

        if 'mobile_bank_cnt' not in customer_list.get(row['masked_id']).contact_mediums:
            customer_list.get(row['masked_id']).contact_mediums.update({'mobile_bank_cnt': [row['mobile_bank_cnt']]})
        else:
            customer_list.get(row['masked_id']).contact_mediums['mobile_bank_cnt'].append(row['mobile_bank_cnt'])

        if 'online_bank_cnt' not in customer_list.get(row['masked_id']).contact_mediums:
            customer_list.get(row['masked_id']).contact_mediums.update({'online_bank_cnt': [row['online_bank_cnt']]})
        else:
            customer_list.get(row['masked_id']).contact_mediums['online_bank_cnt'].append(row['online_bank_cnt'])

        if 'direct_mail_cnt' not in customer_list.get(row['masked_id']).contact_mediums:
            customer_list.get(row['masked_id']).contact_mediums.update({'direct_mail_cnt': [row['direct_mail_cnt']]})
        else:
            customer_list.get(row['masked_id']).contact_mediums['direct_mail_cnt'].append(row['direct_mail_cnt'])

        if 'direct_email_cnt' not in customer_list.get(row['masked_id']).contact_mediums:
            customer_list.get(row['masked_id']).contact_mediums.update({'direct_email_cnt': [row['direct_email_cnt']]})
        else:
            customer_list.get(row['masked_id']).contact_mediums['direct_email_cnt'].append(row['direct_email_cnt'])

        if 'direct_phone_cnt' not in customer_list.get(row['masked_id']).contact_mediums:
            customer_list.get(row['masked_id']).contact_mediums.update({'direct_phone_cnt': [row['direct_phone_cnt']]})
        else:
            customer_list.get(row['masked_id']).contact_mediums['direct_phone_cnt'].append(row['direct_phone_cnt'])

    return customer_list

#read_data()