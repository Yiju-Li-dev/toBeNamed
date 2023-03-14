from download import download

def main():
    url = 'https://d1--ov-gotcha07.bilivideo.com/live-bvc/311399/live_300702024_9725507.flv?expires=1678785632&len=0&oi=1745766021&pt=web&qn=0&trid=1000fe00ebdea39b4bfca7c6506c0b63c62c&sigparams=cdn,expires,len,oi,pt,qn,trid&cdn=ov-gotcha07&sign=9a9b0a9d7d13e3a7d20ec7609d49320d&sk=a2c7c534ce579871fd03c9c2928cc693&p2p_type=0&src=57345&sl=2&free_type=0&mid=153405045&pp=rtmp&machinezone=ylf&source=onetier&trace=0&site=063f38c483d279c7ddfb1175e5e1436e&order=1'
    output_file = 'out.mp4'
    duration = int(input("duration: "))

    download(url,output_file,duration)

main()