# ====================================================================================================================================
# @file       archieves.py
# @author     Krzysztof Pierczyk (krzysztof.pierczyk@gmail.com)
# @maintainer Krzysztof Pierczyk (krzysztof.pierczyk@gmail.com)
# @date       Thursday, 22nd December 2022 3:02:47 am
# @modified   Thursday, 22nd December 2022 4:24:00 am
# @project    py-utils
# @brief      General-use utilities for downloading unpacking archieve files
# 
# 
# @copyright Krzysztof Pierczyk © 2022
# ====================================================================================================================================

# ============================================================== Doc =============================================================== #

""" 

.. module:: 
   :platform: OS Independent
   :synopsis: General-use utilities for downloading unpacking archieve files

.. moduleauthor:: Krzysztof Pierczyk <krzysztof.pierczyk@gmail.com>

"""

# ============================================================ Imports ============================================================= #

from pathlib import Path
from pyutils.visuals.progressbars import StandardBar
from typing import Optional
import zipfile
import tarfile

# ============================================================ Script ============================================================== #

def extract_archieve(
    archieve : str,
    outdir : Path = '.',
) :

    # Select proper utilities for handling the archieve
    if archieve.endswith('.zip'):

        arch_wrapper = zipfile.ZipFile
        item_size    = lambda item : item.file_size
        size         = lambda arch : sum([item_size(fileinfo) for fileinfo in arch.filelist])
        items        = lambda arch : arch.infolist()
        extract_item = lambda arch, item : arch.extract(item, outdir)
        
    elif archieve.endswith(('.tar', '.tar.bz2', '.tar.gz', '.tar.xz')):

        # Extract extension
        extension = Path(archieve).suffixes[-1]
        # Remove leading '.'
        extension = extension[1:]

        arch_wrapper = lambda name : tarfile.open(name, f"r:{extension if extension != 'tar' else ''}")
        item_size    = lambda item : item.size
        size         = lambda arch : sum([item_size(fileinfo) for fileinfo in arch.getmembers()])
        items        = lambda arch : arch
        extract_item = lambda arch, item : arch.extract(item, outdir)

    # Unsupported format
    else:
        raise Exception(f'File {archieve} (unsupported archieve format)')
        
    # Write content to the file
    with arch_wrapper(archieve) as arch:

        # Create pretty progressbar
        progressbar = StandardBar()
        
        # Compute size of the archieve
        archieve_size = size(arch)
        # Initialize the bar
        progressbar.start()
        # Add task for the downloding progress
        active_task = progressbar.add_task(
            description = "Extracting",
            total       = archieve_size if archieve_size is not None else Optional[float](),
            message     = "",
        )
        
        # Download and save file chunk by chunk
        for item in items(arch):
            extract_item(arch, item)
            progressbar.update(
                task_id=active_task,
                advance=item_size(item),
            )

        # Finalize progresbar
        progressbar.stop()

# ================================================================================================================================== #
