from flask import Blueprint, request, render_template
from common.utils import execute_selected_simulation
from common.utils import write_simulation_results_in_results_html
from common.utils import generate_zip_csv_result


simulation_blueprint = Blueprint('simulation', __name__)

@simulation_blueprint.route("/execution", methods=['GET', 'POST'])
def execution():
    """
    Execute the simulation
    """

    if request.method == 'POST':

        model = request.form['model']

        execute_selected_simulation(model)

        write_simulation_results_in_results_html(model)

        generate_zip_csv_result(model)        

    return render_template('/results/results.html')
