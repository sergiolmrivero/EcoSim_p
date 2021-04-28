from flask import Blueprint, render_template, request
from common.utils import execute_selected_simulation


simulation_blueprint = Blueprint('simulation', __name__)

@simulation_blueprint.route("/execution", methods=['GET', 'POST'])
def simulation():
    """
    Execute the simulation
    """

    if request.method == 'POST':

        model = request.form['model']

        execute_selected_simulation(model)

    return render_template('/show_results/show_results.html')
