from flask import Blueprint, render_template, request
from common.utils import execute_selected_simulation
from common.utils import write_simulation_results_in_results_html


simulation_blueprint = Blueprint('simulation', __name__)

@simulation_blueprint.route("/execution", methods=['GET', 'POST'])
def execution():
    """
    Execute the simulation
    """

    if request.method == 'POST':

        model = request.form['model']

        from pdb import set_trace
        set_trace()

        execute_selected_simulation(model)

        write_simulation_results_in_results_html(model)

    return render_template('/results/results.html')