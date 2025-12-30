from hydra import main
from olist_ml.config import OlistConfig
from olist_ml.pipelines.extract.pipeline import run_pipeline

@main(config_path="../../../conf", config_name="config", version_base=None)
def main(cfg: OlistConfig) -> None:
    run_pipeline(cfg=cfg)

if __name__ == "__main__":
    main()