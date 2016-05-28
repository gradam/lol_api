def list_to_db_text(li):
	return '&&'.join(li)

def db_text_to_list(tips):
    return tips.split('&&')
