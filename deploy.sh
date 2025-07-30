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

# 업로드 (환경변수에서 토큰 읽기)
echo "📦 Uploading to PyPI..."
if [ -z "$TWINE_PASSWORD" ]; then
    echo "⚠️  TWINE_PASSWORD environment variable not set"
    echo "Please run: export TWINE_PASSWORD=your_api_token"
    echo "Or use: ./deploy.sh --interactive"
    exit 1
fi

twine upload dist/* --username __token__

echo "✨ Deployment completed!"
