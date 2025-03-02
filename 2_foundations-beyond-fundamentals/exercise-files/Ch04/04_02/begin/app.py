first_name = 'malala'
last_name = 'yousafzai'
note = 'award: Nobel Peace Prize'

first_name_cap = first_name.capitalize()
print(first_name_cap)

last_name_cap = last_name.capitalize()
print(last_name_cap)

award_location = note.find('award: ')
print(award_location) # 0 (the index where the text is)

award_text = note[7:] # stringtoslice[start:end]
print(award_text)