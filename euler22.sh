cat p022_names.txt | tr , "\n" | tr -d \" | sort | perl -MList::Util=sum -nE 'chomp; $sum += $. * sum map {ord($_) - 64} split ""; END {say $sum}'
