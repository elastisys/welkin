#!/bin/bash
# Why this complication?
# See https://github.com/lycheeverse/lychee/issues/1819
curl -s https://elastisys.io/welkin/sitemap.xml \
  | grep -oP '(?<=<loc>).*?(?=</loc>)' \
  | lychee --files-from -
