#!/bin/bash
curl -s https://elastisys.io/welkin/sitemap.xml \
  | grep -oP '(?<=<loc>).*?(?=</loc>)' \
  | xargs lychee
