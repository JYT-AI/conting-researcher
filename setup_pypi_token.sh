#!/bin/bash

echo "🔐 PyPI Token Setup Script"
echo "=========================="

# 방법 1: 환경변수 설정 (임시)
echo ""
echo "방법 1: 현재 세션에서만 사용 (임시)"
echo "export TWINE_PASSWORD=your_api_token_here"
echo ""

# 방법 2: .bashrc에 추가 (영구)
echo "방법 2: 영구 설정 (.bashrc에 추가)"
echo "echo 'export TWINE_PASSWORD=your_api_token_here' >> ~/.bashrc"
echo "source ~/.bashrc"
echo ""

# 방법 3: .pypirc 파일 생성
echo "방법 3: .pypirc 파일 생성 (추천)"
echo "다음 내용으로 ~/.pypirc 파일을 생성하세요:"
echo ""
echo "[distutils]"
echo "index-servers = pypi"
echo ""
echo "[pypi]"
echo "username = __token__"
echo "password = your_api_token_here"
echo ""

# 실제로 .pypirc 파일 생성할지 묻기
read -p "지금 .pypirc 파일을 생성하시겠습니까? (y/n): " create_pypirc

if [ "$create_pypirc" = "y" ] || [ "$create_pypirc" = "Y" ]; then
    read -s -p "PyPI API 토큰을 입력하세요: " api_token
    echo ""
    
    cat > ~/.pypirc << EOF
[distutils]
index-servers = pypi

[pypi]
username = __token__
password = $api_token
EOF
    
    chmod 600 ~/.pypirc
    echo "✅ .pypirc 파일이 생성되었습니다!"
    echo "이제 deploy.sh 스크립트를 실행할 수 있습니다."
else
    echo "수동으로 설정하시려면 위의 방법 중 하나를 선택하세요."
fi
