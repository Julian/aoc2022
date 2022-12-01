gsed -z 's/\n/+/ig' data/input | gsed -z 's/++/\n/ig' | gsed -z 's/+$//' | bc | sort -n -r | head -n1
