# "This calculator the power used for work"

# #Scenario 1
# """
# A man did a work of work_joules using time_secs, what is power used in watts?
# """
# # work_joules = float(input("Enter the workdone in joules: "))
# # time_secs = float(input("Enter the time spent in secs: "))
# # power = work_joules/time_secs
# # print(f"The power used is {power:.2f} WATTS")

# #Scenario 2

# """
# A man spent 1 hour to work do a work of 1000 joules, what is the power used"""
# # time_in_hour = 1  #Since time is reported in hour, we need to convert it to secs
# # time_in_secs = time_in_hour *60
# # work_joules = 1000
# # power = work_joules/time_in_secs
# # print(f'The total power used is {power:.2f} WATTS')

# #Scenario 3
# """
# This collects user input verify which time format is it and then performs operation"""
# time_decider = input("What format is the time reported as? ").lower().strip()

# while True:
#     work = int(input('Enter the workdone: '))
#     time_spent = int(input("Enter time spent: "))
#     if time_decider in ('h', 'hour'):
#         power = work/(time_spent * 60)
#         break
#     elif time_decider in ('d', 'day'):
#         power = work/(time_spent *60 *24)
#         break
#     else: 
#         time_decider= input('Enter the right format: ')
        
# print(f'The total power used is {power:.2f} WATTS')