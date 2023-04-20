import twint

config = twint.Config()

config.Search = "go to sleep forever"
config.Lang = "en"
config.Limit = 3
config.Since = "2023-04-01"
config.Until = "2023-04-20"
config.Store_csv = True
config.Output = "res.csv"
#running search
twint.run.Search(config)

