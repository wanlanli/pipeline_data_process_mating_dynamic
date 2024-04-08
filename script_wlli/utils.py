import yaml
from cellmating.config_yml import ExperimentOptions


def load_configs(path: str) -> ExperimentOptions:
    """
    Loads experimental configuration from a YAML file and converts it into a Python object for further processing.
    This function allows users to define experiment parameters externally in a YAML file, offering a convenient
    way to manage and adjust configurations without altering the codebase.

    Parameters:
    ----------
    path : str
        The file path to the experiment configuration YAML file.

    Returns:
    ----------
    ExperimentOptions
        An object representing the loaded configuration, providing programmatic access to the defined experiment
        parameters.

    Example YAML Format:
    --------------------
    Consider the YAML file follows a structure like this:

        experiment_name: MyExperiment
        image_options:
            dimention: "TCWH"
            resolution:
                data_01:
                    reso: 0.2
                    bin: 2
                data_02:
                    reso: 0.4
                    bin: 1
        measure_options:
            contours_length: 60
        tracker_options:
            feature_dimention: 8

    Notes:
    -----
    - Ensure the YAML file's structure matches the expectations of the `ExperimentOptions` class to avoid issues
      during loading and accessing the configuration properties.
    """
    with open(path, 'r') as yamlfile:
        data = yaml.load(yamlfile, Loader=yaml.FullLoader)
    config = ExperimentOptions(data)
    return config
