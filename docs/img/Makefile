all: \
		welkin-c4model-level2.png \
		harbor-usage.png

preview:
		echo "Performing continuous preview ..." >&2
		while true; do \
				make all; \
				inotifywait -e close_write . ; \
				sleep 0.5; \
		done

%.svg: %.dot
	dot -Tsvg $< > $@

%.png: %.svg
	rsvg-convert $< > $@
