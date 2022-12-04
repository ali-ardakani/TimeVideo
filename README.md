<div align="center">

<h1>Time Video</h1>

<p>Time Video is a simple script to sum the time of a video.</p>

</div>
 
<div align="left">
 
<h2 id="about">Usage</h2>
 
<h3>Install Requirements</h3>
     
```bash
pip install -r requirements.txt
```

<h3>Example</h3>
     
```bash
python timeVideo/timeVideo.py --path /path/to/video_dir --exts mp4,avi
```


```python
from time_video import TimeVideo
    
time_video = TimeVideo(path='/path/to/video_dir', exts=['mp4', 'avi'])
time_video()
```

</div>
