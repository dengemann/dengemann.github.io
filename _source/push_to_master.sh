#!/usr/bin/env/bash
rsync -avzh output ../

cd (../ &&
    git ci -am 'updates' &&
    git commit -m 'rebuild pages' --allow-empty &&
    git push origin master)
