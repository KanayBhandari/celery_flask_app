class Config:
    DEBUG = False


class DevConfig(Config):
    DEBUG = True


app_config = {
    'dev': DevConfig,
}
