# PyPI 배포 및 버전 관리 가이드

## 1. 사전 준비

### PyPI 계정 설정
1. [PyPI](https://pypi.org) 계정 생성
2. 계정 설정 → API 토큰 생성
3. 토큰을 안전한 곳에 저장(원드라이브 - 계정관리)

### 필요한 도구 설치
```bash
pip install twine build
```

## 2. 버전 관리

### 버전 번호 규칙 (Semantic Versioning)
- **MAJOR.MINOR.PATCH** (예: 1.2.3)
- **MAJOR**: 호환되지 않는 API 변경
- **MINOR**: 기능 추가 (하위 호환)
- **PATCH**: 버그 수정

### 버전 업데이트 위치
1. `setup.py` → `LATEST_VERSION` 변수
2. `pyproject.toml` → `version` 필드 (2곳)

```python
# setup.py
LATEST_VERSION = "0.14.1"  # 업데이트

# pyproject.toml
[tool.poetry]
version = "0.14.1"  # 업데이트

[project]
version = "0.14.1"  # 업데이트
```

## 3. 배포 프로세스

### Step 1: 환경 활성화
```bash
conda activate gpt-researcher
```

### Step 2: 기존 빌드 파일 정리
```bash
rm -rf dist/* build/*
```

### Step 3: 패키지 빌드
```bash
python setup.py sdist bdist_wheel
```

### Step 4: 빌드 검증
```bash
twine check dist/*
```

### Step 5: PyPI 업로드
```bash
twine upload dist/*
```

## 4. 자동화 스크립트

### 배포 스크립트 생성 (`deploy.sh`)
```bash
#!/bin/bash
set -e

echo "🚀 Starting deployment process..."

# 환경 활성화
source ~/miniconda3/etc/profile.d/conda.sh
conda activate gpt-researcher

# 정리
echo "🧹 Cleaning previous builds..."
rm -rf dist/* build/*

# 빌드
echo "🔨 Building package..."
python setup.py sdist bdist_wheel

# 검증
echo "✅ Checking package..."
twine check dist/*

# 업로드
echo "📦 Uploading to PyPI..."
twine upload dist/*

echo "✨ Deployment completed!"
```

### 스크립트 실행 권한 부여
```bash
chmod +x deploy.sh
```

## 5. 버전 업데이트 체크리스트

- [ ] 코드 변경사항 커밋
- [ ] `setup.py`의 `LATEST_VERSION` 업데이트
- [ ] `pyproject.toml`의 `version` 필드 업데이트 (2곳)
- [ ] `CHANGELOG.md` 업데이트 (선택사항)
- [ ] Git 태그 생성: `git tag v0.14.1`
- [ ] 변경사항 푸시: `git push origin main --tags`
- [ ] 패키지 빌드 및 배포

## 6. 트러블슈팅

### 일반적인 오류들

**1. 중복 버전 오류**
```
File already exists
```
→ 버전 번호를 증가시키고 다시 시도

**2. 인증 오류**
```
Invalid or non-existent authentication information
```
→ API 토큰 재확인 또는 재생성

**3. 패키지 구조 오류**
```
No files/directories in dist/
```
→ `setup.py` 설정 확인, 특히 `packages` 설정

### 유용한 명령어

```bash
# 현재 설치된 패키지 버전 확인
pip show conting-researcher

# PyPI에서 패키지 정보 확인
pip index versions conting-researcher

# 특정 버전 설치
pip install conting-researcher==0.14.0

# 최신 버전으로 업그레이드
pip install --upgrade conting-researcher
```

## 7. 보안 고려사항

- API 토큰을 코드에 하드코딩하지 말 것
- `.pypirc` 파일 사용 시 권한 설정 주의
- 환경변수 또는 키링 사용 권장

```bash
# 환경변수로 토큰 설정
export TWINE_PASSWORD=your_api_token_here
twine upload dist/*
```

## 8. 참고 링크

- [PyPI 공식 문서](https://packaging.python.org/)
- [Semantic Versioning](https://semver.org/)
- [Twine 문서](https://twine.readthedocs.io/)
