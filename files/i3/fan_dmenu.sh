R=$(dmenu -p "Fan Speed:" </dev/null)
if [[ -n "${R/[ ]*\n/}" ]]; then
	nbfc set -s "$R"
else
	nbfc set -a
fi