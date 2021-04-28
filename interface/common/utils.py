import os


def execute_selected_simulation(model: str) -> None:

	cwd = os.getcwd()
	print('cwd: ', cwd)

	folders = ["examples", "models"]

	root_path = os.sep.join(os.getcwd().split(os.sep)[:-1])

	paths = map(lambda folder: os.path.join(root_path, folder), folders)

	path = next(filter(lambda path: model in os.listdir(path), paths), None)

	path_model = os.path.join(path, model)

	sh_file = next(filter(lambda file: ".sh" in file, os.listdir(path_model)), None)

	# os.system(f'cd {path_model}')
	os.chdir(path_model)

	os.system(f'./{sh_file}')

	# os.system(f'cd {cwd}')
	os.chdir(cwd)

	print('Ends')
