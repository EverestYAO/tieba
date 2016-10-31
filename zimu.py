import re

with open('Suicide.Squad.2016.1080p.HDRip.KORSUB.x264.AAC2.0-STUTTERSHIT.mp4_1477203089.srt',encoding='utf-8') as reader, open('zimu.srt', 'w', encoding='utf-8') as writer:


    for line in reader:
        m = re.match(r'[\u4e00-\u9fa5]', line)
        if m:
            continue
        print(line)
        writer.write(line)
    writer.close()
