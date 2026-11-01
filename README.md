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
아직 이미지가 없습니다. 페이지는 이미지가 없는 자리를 회색 'MKS' 자리표시로 보여주므로, 하나씩 채워도 됩니다.
- 방법 1: `.github/image-manifest.txt`의 각 줄 `# URL images/...`를 `https://... images/...` 형태로 바꿔 main에 푸시하면 Actions가 받아 커밋합니다. MKS 공식 사이트(mkspedal.com) 이미지를 쓸 때 편합니다.
- 방법 2: 루비에서 촬영한 사진을 같은 경로로 `images/`에 직접 넣습니다.
- 권장 비율: 히어로 가로 2400px 이상, 제품 컷(`sylvan/01~04`, `lambda/01~04`, `ezy/03~06`) 8:9, 카드(`brand/02~05`, `city/01~03`) 4:5, `brand/01` 21:9, `og.jpg` 2400×1200.

## 문구 수정과 번역
1. `index.src.html`의 한국어 문구를 고칩니다.
2. `python3 tools/build.py` 로 한국어 페이지를 만들고, `python3 i18n/extract.py` 로 `ko.json`을 갱신합니다.
3. 새로 생기거나 바뀐 한국어 문장을 `en.json` · `ja.json`에 같은 키로 추가합니다. HTML 태그는 원문과 똑같이 유지합니다.
4. 다시 `python3 tools/build.py` 를 실행하면 번역되지 않은 문장이 있을 때 목록으로 알려줍니다.

빌드에는 `beautifulsoup4`가 필요합니다 (`pip install beautifulsoup4`).

## 확인이 필요한 내용
문구는 MKS 공식 자료를 직접 열람하지 못한 상태에서 일반적으로 알려진 사실 위주로 작성했습니다. 게시 전에 아래를 공식 자료와 대조해 주세요.
- 창업 연도(1950)와 소재지(사이타마현 도코로자와), 자체 공장 생산
- 람다의 미국 판매명 '그립 킹', 시티 페달의 EZY 버전 여부, EZY 동작 방식(밀어 넣어 잠금, 슬리브를 당겨 분리)
- 컬러 표기(실반 실버, 람다 실버·블랙)와 스펙(9/16인치, 컵 앤 콘 베어링)
- 무게 등 수치 스펙은 넣지 않았습니다. 필요하면 각 Specification 표에 추가하세요.

## 링크
- 헤더 SHOP, 각 모델의 "루비워크샵에서 보기" 버튼: `https://rubiworkshop.com/mks`
- 거래처 문의: 루비서플라이 02-516-8465, 카카오톡 채널 `https://pf.kakao.com/_NFnBj/chat`
- 푸터 MKS Global: `https://www.mkspedal.com/`
