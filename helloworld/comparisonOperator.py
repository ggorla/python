Weight = int(input('Weight :'))
unit = input('Lbs or Kgs')
if unit.upper() =='L':
   converted =  Weight*0.45
   print(f"you are {converted} kilos")
elif unit.upper()=='K':
    converted = Weight
    print(f"your {converted}")