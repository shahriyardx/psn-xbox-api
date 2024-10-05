from quart import Blueprint, request
from utils.psn import send_message, get_profile

psn_bp = Blueprint("psn", __name__, url_prefix="/playstation")


@psn_bp.route("/profile/<string:username>/", methods=["GET"])
async def profile(username):
    headers = request.headers
    authorization = headers.get("Authorization")

    data = get_profile(authorization, username)
    return data


@psn_bp.route("/message/<string:username>/", methods=["POST"])
async def message(username):
    headers = request.headers
    authorization = headers.get("Authorization")

    body = await request.json
    message = body.get("message")

    data = send_message(authorization, username, message)
    return data
