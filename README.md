# MKS Korea

mks.rubiworkshop.com 원페이지 정적 사이트 (GitHub Pages). quoc.rubiworkshop.com과 같은 구조와 디자인 체계입니다.

- `index.html` 한국어 원페이지 (MKS · RANGE · SYLVAN · LAMBDA · CITY · EZY · GUIDE · STORY · SHOWROOM)
- 디자인은 rubi.kr과 같은 체계: 영문 Pretendard · 한글 에스코어 드림, 웨이트 400, 흑백과 얇은 라인, 각진 버튼, 라이트/다크 자동. 일본어 페이지는 빌드 시 Noto Sans JP로 바뀝니다.
- `en/index.html`, `ja/index.html` 영어 · 일본어 페이지 (빌드로 생성, 직접 수정하지 않음)
- `index.src.html` 편집용 한국어 원본. 페달 고르기 표는 `{{GUIDE_TABLE}}` 자리에 빌드 시 채워집니다 (`tools/build.py`의 `GUIDE`).
- `i18n/` 번역 사전 (`ko.json` 원문 목록, `en.json` · `ja.json` 원문→번역)
- `tools/build.py` 한국어 페이지, 번역 페이지, sitemap.xml을 한 번에 생성
- `404.html` 하위 주소(/sylvan, /lambda, /allways, /ezy, /guide, /dealers 등)를 섹션으로 연결
- `images/` 섹션별 이미지 (`hero`, `brand`, `sylvan`, `lambda`, `city`, `ezy`)
- `.github/image-manifest.txt` + `fetch-images.yml` 이미지 URL을 적으면 Actions가 받아 커밋

## 처음 올릴 때
1. Settings → Pages → Source: Deploy from a branch, Branch: main / (root).
2. 도메인 DNS에 `mks` CNAME 레코드를 `sereno-kwon.github.io`로 추가하고, Pages 설정의 Custom domain에 `mks.rubiworkshop.com`을 넣습니다 (CNAME 파일은 이미 들어 있음).
3. 이미지를 채웁니다 (아래).
4. 파비콘: `images/favicon-48.png`, `images/favicon-96.png`, `images/apple-touch-icon.png`(180px), `images/logo-512.png`. 헤더 로고는 지금 텍스트 워드마크(MKS)입니다.

## 이미지
`images/`의 사진은 MKS 공식 사이트(mkspedal.com)에서 가져왔고, 출처 URL은 `.github/image-manifest.txt`에 적혀 있습니다. 큰 공장 사진은 가로 2400px로 줄였습니다.
- 바꾸려면 `images/`의 파일을 지우고 매니페스트의 URL을 바꿔 푸시하거나(Actions가 받아 커밋), 같은 경로에 새 사진을 넣습니다.
- 공식 사이트의 제품 사진은 대부분 750×500 크기라 크게 보면 흐릴 수 있습니다. 히어로 4번(EZY)과 실반 토클립 사진은 루비에서 직접 촬영한 사진으로 바꾸는 것을 권합니다.
- 쇼룸 섹션 사진(`brand/10`, `brand/11`)은 MKS 공장·전시 사진이라, 루비워크샵 매장 사진으로 바꾸는 것이 좋습니다.
- 이미지가 없는 자리는 회색 'MKS' 자리표시로 보입니다.

## 문구 수정과 번역
1. `index.src.html`의 한국어 문구를 고칩니다.
2. `python3 tools/build.py` 로 한국어 페이지를 만들고, `python3 i18n/extract.py` 로 `ko.json`을 갱신합니다.
3. 새로 생기거나 바뀐 한국어 문장을 `en.json` · `ja.json`에 같은 키로 추가합니다. HTML 태그는 원문과 똑같이 유지합니다.
4. 다시 `python3 tools/build.py` 를 실행하면 번역되지 않은 문장이 있을 때 목록으로 알려줍니다.

빌드에는 `beautifulsoup4`가 필요합니다 (`pip install beautifulsoup4`).

## 확인이 필요한 내용
회사 연혁(1943 창업, 1946 페달 전환, 1949 법인 설립, 1951 통산대신상, 1956 JIS), NJS 유일 인증, 냉간 단조·자체 열처리·ADC6 바디, EZY/Ezy Superior, 회장 인용문은 MKS 공식 사이트의 회사 소개·연혁·제품 페이지와 대조했습니다.
아래는 공식 페이지에서 직접 확인하지 못한 내용입니다.
- 실반 로드·트랙의 토클립 장착 여부, 실반 투어링의 양면 구조, 스핀들 9/16인치
- 람다·올웨이즈·어반 플랫폼·GR-9의 세부 형태(양면 여부 등)와 컬러
- 무게 등 수치 스펙은 넣지 않았습니다. 필요하면 각 Specification 표에 추가하세요.

## 링크
- 헤더 SHOP, 각 모델의 "루비워크샵에서 보기" 버튼: `https://rubiworkshop.com/mks`
- 거래처 문의: 루비서플라이 02-516-8465, 카카오톡 채널 `https://pf.kakao.com/_NFnBj/chat`
- 푸터 MKS Global: `https://www.mkspedal.com/`
