# --------------
# Importing header files
import numpy as np

# Path of the file has been stored in variable called 'path'

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

data = np.genfromtxt(path, delimiter=",", skip_header=1)
print(data)

census = np.concatenate((data, np.array(new_record)), axis=0)

#Code starts here



# --------------
#Code starts here

age = census[:, 0]

max_age = np.max(age)

min_age = np.min(age)

age_mean = np.mean(age)

age_std = np.std(age)



# --------------
#Code starts here

race_0 = census[census[:, 2] == 0]
race_1 = census[census[:, 2] == 1]
race_2 = census[census[:, 2] == 2]
race_3 = census[census[:, 2] == 3]
race_4 = census[census[:, 2] == 4]

len_0 = race_0[:, [2]].size
len_1 = race_1[:, [2]].size
len_2 = race_2[:, [2]].size
len_3 = race_3[:, [2]].size
len_4 = race_4[:, [2]].size

dic = {0: len_0, 1: len_1, 2: len_2, 3: len_3, 4: len_4}
minority_race = min(dic, key=dic.get)




# --------------
#Code starts here

senior_citizens = census[census[:, 0] > 60]
working_hours_sum = np.sum(senior_citizens[:, 6])

senior_citizens_len = senior_citizens[:, 0].size

avg_working_hours = working_hours_sum / senior_citizens_len

print(avg_working_hours)


# --------------
#Code starts here

high = census[census[:, 1] > 10]
low = census[census[:, 1] <= 10]


avg_pay_high = np.mean(high[:, 7])
avg_pay_low = np.mean(low[:, 7])


