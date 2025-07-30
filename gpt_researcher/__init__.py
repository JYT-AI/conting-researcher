import os
import sys
from .agent import GPTResearcher

__all__ = ['GPTResearcher']
__version__ = "0.15.0"

# Conting-Researcher 브랜딩 메시지
def _show_branding():
    """Import 시 브랜딩 메시지 표시 (한 번만)"""
    # 환경변수로 메시지 표시 여부 제어
    if os.getenv('CONTING_RESEARCHER_QUIET', '').lower() in ('1', 'true', 'yes'):
        return

    # 이미 표시했는지 확인 (중복 방지)
    if hasattr(_show_branding, '_shown'):
        return
    _show_branding._shown = True

    # 테스트 환경에서는 메시지 숨김
    if 'pytest' in sys.modules or 'unittest' in sys.modules:
        return

    print("🚀 Conting-Researcher v0.15.0 - Enhanced GPT-Researcher")
    print("   📦 pip install conting-researcher")
    print("   🔗 https://github.com/JYT-AI/conting-researcher")

# Import 시 브랜딩 메시지 표시
_show_branding()