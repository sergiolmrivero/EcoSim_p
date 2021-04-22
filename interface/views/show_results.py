from flask import Blueprint, render_template


show_results_blueprint = Blueprint('show_results', __name__)

@show_results_blueprint.route('/', methods=['GET', 'POST'])
def show_result():
    """
    Render the html returned of the R markdown
    """
    return render_template('/show_results/show_results.html')
