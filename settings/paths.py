import pathlib

storageDir = pathlib.Path(__file__).parent.parent/"storage"
storageDir.mkdir(parents=True, exist_ok=True)

usersFile = storageDir / "users.json"
