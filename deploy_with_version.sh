#!/bin/bash
set -e

# 사용법 체크
if [ $# -eq 0 ]; then
    echo "사용법: $0 <new_version>"
    echo "예시: $0 0.14.1"
    exit 1
fi

NEW_VERSION=$1

echo "🚀 Starting deployment process for version $NEW_VERSION..."

# 환경 활성화
source ~/miniconda3/etc/profile.d/conda.sh
conda activate gpt-researcher

# 버전 업데이트
echo "📝 Updating version numbers..."

# setup.py 업데이트
sed -i "s/LATEST_VERSION = \".*\"/LATEST_VERSION = \"$NEW_VERSION\"/" setup.py

# pyproject.toml 업데이트 (tool.poetry.version)
sed -i "/\[tool\.poetry\]/,/\[/ s/version = \".*\"/version = \"$NEW_VERSION\"/" pyproject.toml

# pyproject.toml 업데이트 (project.version)
sed -i "/\[project\]/,/\[/ s/version = \".*\"/version = \"$NEW_VERSION\"/" pyproject.toml

echo "✅ Version updated to $NEW_VERSION"

# Git 커밋 (선택사항)
read -p "Git에 커밋하시겠습니까? (y/n): " commit_git
if [ "$commit_git" = "y" ] || [ "$commit_git" = "Y" ]; then
    git add setup.py pyproject.toml
    git commit -m "Bump version to $NEW_VERSION"
    git tag "v$NEW_VERSION"
    echo "✅ Git commit and tag created"
fi

# 정리
echo "🧹 Cleaning previous builds..."
rm -rf dist/* build/*

# 빌드
echo "🔨 Building package..."
python setup.py sdist bdist_wheel

# 검증
echo "✅ Checking package..."
twine check dist/*

# 업로드 확인
echo "📦 Ready to upload version $NEW_VERSION to PyPI"
read -p "업로드를 진행하시겠습니까? (y/n): " proceed_upload

if [ "$proceed_upload" = "y" ] || [ "$proceed_upload" = "Y" ]; then
    # .pypirc 파일이 있는지 확인
    if [ -f ~/.pypirc ]; then
        echo "📤 Uploading using .pypirc credentials..."
        twine upload dist/*
    elif [ ! -z "$TWINE_PASSWORD" ]; then
        echo "📤 Uploading using environment variable..."
        twine upload dist/* --username __token__
    else
        echo "⚠️  No credentials found!"
        echo "Please run ./setup_pypi_token.sh first"
        exit 1
    fi
    
    # Git 푸시 (선택사항)
    if [ "$commit_git" = "y" ] || [ "$commit_git" = "Y" ]; then
        read -p "Git에 푸시하시겠습니까? (y/n): " push_git
        if [ "$push_git" = "y" ] || [ "$push_git" = "Y" ]; then
            git push origin main --tags
            echo "✅ Pushed to Git repository"
        fi
    fi
    
    echo "✨ Deployment completed successfully!"
    echo "🎉 Version $NEW_VERSION is now available on PyPI!"
else
    echo "❌ Upload cancelled"
fi
