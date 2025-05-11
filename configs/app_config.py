class Config:
    """ Simple parent Class to hold possible configuration variables"""
    SECRET_KEY = "possibleSecretKey"
    DEBUG = False


class DevelopmentConfig(Config):
    """ Class to hold possible development configuration variables. DEBUG value is to capture change"""
    DEBUG = True