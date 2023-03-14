import subprocess

def download(url,output_file,duration):
    subprocess.run(['ffmpeg', '-i', url, '-t', str(duration), '-c', 'copy', output_file], check=True)