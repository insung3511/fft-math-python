# Fourier Transform by Python
이미지 프로세싱에서 푸리에 변환이 어떤 식으로 사용이 되는지를 수학 및 OpenCV, Numpy 를 통해서 확인하며 공부를 하였습니다.

# Directory
```
./docs/2021수학발표.pdf
```
수학적 기법 및 파이썬에서의 작동 원리와 활용 예시를 간단히 정리한 발표 자료 입니다. 해당 본 문서는 <a href="https://www.apple.com/keynote/">Keynote</a>로 작성이 되었으며 다른 이들이 볼 수 있게 PDF 로 업로드 하였습니다. 원본 문서는 업로드 예정에 없습니다.

만일 필요할 경우 Issue에 작성을 해주시면 검토 후에 따로 드리던지 하겠습니다.
```
img
├── jogang.jpg
├── nefus.jpg
└── sky.jpg
```
푸리에를 통한 이미지 처리를 하게 될 예시 사진들 입니다. 모두 제가 직접 찍은 사진이며 해당 사진을 무단으로 사용시 불이익이 가해질 수 있습니다. 그러니 사용시에는 Issue 로 미리 말씀 하시고 사용해주시기 바랍니다.
```
src
├── cv
│   ├── cv_inverse.py
│   ├── cv_main.py
│   └── ft_in_cv.py
└── numpy
    ├── hpf_and_jet.py
    ├── np_main.py
    └── spectrum.py
```
cv 폴더에는 OpenCV 를 활용한 푸리에 변환의 코드들이 담겨져 있으며 cv_inverse.py 는 원본 사진을 다시 복구하는 코드가 있습니다. ft_in_cv.py 는 OpenCV의 푸리에 변환을 통해 원본 사진에서 저주파 영역을 제거 하여 가우시안 블러를 필터링 해주는 코드 입니다. cv_main.py 는 해당 코드를 모두 합쳐놓은 코드 입니다.

numpy 폴더에는 hpf_and_jet.py 는 Numpy 모듈을 활용하여 이지미의 고주파 영역 및 저주파 영역을 분간 해놓은 코드 입니다. Spectrum.py 는 Numpy 모듈을 활용하여 fft의 스펙트럼을 보여주고 마지막 np_main.py 는 Numpy 모듈을 활용한 모든 코드들을 작성 해 놓은 코드 입니다.

# Explain
코드에 대한 설명은 cv, numpy 폴더에 README.md 파일로 작성을 해둘 예정 입니다. 차근차근 적을터이니 궁금하신 점은 Issue 혹은 저의 이메일로 연락주시면 되겠습니다. 감사합니다 :)