import subprocess
import os

# 获取项目的根目录的相对路径
try:
    rdir = subprocess.check_output(['git', 'rev-parse', '--git-dir']).strip().decode('utf-8')
    rel_path = os.path.dirname(rdir)
except subprocess.CalledProcessError:
    print("未找到 Git 仓库根目录")
    exit(1)

# 更改到指定的路径
os.chdir(os.path.join(rel_path, 'src', 'latex2sympy2_extended'))

# 创建 gen 目录（如果它不存在）
os.makedirs('gen', exist_ok=True)

# 定义 ANTLR JAR 文件路径和输出目录
antlr_versions = {
    '4.13.2': 'gen/antlr4_13_2',
    '4.11.0': 'gen/antlr4_11_0',
    '4.9.3': 'gen/antlr4_9_3'
}

# 运行 ANTLR 对于每个版本的 grammar 文件
grammar_file = 'PS.g4'
for version, output_dir in antlr_versions.items():
    antlr_jar = f'../../antlr-{version}-complete.jar'
    # 确保 ANTLR JAR 文件存在
    if not os.path.isfile(antlr_jar):
        print(f"未找到 ANTLR {version} JAR 文件: {antlr_jar}")
        continue
    
    # 运行 ANTLR
    subprocess.run(['java', '-jar', antlr_jar, grammar_file, '-o', output_dir], check=True)
    print(f"ANTLR {version} 生成完成，输出目录: {output_dir}")
