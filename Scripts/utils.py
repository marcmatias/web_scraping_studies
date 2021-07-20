#TODO pensar numa forma de puxar esses arquivos para o 

# Pandas utils
def add_new_row(data_frame, name_row, t_confirmado, t_obito):
    data_frame.loc[-1] = [name_row, t_confirmado, t_obito]  # adding a row
    data_frame.index = data_frame.index + 1  # shifting index
    return data_frame.sort_index()  # sorting by index