import os

import pandas as pd

from cellmating.cells import create_cells_from_image
from cellmating.mating import Mating


def extract_mating_features(image, g, key: int, granularity: int = 10):
    """
    Extracts mating cell features from a time-lapse movie (image), focusing on the specified cell and its potential
    mating partners based on their division and fusion relationships within a cell generation network (g). The analysis
    spans from a defined start time to the point of cell fusion, with measurements taken at specified intervals
    (granularity).

    Parameters:
    -----------
    image : np.ndarray
        A 4D numpy array representing the mating movie, with dimensions [Time, Channel, Width, Height]. The tracked
        images are included in the last channel, providing visual data for feature extraction.

    g : networkx.Graph
        The generation network graph of cells, which is used to label and understand division and fusion relationships.
        This network should encode the lineage and interactions between cells over time.

    key : int
        The identifier (ID) of the central, fusioned cell for which the analysis is to be conducted. This ID should
        correspond to a node in the generation network `g` that represents the cell of interest.

    granularity : int, optional
        The granularity of time measurements, indicating the step length in time units between the start and end points
        of the analysis. The start time is determined by the earliest time at which parent cells exist, and the end time
        is the fusion time point of the central cell. Defaults to 10.

    Returns:
    ----------
    pd.DataFrame
        A DataFrame containing the features of the central cell's parent cells and potential mating partners. The
        features are structured to facilitate analysis of mating behaviors and cell interactions over the specified
        time span.

    Notes:
    -----
    The extraction of features and the construction of the DataFrame depend on the tracked image data and the
    structure of the cell generation network.
    """

    feature_time_point = {}
    cells = create_cells_from_image(image[:, -1], g)
    c_mating = Mating(image=image, cells=cells, center=key, g=g)

    start_time = min(cells[c_mating.p].start, cells[c_mating.m].start)
    end_time = max(cells[c_mating.p].end, cells[c_mating.m].end)

    for flag, time in enumerate(range(end_time, start_time, -granularity)):
        data = c_mating.center_cells_potential_pairs(time)
        if data is not None:
            if '-'+str(flag) not in feature_time_point.keys():
                feature_time_point['-'+str(flag)] = None
            feature_time_point['-'+str(flag)] = pd.concat([feature_time_point['-'+str(flag)], data])

    data = c_mating.center_cells_potential_pairs(start_time)
    if data is not None:
        if 'start' not in feature_time_point.keys():
            feature_time_point['start'] = None
        feature_time_point["start"] = pd.concat([feature_time_point["start"], data])
    return feature_time_point


def stack_features(all_data: dict = {}, data: dict = {}, name: str = ""):
    for key in data.keys():
        if not data[key].empty:
            data[key]["image"] = os.path.basename(name)
            if key not in all_data.keys():
                all_data[key] = data[key]
            else:
                all_data[key] = pd.concat([all_data[key], data[key]])
    return all_data
