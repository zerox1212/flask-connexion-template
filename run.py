""" Commissioning.IO Web App - V0.3 - © 2018 Split Rock Software LLC"""

from cioapp import create_app


if __name__ == "__main__":
    app = create_app('cioapp.settings.DevConfig')
    app.run()
else:
    app = create_app('cioapp.settings.ProdConfig')
