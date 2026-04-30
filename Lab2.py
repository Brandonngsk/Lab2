def display_main_menu():
    print("display_main_menu()")
    print("Enter some numbers separated by commas (e.g. 5, 67, 32): ")
    
def get_user_input():
   x = input()
   x = x.split(",")
   float_list = []
   for num_str in x:
       float_list.append (float(num_str))
   return float_list

def calc_average_temperature(list_temp):
    avg = sum(list_temp) / len(list_temp)
    return avg

def calc_min_max_temperature(list_max_temp):
    maxxy = max(list_max_temp)
    minny = min(list_max_temp)
    print("maximum = ", maxxy , ",minimum= ", minny)
    
float_list = get_user_input()

average = calc_average_temperature(float_list)
print (average)

calc_min_max_temperature(float_list)