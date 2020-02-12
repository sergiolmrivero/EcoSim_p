import os


def get_paths(is_print=True):

    di_directory_paths = dict()
    di_directory_paths['kernel'] = os.getcwd()
    di_directory_paths['Ecos_p'] = os.path.join(di_directory_paths['kernel'][:-7])
    di_directory_paths['examples'] = os.path.join(di_directory_paths['Ecos_p'], 'examples')
    di_directory_paths['master'] = os.path.join(di_directory_paths['Ecos_p'][:-7])

    di_directory_model_paths = dict()

    for sub_dir in os.listdir(di_directory_paths['examples']):
        if 'model' in sub_dir:
            di_directory_model_paths[sub_dir] = os.path.join(di_directory_paths['examples'], sub_dir)
        else:
            di_directory_paths[sub_dir] = os.path.join(di_directory_paths['examples'], sub_dir)

    if is_print:
        print('\nDIRECTORIES')
        for key, value in di_directory_paths.items():
            print(key, value)

        print('\nMODELS')
        for key, value in di_directory_model_paths.items():
            print(key, value)

    return di_directory_paths, di_directory_model_paths

get_paths()
