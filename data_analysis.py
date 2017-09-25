from read_data import read_data
from sklearn import tree

#file where the decision tree information will print to
output_file = 'custom_report.txt'
training_data_for_print = read_data()
#breaks up data to fit the DecisionTreeClassifier().fit
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
'''
1) Makes a prediction to open/close a checking account based off of customers' checking balances
    a) This data is taken from the original customers who closed an account over the 6 months,
        will be able to refine when sample size is larger
2) If prediction is 'close an account', it will make a prediction again based off of customers' saving balances
3) Prints all this data to a file, along with their preferred contact method.
'''
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
        customer_list[masked_id].pref_contact_medium = max(customer_list[masked_id].contact_mediums, key = customer_list[masked_id].contact_mediums.get)


    print_data_report(c_list = customer_list, file_name = output_file, train_data = training_data_for_print)
'''
prints data from decision tree to file_name
@params: file_name is passed from create_decision_tree() -> output_file
        c_list is the customer list, passed from create_decision_tree()
'''
def print_data_report(c_list = {}, file_name = '', print_training_data = True, train_data = {}):
    if (len(c_list) > 0) and (file_name != ''):
        f = open(file_name, 'w')

        if print_training_data:
            f.write('TRAINING DATA USED:\n')
            for masked_id in train_data:
                if train_data[masked_id].get_checking_status() != '':
                    f.write('\t[masked_id: %s, age: %s]\n' % (masked_id, c_list[masked_id].age))
                    f.write('\t\tchecking_balances: ' + str(c_list[masked_id].get_check_balances()) + '\n')
                    f.write('\t\tsavings_balances: ' + str(c_list[masked_id].get_sav_balances()) + '\n')
                    f.write('\t[Decision: %s]\n\n' % c_list[masked_id].get_checking_status())
            f.write('\n\n')

        f.write('PREDICTIONS MADE BY DECISION TREE:\n')
        for masked_id in c_list:
            f.write('\t[masked_id: %s, age: %s]\n' % (masked_id, c_list[masked_id].age))
            f.write('\t\tcheckings_balances: ' + str(c_list[masked_id].get_check_balances()) + '\n')
            f.write('\t\tsavings_balances: ' + str(c_list[masked_id].get_sav_balances()) + '\n')
            f.write('\t[Decision: %s]\n' % (c_list[masked_id].get_checking_status()))
            f.write('\t[Preferred contact method: %s]\n\n' % c_list[masked_id].pref_contact_medium[:-4])
        f.close()





create_decision_tree()