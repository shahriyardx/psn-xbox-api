from quart import Quart
from quart_cors import cors

from .blueprints.psn import psn_bp
from .blueprints.xbox import xbox_bp

app = cors(Quart(__name__), allow_origin="*", allow_headers="*", allow_methods="*")

app.register_blueprint(psn_bp)
app.register_blueprint(xbox_bp)
