# Style, format, etc. checks:
format:
	black todo/ tests/

style-check:
	flake8 todo/ tests/

format-check:
	black --check todo/ tests/

all-checks: format-check style-check
