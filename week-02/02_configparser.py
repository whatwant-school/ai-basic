import configparser

if __name__ == '__main__':
    config = configparser.ConfigParser()
    config.sections()

    config.read('02_config.cfg')
    print(config.sections())

    for key in config['SectionOne']:
        value = config['SectionOne'][key]
        print(f"{key}  : {value}")
