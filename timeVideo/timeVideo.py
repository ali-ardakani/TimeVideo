# timeVideos.py

# Get total time of all videos in a directory

from datetime import timedelta
from os import walk
from os.path import join

import cv2


class TimeVideos:
    """
    Calculate total time of all videos in a directory
    
    Parameters
    ----------
    path : str
        Path to directory
    exts : list
        List of extensions to search for
    
    Returns
    -------
    total_time : datetime.timedelta
        Total time of all videos in a directory
    
    Examples
    --------
    >>> from timeVideos import TimeVideos
    >>> path = "."
    >>> exts = [".mp4", ".avi"]
    >>> time_videos = TimeVideos(path, exts)
    >>> time_videos()
    5:00:00
    >>> print(time_videos)
    Total time: 5:00:00
    """
    def __init__(self, path: str, exts: list):
        self.path = path
        self.exts = exts
        self.__total_time = 0

    def get_time(self, filename):
        """
        Get time from file
        """
        video = cv2.VideoCapture(filename)
        frames = video.get(cv2.CAP_PROP_FRAME_COUNT)
        fps = video.get(cv2.CAP_PROP_FPS)

        seconds = frames / fps

        return seconds

    def get_total_time(self):
        """
        Get total time of all videos in a directory
        """
        if self.__total_time:
            return self.__total_time
        # get all files with extension
        files = []
        for (dirpath, dirnames, filenames) in walk(self.path):
            for ext in self.exts:
                files.extend([
                    join(dirpath, file) for file in filenames
                    if file.endswith(ext)
                ])

        total_time = 0
        for file in files:
            time = self.get_time(file)
            total_time += time
        self.__total_time = timedelta(seconds=total_time)
        return self.__total_time

    def __call__(self):
        return self.get_total_time()

    def __repr__(self):
        return f"Total time: {self.get_total_time()}"
    
if __name__ == "__main__":
    import sys
    # get --path and --exts from command line
    path = sys.argv[sys.argv.index("--path") + 1]
    exts = sys.argv[sys.argv.index("--exts") + 1].split(",")
    time_videos = TimeVideos(path, exts)
    print(time_videos())