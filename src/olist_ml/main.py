from hydra import main
from olist_ml.config import OlistConfig
from olist_ml.data import main as prepare_data

@main(config_path="../../../conf", config_name="config", version_base=None)
def main(cfg: OlistConfig) -> None:
    prepare_data()
if __name__ == "__main__":
    main()