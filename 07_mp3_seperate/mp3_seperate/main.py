from spleeter.separator import Separator
import os
import sys



base="./target"

if __name__ == '__main__':
    # Spleeter 모델 초기화 (2 stems 모델 사용)
    separator = Separator('spleeter:2stems')

    # 분리할 오디오 파일
    input_audio = base+'.mp3'

    # 결과를 저장할 디렉토리
    output_dir = 'output'

    # 오디오 파일 분리
    separator.separate_to_file(input_audio, output_dir)