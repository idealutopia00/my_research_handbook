.PHONY: all clean

# 只要在终端输 'make'，它就会跑这一串
all:
	xelatex -synctex=1 -interaction=nonstopmode main
	biber main
	xelatex -synctex=1 -interaction=nonstopmode main
	xelatex -synctex=1 -interaction=nonstopmode main

# 只要输 'make clean'，它就清理垃圾
clean:
	latexmk -c
	# rm -f *.bbl *.run.xml *.synctex.gz