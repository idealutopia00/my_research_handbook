.PHONY: all clean view distclean check

# 默认目标：编译完整文档
all:
	xelatex -synctex=1 -interaction=nonstopmode main
	biber main
	xelatex -synctex=1 -interaction=nonstopmode main
	xelatex -synctex=1 -interaction=nonstopmode main

# 快速编译（单次，用于检查）
fast:
	xelatex -synctex=1 -interaction=nonstopmode main

# 查看生成的PDF（macOS）
view:
	open main.pdf

# 清理中间文件
clean:
	latexmk -c
	rm -f *.bbl *.run.xml *.synctex.gz *.nav *.snm *.vrb

# 深度清理（包括PDF）
distclean: clean
	rm -f main.pdf

# 检查语法和引用
check:
	chktex -q main.tex || true

# 编译并查看
all-view: all view

# 统计字数（近似）
wordcount:
	detex main.tex | wc -w