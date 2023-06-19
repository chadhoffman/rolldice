import pynecone as pc

class RolldiceConfig(pc.Config):
    pass

config = RolldiceConfig(
    app_name="rolldice",
    db_url="sqlite:///pynecone.db",
    env=pc.Env.DEV,
)