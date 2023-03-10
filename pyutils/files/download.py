# ====================================================================================================================================
# @file       download.py
# @author     Krzysztof Pierczyk (krzysztof.pierczyk@gmail.com)
# @maintainer Krzysztof Pierczyk (krzysztof.pierczyk@gmail.com)
# @date       Friday, 16th December 2022 12:37:44 am
# @modified   Thursday, 22nd December 2022 3:07:11 am
# @project    py-utils
# @brief      General-use utilities for downloading files from the network
# 
# 
# @copyright Krzysztof Pierczyk © 2022
# ====================================================================================================================================

# ============================================================== Doc =============================================================== #

""" 

.. module:: 
   :platform: OS Independent
   :synopsis: General-use utilities for downloading files from the network

.. moduleauthor:: Krzysztof Pierczyk <krzysztof.pierczyk@gmail.com>

"""

# ============================================================ Imports ============================================================= #

from pathlib import Path
import requests
from pyutils.visuals.progressbars import StandardBar
from typing import Optional

# ============================================================ Functions =========================================================== #

def download_file(
    url : str,
    file : Path,
    chunk_size : int = 4096,
) :

    """Downloads content of @p url into a local @p file displaying pretty progress bar"""

    # Open connection to the server
    response = requests.get(url, stream=True)
    # Get length of the file to be downloaded
    total_length = int(response.headers.get('content-length'))
    
    # Create pretty progressbar
    progressbar = StandardBar()
    
    # Initialize the bar
    progressbar.start()
    # Add task for the downloding progress
    active_task = progressbar.add_task(
        description = "Downloading",
        total       = total_length if total_length is not None else Optional[float](),
        message     = "",
    )
        
    # Write content to the file
    with open(file, "wb") as file_handle:

        # Download and save file chunk by chunk
        for data in response.iter_content(chunk_size=chunk_size):
            file_handle.write(data)
            progressbar.update(
                task_id=active_task,
                advance=chunk_size,
            )

        # Flush write buffor before closing the file
        file_handle.flush()
        # Finalize progresbar
        progressbar.stop()

# ================================================================================================================================== #
