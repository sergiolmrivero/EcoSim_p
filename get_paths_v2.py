import os
import sys

os.chdir(os.path.dirname(__file__))
print(f'cwd: {os.getcwd()}')


def get_paths(model_name_from_json):

    dir_separator = os.sep
    di_directory_paths = dict()
    di_directory_paths['kernel'] = os.getcwd()
    di_directory_paths['Ecos_p'] = dir_separator.join(di_directory_paths['kernel'].split(sep=dir_separator)[:-1])
    di_directory_paths['examples'] = os.path.join(di_directory_paths['Ecos_p'], 'examples')
    di_directory_paths['master'] = dir_separator.join(di_directory_paths['Ecos_p'].split(sep=dir_separator)[:-1])
    di_directory_paths['interface'] = os.path.join(di_directory_paths['Ecos_p'], 'interface')

    di_directory_model_paths = dict()
    di_kernel_file_paths = dict()
    di_interface_file_paths = dict()
    di_models_file_paths = dict()
    di_model_agent_classes = dict()

    for sub_dir in os.listdir(di_directory_paths['examples']):
        if model_name_from_json in sub_dir:
            di_directory_model_paths[sub_dir] = os.path.join(di_directory_paths['examples'], sub_dir)
        else:
            di_directory_paths[sub_dir] = os.path.join(di_directory_paths['examples'], sub_dir)

    # KERNEL FILES
    for file in os.listdir(di_directory_paths['kernel']):
        if not '__init__' in file:
            di_kernel_file_paths[file] = os.path.join(di_directory_paths['kernel'], file)

    # INTERFACE FILES
    for file in os.listdir(di_directory_paths['interface']):
        if not '__init__' in file:
            di_interface_file_paths[file] = os.path.join(di_directory_paths['interface'], file)

    # MODELS FILES
    for model, path in di_directory_model_paths.items():
        di_models_file_paths[model] = dict()
        for file in os.listdir(di_directory_model_paths[model]):
            if not '__init__' in file:
                di_models_file_paths[model][file] = os.path.join(di_directory_model_paths[model], file)

        if not model == 'dumb_model':
            di_model_agent_classes[model] = {}
            try:
                for agent_class_file in os.listdir(os.path.join(di_directory_model_paths[model], 'agents_classes')):
                    if not '__init__' in agent_class_file:
                        di_model_agent_classes[model][agent_class_file] = (os.path.join(di_directory_model_paths[model], 'agents_classes', agent_class_file))

            except FileNotFoundError:
                print('There is no file on {} directory'.format(os.path.join(di_directory_model_paths[model], 'agents_classes')))
                pass

    print('\nDIRECTORIES')
    for key, value in di_directory_paths.items():
        print(key, value)
        sys.path.append(value)

    print('\nMODELS')
    for key, value in di_directory_model_paths.items():
        print(key, value)
        sys.path.append(value)

    for model in di_models_file_paths.keys():

        print(f'\nAGENTS CLASSES OF MODEL {model}')
        if not model == 'dumb_model':
            for key, value in di_model_agent_classes[model].items():
                print(key, value)
                sys.path.append(value)

        print(f'\nFILES FROM MODEL {model}')
        for key, value in di_models_file_paths[model].items():
            print(key, value)
            sys.path.append(value)

    print(f'\nFILES FROM INTERFACE')
    for key, value in di_interface_file_paths.items():
        print(key, value)
        sys.path.append(value)

    print('\nFILES FROM KERNEL')
    for key, value in di_kernel_file_paths.items():
        print(key, value)
        sys.path.append(value)

    # print('\n\n')
    # print(di_model_agent_classes)
    # return [di_directory_paths, di_directory_model_paths, di_kernel_file_paths, di_interface_file_paths,
    # di_models_file_paths]


# get_paths('dumb_model')
get_paths('macro_model')
print('\n\nPATH')
for path in sys.path:
    print(path)
