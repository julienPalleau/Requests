emps = {'emp1': {'name': 'Abe', 'position': {'office':'Mgr'},'home':'tenant'}, 'emp2': {'name': 'Bom', 'position': {'office':'Mgr'},'home':'tenant'}}

def generic_items(dict_or_list):
	if type(dict_or_list) is dict:
		return dict_or_list.items()
	if type(dict_or_list) is list:
		return enumerate(dict_or_list)
def get_keys(dictionary):
	result = []
	for key, value in generic_items(dictionary):
		if type(value) is dict or type(value) is list:
			new_keys = get_keys(value)
			result.append(key)
			for innerkey in new_keys:
				result.append(f'{key}/{innerkey}')
		else:
			result.append(key)
	return result

print(generic_items(emps))
print(get_keys(emps))

