from read_data import read_data
from sklearn import tree
import operator

def get_decision_tree_data(cust_dict = {}):
    training_data = []
    if len(cust_dict) > 0:
        c_balances = []
        s_balances = []
        decision = []
        for masked_id in cust_dict:
            if cust_dict[masked_id].get_checking_status() != '':
                c_balances.append(cust_dict[masked_id].get_check_balances())
                s_balances.append(cust_dict[masked_id].get_sav_balances())
                decision.append(cust_dict[masked_id].get_checking_status())
        training_data.append(c_balances)
        training_data.append(s_balances)
        training_data.append(decision)
    return training_data


def create_decision_tree():
    #gets the customer list w preprocessed data -> {1 : c, 2: c,...}
    customer_list = read_data()
    train_data = get_decision_tree_data(customer_list)
    check_bal = train_data[0]
    sav_bal = train_data[1]
    decision = train_data[2]

    model = tree.DecisionTreeClassifier()
    model.fit(check_bal, decision)

    #predict = model.predict([df[2].get_check_balances()])

    for masked_id in customer_list:
        if customer_list[masked_id].get_checking_status() == '':
            predict = model.predict([customer_list[masked_id].get_check_balances()])
            customer_list[masked_id].checking_status = predict[0]

    model.fit(sav_bal, decision)

    for masked_id in customer_list:
        if customer_list[masked_id].get_checking_status() == 'close an account':
            predict = model.predict([customer_list[masked_id].get_sav_balances()])
            customer_list[masked_id].checking_status = predict[0]

    for masked_id in customer_list:
        customer_list[masked_id].pref_contact_medium = max(customer_list[masked_id].contact_mediums, key = operator.itemgetter(1))[0]


    for masked_id in customer_list:
        print(masked_id)
        print('\t c_balances: ' + str(customer_list[masked_id].get_check_balances()))
        print('\t s_balances: ' + str(customer_list[masked_id].get_sav_balances()))
        print('\t' + str(customer_list[masked_id].get_checking_status()))

def print_data_report(c_list):
    for masked_id in c_list:







create_decision_tree()