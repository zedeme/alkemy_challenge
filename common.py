import yaml

__config = None

# Obtiene las config de los archivos yaml
def config():
        if not __config:
            with open("config.yaml") as f:
                config = yaml.safe_load(f)
        return config

def config_data():
        if not __config:
            with open("data_config.yaml") as f:
                config = yaml.safe_load(f)
        return config