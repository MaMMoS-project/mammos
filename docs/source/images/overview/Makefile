diagram.png: diagram.puml
	plantuml -tpng diagram.puml


diagram.pdf: diagram.puml
	plantuml -teps diagram.puml
	epstopdf diagram.eps


clean:
	rm -f diagram.pdf diagram.png

