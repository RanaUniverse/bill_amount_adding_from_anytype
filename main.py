"""
I will make this script which will add easily
My bills values in total.
The input value can be the type of input value_variable i passed here.
"""

input_value = """
₹405
₹90
₹40
₹25
₹60  ₹25
₹10
"""

print(input_value)


normal_list = input_value.split()
print("Input Value's List is:", normal_list)

str_value_list: list[str] = []
for i in normal_list:
    i_value_only_str = i.removeprefix("₹")
    str_value_list.append(i_value_only_str)
print(str_value_list)


int_value_list: list[int] = []
for i in str_value_list:
    i_as_int = int(i)
    int_value_list.append(i_as_int)
print(int_value_list)

total_value = sum(int_value_list)
print(f"The Total Sum of {len(int_value_list)} Items is,", f"₹{total_value}")
