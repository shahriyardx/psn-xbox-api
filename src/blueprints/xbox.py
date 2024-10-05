from quart import Blueprint, request
from utils.xbox import send_message, get_profile

xbox_bp = Blueprint("xbox", __name__, url_prefix="/xbox")


@xbox_bp.route("/profile/<string:gamertag>/", methods=["GET"])
async def profile(gamertag):
    headers = request.headers
    authorization = headers.get("Authorization")

    data = await get_profile(authorization, gamertag)
    return data


@xbox_bp.route("/message/<string:gamertag>/", methods=["POST"])
async def message(gamertag):
    headers = request.headers
    authorization = headers.get("Authorization")

    body = await request.json
    message = body.get("message")

    data = await send_message(authorization, gamertag, message)
    return data
