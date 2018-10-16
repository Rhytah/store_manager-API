class Config:
    DEBUG=False
    #APP_SECRET = 'andela'

class DevelopmentConfig(Config):
    DEBUG=True

class TestingConfig(Config):
    DEBUG=True

app_configuration = {
    "development":DevelopmentConfig,
    "testing":TestingConfig
}