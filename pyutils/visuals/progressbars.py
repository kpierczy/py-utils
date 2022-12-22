# ====================================================================================================================================
# @file       progressbars.py
# @author     Krzysztof Pierczyk (krzysztof.pierczyk@gmail.com)
# @maintainer Krzysztof Pierczyk (krzysztof.pierczyk@gmail.com)
# @date       Thursday, 22nd December 2022 3:03:37 am
# @modified   Thursday, 22nd December 2022 3:06:18 am
# @project    py-utils
# @brief      General-purpose progress bars
# 
# 
# @copyright Krzysztof Pierczyk © 2022
# ====================================================================================================================================

# ============================================================== Doc =============================================================== #

""" 

.. module:: 
   :platform: OS Independent
   :synopsis: General-purpose progress bars

.. moduleauthor:: Krzysztof Pierczyk <krzysztof.pierczyk@gmail.com>

"""

# ============================================================ Imports ============================================================= #

import rich.progress
import rich.console

# ============================================================ Script ============================================================== #

class StandardBar(rich.progress.Progress):

    '''Standard progress-base implementation'''

    def __init__(self):
        super(StandardBar, self).__init__(

            # Layout
            rich.progress.SpinnerColumn(),
            rich.progress.TextColumn("[rich.progress.description]{task.description}"),
            rich.progress.BarColumn(),
            rich.progress.DownloadColumn(),
            rich.progress.TextColumn("[bright_black][rich.progress.percentage]{task.percentage:>3.0f}%"),
            rich.progress.TextColumn("|"),
            rich.progress.TransferSpeedColumn(),
            rich.progress.TextColumn("|"),
            rich.progress.TextColumn("eta"),
            rich.progress.TimeRemainingColumn(),
            rich.progress.TextColumn("{task.fields[message]}"),
            # Config
            console   = rich.console.Console(),
            transient = False,
            
        )


# ================================================================================================================================== #
