import os


def execute_selected_simulation(model: str) -> None:

	cwd = os.getcwd()	

	folders = ["examples", "models"]

	root_path = os.sep.join(os.getcwd().split(os.sep)[:-1])

	paths = map(lambda folder: os.path.join(root_path, folder), folders)

	path = next(filter(lambda path: model in os.listdir(path), paths), None)

	path_model = os.path.join(path, model)

	sh_file = next(filter(lambda file: ".sh" in file, os.listdir(path_model)), None)
	
	os.chdir(path_model)

	os.system(f'./{sh_file}')
	
	os.chdir(cwd)	


def write_simulation_results_in_results_html(model: str) -> None:

	path_interface = os.getcwd()	

	folders = ["examples", "models"]

	root_path = os.sep.join(os.getcwd().split(os.sep)[:-1])

	paths = map(lambda folder: os.path.join(root_path, folder), folders)

	path = next(filter(lambda path: model in os.listdir(path), paths), None)

	path_model_results = os.path.join(path, model, "results")

	html_results_file = next(filter(lambda file: ".html" in file, os.listdir(path_model_results)), None)

	path_html_results_ecos_file = os.path.join(path_model_results, html_results_file)

	path_html_results_web_file = os.path.join(path_interface, 'pages', 'results', 'results.html')

	with open(path_html_results_ecos_file, 'r') as f_html_ecos:		

		with open(path_html_results_web_file, 'w') as f_html_web:

			f_html_web.writelines(f_html_ecos.readlines())