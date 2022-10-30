import yaml

with open('config.yml', 'r',encoding="utf-8") as yml:
    config = yaml.safe_load(yml) #連想配列(辞書型)として取得できる。
    print(config)
