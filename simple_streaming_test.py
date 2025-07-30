#!/usr/bin/env python3
"""
GPT-Researcher 스트리밍 간단 테스트
실시간으로 연구 진행상황을 받아볼 수 있는 예제
"""

import asyncio
import os
from datetime import datetime
from dotenv import load_dotenv

# 환경변수 로드
load_dotenv()

# GPT-Researcher 임포트
from gpt_researcher import GPTResearcher


class StreamingHandler:
    """실시간 스트리밍을 처리하는 핸들러"""
    
    def __init__(self):
        self.start_time = datetime.now()
        self.message_count = 0
        
    async def send_json(self, data):
        """WebSocket의 send_json 메서드를 시뮬레이션"""
        self.message_count += 1
        elapsed = (datetime.now() - self.start_time).total_seconds()
        
        # 데이터 파싱
        msg_type = data.get('type', 'unknown')
        content = data.get('content', '')
        output = data.get('output', '')
        
        # 중요한 메시지만 출력
        if msg_type == 'logs':
            if content in ['starting_research', 'agent_generated', 'subqueries', 'report_written']:
                print(f"🔔 [{elapsed:5.1f}s] {content}: {output[:60]}...")
            elif content == 'added_source_url':
                print(f"📎 [{elapsed:5.1f}s] 소스 추가: {data.get('metadata', '')}")
        elif msg_type == 'report':
            # 리포트 내용은 10개마다 한 번씩만 출력
            if self.message_count % 10 == 0:
                print(f"📝 [{elapsed:5.1f}s] 리포트 작성 중... ({len(output)}자)")


async def simple_research_test():
    """간단한 연구 테스트"""
    print("🚀 GPT-Researcher 스트리밍 테스트")
    print("=" * 50)
    
    # API 키 확인
    if not os.getenv("OPENAI_API_KEY"):
        print("❌ OPENAI_API_KEY 환경변수가 필요합니다")
        return
    
    if not (os.getenv("SERPER_API_KEY") or os.getenv("TAVILY_API_KEY")):
        print("❌ SERPER_API_KEY 또는 TAVILY_API_KEY 환경변수가 필요합니다")
        return
    
    print("✅ API 키 확인 완료")
    
    # 스트리밍 핸들러 생성
    handler = StreamingHandler()
    
    # 연구 주제
    query = "파이썬 머신러닝 기초"
    print(f"🔍 연구 주제: {query}")
    print("📡 실시간 스트리밍 시작...\n")
    
    try:
        # GPTResearcher 생성 (스트리밍 핸들러 연결)
        researcher = GPTResearcher(
            query=query,
            report_type="outline_report",  # 빠른 아웃라인 리포트
            websocket=handler,  # 스트리밍 핸들러 연결
            verbose=True
        )
        
        # 연구 수행 (실시간 스트리밍됨)
        print("🔬 연구 시작...")
        await researcher.conduct_research()
        
        print("📝 리포트 작성...")
        report = await researcher.write_report()
        
        # 결과 출력
        print("\n" + "=" * 50)
        print("✅ 연구 완료!")
        print(f"📊 총 스트리밍 메시지: {handler.message_count}개")
        print(f"📄 리포트 길이: {len(report)}자")
        print("\n📋 생성된 리포트 미리보기:")
        print("-" * 30)
        print(report[:500] + "..." if len(report) > 500 else report)
        
        return True
        
    except Exception as e:
        print(f"\n❌ 오류 발생: {e}")
        return False


if __name__ == "__main__":
    print("🎯 GPT-Researcher 스트리밍 기능 테스트")
    print("실시간으로 연구 진행상황을 확인할 수 있습니다.\n")
    
    # 테스트 실행
    success = asyncio.run(simple_research_test())
    
    if success:
        print("\n🎉 스트리밍 테스트 성공!")
        print("💡 이제 웹소켓을 통해 실시간 연구 진행상황을 받을 수 있습니다.")
    else:
        print("\n💥 테스트 실패")
        print("💡 환경변수 설정을 확인해주세요:")
        print("   - OPENAI_API_KEY")
        print("   - SERPER_API_KEY 또는 TAVILY_API_KEY")
