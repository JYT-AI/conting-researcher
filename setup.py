from setuptools import find_packages, setup

LATEST_VERSION = "0.15.0"

def check_gpt_researcher_conflict():
    """설치 시 gpt-researcher 충돌 확인 및 경고"""
    try:
        import pkg_resources
        try:
            existing_pkg = pkg_resources.get_distribution('gpt-researcher')
            print("\n" + "="*60)
            print("⚠️  WARNING: PACKAGE CONFLICT DETECTED!")
            print("="*60)
            print(f"📦 Found existing gpt-researcher v{existing_pkg.version}")
            print("🔄 conting-researcher is an enhanced version of gpt-researcher")
            print("\n💡 To avoid conflicts, run this command:")
            print("   pip uninstall gpt-researcher -y && pip install conting-researcher")
            print("\n🎯 Both packages use the same import: 'from gpt_researcher import GPTResearcher'")
            print("   The last installed package will take precedence.")
            print("="*60 + "\n")
        except pkg_resources.DistributionNotFound:
            print("✅ No gpt-researcher conflict detected. Safe to install!")
    except ImportError:
        pass  # pkg_resources not available

# 설치 시 충돌 확인 실행
check_gpt_researcher_conflict()

exclude_packages = [
    "selenium",
    "webdriver",
    "fastapi",
    "fastapi.*",
    "uvicorn",
    "jinja2",
    "gpt-researcher",
    "langgraph"
]

with open(r"README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

with open("requirements.txt", "r") as f:
    reqs = [line.strip() for line in f if not any(pkg in line for pkg in exclude_packages)]

setup(
    name="conting-researcher",
    version=LATEST_VERSION,
    description="Conting Researcher - A fork of GPT-Researcher with enhanced features for comprehensive web research",
    package_dir={'gpt_researcher': 'gpt_researcher'},
    packages=find_packages(exclude=exclude_packages),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/JYT-AI/conting-researcher",
    author="hurxxxx",
    author_email="hurxxxx@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    python_requires='>=3.11',
    install_requires=reqs,


)