WWU_TEXLIVE_IMAGE=wwutex
WWU_TEXLIVE_TAG=854c753
THIS_DIR = $(patsubst %/,%,$(dir $(abspath $(lastword $(MAKEFILE_LIST)))))

ifndef CI
    NO_DOCKER = $(shell docker image inspect 925ef62cead9; echo $$? )
    INTERACTIVE = -ti
    USERARGS = -e LOCAL_USER=${USER} -e LOCAL_UID=$(shell id -u) -e LOCAL_GID=$(shell id -g)
else
    NO_DOCKER = 0
    INTERACTIVE =
    USERARGS = -e LOCAL_USER=${USER} -e LOCAL_UID=$(shell id -u) -e LOCAL_GID=$(shell id -g)
endif

ifeq (${NO_DOCKER}, 0)
    DOCKER = docker run -m 3G $(INTERACTIVE) $(USERARGS) -v $(THIS_DIR):/src $(WWU_TEXLIVE_IMAGE):$(WWU_TEXLIVE_TAG)
    # don't want to (and cannot) run a viewer from inside the image
    VIEW = -view=none
else
    DOCKER =
    VIEW =
endif

LATEXMK = $(DOCKER) latexmk -f


all: superbowl_squares.pdf

superbowl_squares.pdf:  superbowl_squares.tex
	python sbsq.py
	$(LATEXMK) $(PREVIEW_CONTINUOUSLY) superbowl_squares.tex

superbowl_squares: superbowl_squares.pdf

check: superbowl_squares
	$(DOCKER) chktex superbowl_squares.tex
	$(DOCKER) lacheck superbowl_squares.tex

FORCE:

.PHONY: watch clean superbowl_squares.pdf check FORCE
# Set the PREVIEW_CONTINUOUSLY variable to -pvc to switch latexmk into the preview continuously mode
watch: PREVIEW_CONTINUOUSLY=-pvc $(VIEW)
watch: superbowl_squares.pdf

# -bibtex also removes the .bbl files
clean:
# 	rm -f includes/labels.tex
	$(DOCKER) latexmk -verbose -C -bibtex
