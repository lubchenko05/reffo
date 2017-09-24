from matrix_client.client import MatrixClient


def send_post(post):
    client = MatrixClient("http://localhost:8008")
    # Existing user
    token = client.login_with_password(username="foobar", password="monkey")
    room = client.create_room("my_room_alias")
    room.send_text(f"{post.title}\n\n{post.text}\n\n{post.owner}")