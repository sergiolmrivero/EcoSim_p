from flask import Blueprint, render_template

parametrization_blueprint = Blueprint('parametrization', __name__)

@parametrization_blueprint.route('/', methods=['GET'])
def parametrization():
	"""
	Route to render the parametrization page
	"""

	return render_template('/parametrization/parametrization.html')
