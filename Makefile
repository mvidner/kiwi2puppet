# no building necessary
TOOL=kiwi2puppet
all: ${TOOL}
# test data
%.pp: %.xml ${TOOL}
	./${TOOL} $< > $@
# a crude test
check:
	puppet --parseonly --ignoreimport *.pp
